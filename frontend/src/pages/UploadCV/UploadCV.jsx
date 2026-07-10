import { useMemo, useRef, useState } from 'react'
import LanguageSwitcher from '../../components/LanguageSwitcher.jsx'
import { useLanguage } from '../../i18n/LanguageContext.jsx'
import {
  createMockCvAnalysis,
  formatFileSize,
  formatUploadDate,
  saveCvAnalysis,
  validateCvFile,
} from '../../services/cvStorage.js'
import { analyzeCvOnAws, uploadCvToAws } from '../../services/cvApi.js'
import './UploadCV.css'

const navItems = [
  { id: 'dashboard', labelKey: 'nav.dashboard', icon: 'dashboard' },
  { id: 'upload-cv', labelKey: 'nav.uploadCv', icon: 'file' },
  { id: 'interview', labelKey: 'nav.aiInterview', icon: 'mic' },
  { id: 'result', labelKey: 'nav.result', icon: 'chart' },
  { id: 'history', labelKey: 'nav.history', icon: 'history' },
]

const fallbackUser = {
  userId: 'user_demo_001',
  fullName: 'Nguyen Huy Dat',
  initials: 'HD',
  role: 'user',
}

function translateFileError(code, t) {
  const map = {
    NO_FILE: t('errors.noFile'),
    INVALID_FILE_TYPE: t('errors.invalidFileType'),
    FILE_TOO_LARGE: t('errors.fileTooLarge'),
  }

  return map[code] ?? code
}

export default function UploadCV({
  cvAnalysis,
  currentUser = fallbackUser,
  onNavigate = () => {},
  onLogout = () => {},
  onUploadComplete = () => {},
}) {
  const { t } = useLanguage()
  const uploadSteps = useMemo(() => [
    { label: t('upload.stepValidate'), description: t('upload.stepValidateDesc') },
    { label: t('upload.stepUpload'), description: t('upload.stepUploadDesc') },
    { label: t('upload.stepAnalyze'), description: t('upload.stepAnalyzeDesc') },
    { label: t('upload.stepSave'), description: t('upload.stepSaveDesc') },
  ], [t])

  const inputRef = useRef(null)
  const [selectedFile, setSelectedFile] = useState(null)
  const [error, setError] = useState('')
  const [isDragging, setIsDragging] = useState(false)
  const [progress, setProgress] = useState(0)
  const [status, setStatus] = useState('idle')
  const [analysis, setAnalysis] = useState(null)

  const isWorking = status === 'uploading' || status === 'analyzing'
  const latestAnalysis = analysis ?? cvAnalysis

  function handleFile(file) {
    const issue = validateCvFile(file)

    if (issue) {
      setSelectedFile(null)
      setAnalysis(null)
      setProgress(0)
      setStatus('idle')
      setError(translateFileError(issue, t))
      return
    }

    setSelectedFile(file)
    setAnalysis(null)
    setError('')
    setProgress(0)
    setStatus('ready')
  }

  async function handleUpload() {
    const issue = validateCvFile(selectedFile)

    if (issue) {
      setError(translateFileError(issue, t))
      return
    }

    setError('')
    setStatus('uploading')
    setProgress(15)

    try {
      await wait(150)
      setProgress(35)

      const uploadedCv = await uploadCvToAws(selectedFile, currentUser.userId)
      setProgress(72)
      setStatus('analyzing')

      const analyzedCv = await analyzeCvOnAws(uploadedCv)
      const result = createDashboardAnalysis(selectedFile, analyzedCv, currentUser.userId)
      saveCvAnalysis(result, currentUser.userId)
      setAnalysis(result)
      setProgress(100)
      setStatus('done')
      onUploadComplete(result)
    } catch (uploadError) {
      setError(uploadError.message || t('errors.uploadFailed'))
      setProgress(0)
      setStatus('ready')
    }
  }

  return (
    <div className="dashboard-page upload-page">
      <div className="dashboard-frame">
        <UploadSidebar currentPage="upload-cv" onNavigate={onNavigate} onLogout={onLogout} t={t} />

        <main className="dashboard-main">
          <header className="topbar">
            <div className="topbar-title">
              <button
                className="icon-button"
                type="button"
                aria-label={t('upload.backToDashboard')}
                title={t('upload.backToDashboard')}
                onClick={() => onNavigate('dashboard')}
              >
                <Icon name="arrowLeft" />
              </button>
              <div>
                <p>{t('upload.pageTitle')}</p>
                <h2>{t('upload.pageSubtitle')}</h2>
              </div>
            </div>

            <div className="topbar-actions">
              <LanguageSwitcher compact />
              <button className="icon-button" type="button" aria-label={t('common.notifications')} title={t('common.notifications')}>
                <Icon name="bell" />
              </button>
              <div className="user-chip" aria-label={t('profile.pageSubtitle')}>
                <span>{currentUser.fullName}</span>
                <small>{currentUser.role === 'admin' ? t('common.admin') : t('common.user')}</small>
                <div className="avatar">{currentUser.initials}</div>
              </div>
            </div>
          </header>

          <div className="dashboard-content upload-content">
            <section className="upload-hero panel">
              <div>
                <p className="eyebrow">{t('upload.eyebrow')}</p>
                <h1>{t('upload.title')}</h1>
                <p>{t('upload.description')}</p>
              </div>
              <button className="primary-action upload-hero-action" type="button" onClick={() => inputRef.current?.click()}>
                <Icon name="upload" />
                {t('upload.chooseCv')}
              </button>
            </section>

            <div className="upload-grid">
              <section className="panel upload-card">
                <div
                  className={`dropzone ${isDragging ? 'dragging' : ''} ${selectedFile ? 'has-file' : ''}`}
                  onDragEnter={(event) => {
                    event.preventDefault()
                    setIsDragging(true)
                  }}
                  onDragOver={(event) => event.preventDefault()}
                  onDragLeave={(event) => {
                    event.preventDefault()
                    setIsDragging(false)
                  }}
                  onDrop={(event) => {
                    event.preventDefault()
                    setIsDragging(false)
                    handleFile(event.dataTransfer.files[0])
                  }}
                >
                  <input
                    ref={inputRef}
                    type="file"
                    accept=".pdf,.doc,.docx,application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    onChange={(event) => handleFile(event.target.files[0])}
                    hidden
                  />

                  <div className="dropzone-icon"><Icon name="upload" /></div>
                  <h3>{selectedFile ? selectedFile.name : t('upload.dropHere')}</h3>
                  <p>
                    {selectedFile
                      ? t('upload.fileSelected', { size: formatFileSize(selectedFile.size) })
                      : t('upload.supportedFormats')}
                  </p>

                  <div className="dropzone-actions">
                    <button className="secondary-upload-action" type="button" onClick={() => inputRef.current?.click()} disabled={isWorking}>
                      {t('upload.browseFile')}
                    </button>
                    <button className="primary-upload-action" type="button" onClick={handleUpload} disabled={!selectedFile || isWorking}>
                      {isWorking ? t('common.processing') : t('upload.uploadAnalyze')}
                    </button>
                  </div>
                </div>

                {error ? <p className="upload-error">{error}</p> : null}

                <div className="upload-progress" aria-label={t('upload.uploadFlow')}>
                  <div className="progress-meta">
                    <span>{getStatusLabel(status, t)}</span>
                    <strong>{progress}%</strong>
                  </div>
                  <div className="progress-track">
                    <div className="progress-fill" style={{ width: `${progress}%` }} />
                  </div>
                </div>
              </section>

              <aside className="panel upload-steps-card">
                <div className="panel-header">
                  <div>
                    <h3>{t('upload.uploadFlow')}</h3>
                    <p>{t('upload.uploadFlowDesc')}</p>
                  </div>
                </div>

                <div className="upload-step-list">
                  {uploadSteps.map((step, index) => (
                    <div className={`upload-step ${getStepState(status, index)}`} key={step.label}>
                      <span>{index + 1}</span>
                      <div>
                        <strong>{step.label}</strong>
                        <p>{step.description}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </aside>
            </div>

            {latestAnalysis ? (
              <section className="panel analysis-preview">
                <div className="panel-header">
                  <div>
                    <h3>{t('upload.analysisResult')}</h3>
                    <p>{t('upload.analysisResultDesc')}</p>
                  </div>
                  <div className="analysis-actions">
                    <button className="secondary-upload-action" type="button" onClick={() => onNavigate('dashboard')}>
                      {t('upload.viewDashboard')}
                    </button>
                    <button className="primary-upload-action" type="button" onClick={() => onNavigate('interview')}>
                      <Icon name="mic" />
                      {t('upload.startAiInterview')}
                    </button>
                  </div>
                </div>

                <div className="analysis-grid">
                  <AnalysisMetric label={t('dashboard.cvScore')} value={`${latestAnalysis.cvScore}/100`} />
                  <AnalysisMetric label={t('upload.suggestedRole')} value={latestAnalysis.suggestedPosition} />
                  <AnalysisMetric label={t('upload.uploaded')} value={formatUploadDate(latestAnalysis.uploadedAt)} />
                  <AnalysisMetric label={t('upload.fileSize')} value={formatFileSize(latestAnalysis.fileSize)} />
                </div>

                <div className="analysis-sections">
                  <ResultBlock title={t('upload.extractedSkills')} items={latestAnalysis.skills} />
                  <ResultBlock title={t('upload.projects')} items={latestAnalysis.projects} />
                  <ResultBlock title={t('upload.experience')} items={latestAnalysis.experience} />
                  <ResultBlock title={t('upload.certificates')} items={latestAnalysis.certificates} />
                </div>

                <InterviewPreparation analysis={latestAnalysis} t={t} />
              </section>
            ) : null}
          </div>
        </main>
      </div>
    </div>
  )
}

function UploadSidebar({ currentPage, onNavigate, onLogout, t }) {
  return (
    <aside className="sidebar" aria-label={t('common.mainMenu')}>
      <div className="brand">
        <div className="brand-mark"><Icon name="brain" /></div>
        <div>
          <strong>Vertex-IntervAI</strong>
          <span>{t('common.brandSubtitleAlt')}</span>
        </div>
      </div>

      <nav className="nav-menu">
        <span className="nav-caption">{t('common.mainMenu')}</span>
        {navItems.map((item) => (
          <button
            className={`nav-item ${currentPage === item.id ? 'active' : ''}`}
            type="button"
            key={item.id}
            onClick={() => onNavigate(item.id)}
          >
            <Icon name={item.icon} />
            <span>{t(item.labelKey)}</span>
          </button>
        ))}

        <span className="nav-caption nav-caption-spaced">{t('common.general')}</span>
        <button
          className={`nav-item ${currentPage === 'profile' ? 'active' : ''}`}
          type="button"
          onClick={() => onNavigate('profile')}
        >
          <Icon name="user" />
          <span>{t('nav.profile')}</span>
        </button>
        <button className="nav-item" type="button">
          <Icon name="settings" />
          <span>{t('nav.settings')}</span>
        </button>
      </nav>

      <button className="logout-button" type="button" onClick={onLogout}>
        <Icon name="logout" />
        {t('common.logOut')}
      </button>
    </aside>
  )
}

function AnalysisMetric({ label, value }) {
  return (
    <div className="analysis-metric">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  )
}

function ResultBlock({ title, items }) {
  return (
    <div className="result-block">
      <h4>{title}</h4>
      <div className="tag-list">
        {items.map((item) => (
          <span key={item}>{item}</span>
        ))}
      </div>
    </div>
  )
}

function InterviewPreparation({ analysis, t }) {
  const skills = analysis.skills?.slice(0, 5) ?? []

  return (
    <section className="interview-prep" aria-label={t('upload.interviewPrep')}>
      <div className="prep-copy">
        <span className="prep-icon"><Icon name="brain" /></span>
        <div>
          <h4>{t('upload.interviewPrep')}</h4>
          <p>{t('upload.interviewPrepDesc')}</p>
        </div>
      </div>

      <div className="prep-grid">
        <PrepItem label={t('upload.suggestedRole')} value={analysis.suggestedPosition} />
        <PrepItem label={t('upload.interviewLevel')} value={getInterviewLevel(analysis.cvScore, t)} />
        <PrepItem label={t('upload.estimatedQuestions')} value={t('upload.questionsCount')} />
        <PrepItem label={t('upload.mainSkills')} value={skills.join(', ') || 'React, Python, AWS'} />
      </div>
    </section>
  )
}

function PrepItem({ label, value }) {
  return (
    <div className="prep-item">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  )
}

function getStatusLabel(status, t) {
  const labels = {
    idle: t('upload.statusIdle'),
    ready: t('upload.statusReady'),
    uploading: t('upload.statusUploading'),
    analyzing: t('upload.statusAnalyzing'),
    done: t('upload.statusDone'),
  }

  return labels[status] ?? labels.idle
}

function getStepState(status, index) {
  if (status === 'done') return 'complete'
  if (status === 'analyzing') return index <= 2 ? 'active' : ''
  if (status === 'uploading') return index <= 1 ? 'active' : ''
  if (status === 'ready') return index === 0 ? 'active' : ''
  return ''
}

function getInterviewLevel(score, t) {
  if (score >= 85) return t('upload.levelStrong')
  if (score >= 70) return t('upload.levelReady')
  return t('upload.levelFoundation')
}

function createDashboardAnalysis(file, uploadedCv, userId) {
  const mockAnalysis = createMockCvAnalysis(file)

  return {
    ...mockAnalysis,
    ...uploadedCv,
    cvId: uploadedCv.cvId || mockAnalysis.cvId,
    userId: uploadedCv.userId || userId,
    fileName: uploadedCv.fileName || mockAnalysis.fileName,
    fileSize: Number(uploadedCv.fileSize || mockAnalysis.fileSize),
    uploadedAt: uploadedCv.createdAt || uploadedCv.uploadedAt || mockAnalysis.uploadedAt,
    status: uploadedCv.status || 'UPLOADED',
    s3Bucket: uploadedCv.s3Bucket,
    s3Key: uploadedCv.s3Key,
  }
}

function wait(ms) {
  return new Promise((resolve) => {
    window.setTimeout(resolve, ms)
  })
}

function Icon({ name }) {
  const paths = {
    dashboard: (
      <>
        <rect x="3" y="3" width="7" height="7" rx="1.5" />
        <rect x="14" y="3" width="7" height="7" rx="1.5" />
        <rect x="3" y="14" width="7" height="7" rx="1.5" />
        <rect x="14" y="14" width="7" height="7" rx="1.5" />
      </>
    ),
    file: <path d="M7 3h7l4 4v14H7zM14 3v5h5M9 13h6M9 17h4" />,
    mic: <path d="M12 3a3 3 0 0 0-3 3v5a3 3 0 0 0 6 0V6a3 3 0 0 0-3-3zM5 11a7 7 0 0 0 14 0M12 18v3M9 21h6" />,
    chart: <path d="M4 19V5M4 19h16M8 16v-5M12 16V8M16 16v-8" />,
    history: <path d="M4 12a8 8 0 1 0 3-6.25M4 5v5h5M12 8v5l3 2" />,
    user: <path d="M20 21a8 8 0 0 0-16 0M12 13a5 5 0 1 0 0-10 5 5 0 0 0 0 10z" />,
    settings: <path d="M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM4 12h2M18 12h2M12 4v2M12 18v2M6.3 6.3l1.4 1.4M16.3 16.3l1.4 1.4M17.7 6.3l-1.4 1.4M7.7 16.3l-1.4 1.4" />,
    bell: <path d="M18 16v-5a6 6 0 0 0-12 0v5l-2 2h16zM10 20a2 2 0 0 0 4 0" />,
    brain: <path d="M9 4a3 3 0 0 0-3 3v1a3 3 0 0 0 0 6v1a3 3 0 0 0 5 2.2M15 4a3 3 0 0 1 3 3v1a3 3 0 0 1 0 6v1a3 3 0 0 1-5 2.2M12 5v14M8 10h3M13 10h3M8 15h3M13 15h3" />,
    upload: <path d="M12 16V4M7 9l5-5 5 5M5 20h14" />,
    logout: <path d="M10 17l5-5-5-5M15 12H3M21 4v16" />,
    arrowLeft: <path d="M15 18l-6-6 6-6" />,
    edit: <path d="M4 20h4l10.5-10.5a2.1 2.1 0 0 0-3-3L5 17v3zM13.5 7.5l3 3" />,
  }

  return (
    <svg className="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      {paths[name]}
    </svg>
  )
}
