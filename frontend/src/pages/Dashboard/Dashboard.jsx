import LanguageSwitcher from '../../components/LanguageSwitcher.jsx'
import { useLanguage } from '../../i18n/LanguageContext.jsx'
import { formatFileSize, formatUploadDate } from '../../services/cvStorage.js'
import { formatInterviewDate, loadInterviewHistory } from '../../services/interviewStorage.js'
import { getPreferredInterviewRole } from '../../services/userPreferences.js'
import './Dashboard.css'

const navItems = [
  { id: 'dashboard', labelKey: 'nav.dashboard', icon: 'dashboard' },
  { id: 'upload-cv', labelKey: 'nav.uploadCv', icon: 'file' },
  { id: 'interview', labelKey: 'nav.aiInterview', icon: 'mic' },
  { id: 'result', labelKey: 'nav.result', icon: 'chart' },
  { id: 'history', labelKey: 'nav.history', icon: 'history' },
  { id: 'profile', labelKey: 'nav.profile', icon: 'user' },
  { id: 'settings', labelKey: 'nav.settings', icon: 'settings' },
]

function buildFallbackCvAnalysis(t) {
  return {
    fileName: 'Nguyen-Huy-Dat-CV.pdf',
    fileSize: 428000,
    uploadedAt: '2026-07-03T00:00:00.000Z',
    cvScore: 92,
    suggestedPosition: t('dashboard.fallbackRole'),
    recommendation: t('dashboard.fallbackRecommendation'),
    skills: ['React', 'Python', 'AWS Lambda', 'DynamoDB'],
    talentScores: [
      { label: 'React', score: 88 },
      { label: 'Python', score: 76 },
      { label: 'AWS', score: 72 },
      { label: 'Database', score: 68 },
      { label: 'Communication', score: 82 },
      { label: 'Problem Solving', score: 79 },
    ],
    skillGroups: [
      { label: t('dashboard.fallbackSkillFrontend'), value: 88, skills: 'React, Vite, Tailwind', tone: 'purple' },
      { label: t('dashboard.fallbackSkillBackend'), value: 76, skills: 'Python, Lambda APIs', tone: 'blue' },
      { label: t('dashboard.fallbackSkillCloud'), value: 72, skills: 'S3, Bedrock, DynamoDB', tone: 'orange' },
      { label: t('dashboard.fallbackSkillCommunication'), value: 82, skills: 'Clear answers, steady flow', tone: 'green' },
    ],
  }
}

function buildFallbackInterviews(t) {
  return [
    { role: t('dashboard.fallbackInterviewFrontend'), date: 'Jul 03, 2026', score: 78, status: 'Completed' },
    { role: t('dashboard.fallbackInterviewBackend'), date: 'Jun 28, 2026', score: 84, status: 'Completed' },
    { role: t('dashboard.fallbackInterviewCloud'), date: 'Jun 21, 2026', score: 73, status: 'Review' },
  ]
}

const actions = [
  { labelKey: 'dashboard.uploadCv', icon: 'upload', tone: 'purple', page: 'upload-cv' },
  { labelKey: 'dashboard.startInterview', icon: 'play', tone: 'green', page: 'interview' },
  { labelKey: 'dashboard.viewResult', icon: 'chart', tone: 'blue', page: 'result' },
]

const fallbackUser = {
  fullName: 'Nguyen Huy Dat',
  initials: 'HD',
  role: 'user',
}

function translateStatus(status, t) {
  const map = {
    Completed: t('status.completed'),
    Review: t('status.review'),
  }

  return map[status] ?? status
}

export default function Dashboard({
  cvAnalysis,
  interviewResult,
  currentUser = fallbackUser,
  onNavigate = () => {},
  onLogout = () => {},
}) {
  const { t } = useLanguage()
  const hasUploadedCv = Boolean(cvAnalysis)
  const analysis = cvAnalysis ?? buildFallbackCvAnalysis(t)
  const roleLabel = analysis?.suggestedPosition || getPreferredInterviewRole(currentUser?.userId, t('dashboard.fallbackRole'))
  const latestInterviewScore = interviewResult?.overallScore ?? 0
  const averageScore = interviewResult && analysis?.cvScore
    ? Math.round((analysis.cvScore + latestInterviewScore) / 2)
    : (analysis?.cvScore ? Math.round(analysis.cvScore * 0.9) : 81)
  const historyRows = loadInterviewHistory(currentUser?.userId)
  const interviewRows = historyRows.length
    ? historyRows.slice(0, 3).map((item) => ({
      role: item.role,
      date: formatInterviewDate(item.completedAt),
      score: item.overallScore,
      status: item.status,
    }))
    : (interviewResult
      ? [{
        role: interviewResult.role,
        date: formatInterviewDate(interviewResult.completedAt),
        score: interviewResult.overallScore,
        status: interviewResult.status,
      }]
      : buildFallbackInterviews(t))
  const firstName = currentUser.fullName?.split(' ')[0] ?? t('dashboard.candidate')
  const stats = [
    { label: t('dashboard.cvScore'), value: String(analysis.cvScore), suffix: '/100', icon: 'file', tone: 'purple' },
    { label: t('dashboard.latestInterview'), value: String(latestInterviewScore), suffix: '/100', icon: 'mic', tone: 'green' },
    { label: t('dashboard.completedInterviews'), value: interviewResult ? '1' : '12', suffix: '', icon: 'check', tone: 'orange' },
    { label: t('dashboard.averageScore'), value: String(averageScore), suffix: '/100', icon: 'chart', tone: 'blue' },
  ]

  return (
    <div className="dashboard-page">
      <div className="dashboard-frame">
        <Sidebar currentPage="dashboard" onNavigate={onNavigate} onLogout={onLogout} t={t} />

        <main className="dashboard-main">
          <Topbar currentUser={currentUser} t={t} />

          <div className="dashboard-content">
            <section className="hero-panel" aria-label={t('dashboard.pageTitle')}>
              <div className="hero-copy">
                <p className="eyebrow">{t('dashboard.eyebrow')}</p>
                <h1>{t('dashboard.welcome', { name: firstName })}</h1>
                <p>{hasUploadedCv ? `${t('dashboard.hasCv')} • ${roleLabel}` : t('dashboard.noCv')}</p>
                <div className="hero-actions">
                  <button className="primary-action" type="button" onClick={() => onNavigate('interview')}>
                    <Icon name="play" />
                    {t('dashboard.startInterview')}
                  </button>
                  <button className="secondary-action" type="button" onClick={() => onNavigate('upload-cv')}>
                    <Icon name="upload" />
                    {t('dashboard.uploadNewCv')}
                  </button>
                </div>
              </div>

              <div className="workflow-strip" aria-label={t('dashboard.pageSubtitle')}>
                <WorkflowStep icon="file" label={t('dashboard.cvParsed')} status={hasUploadedCv ? t('status.done') : t('status.demo')} active />
                <WorkflowStep icon="brain" label={t('dashboard.questions')} status={t('status.ready')} active={hasUploadedCv} />
                <WorkflowStep icon="mic" label={t('dashboard.voiceRound')} status={interviewResult ? t('status.done') : t('status.next')} active={Boolean(interviewResult)} />
                <WorkflowStep icon="chart" label={t('dashboard.talentGraph')} status={interviewResult ? t('status.updated') : t('status.after')} active={Boolean(interviewResult)} />
              </div>
            </section>

            <section className="stats-grid" aria-label={t('dashboard.pageTitle')}>
              {stats.map((stat) => (
                <StatCard key={stat.label} {...stat} />
              ))}
            </section>

            <div className="dashboard-grid">
              <section className="panel talent-panel">
                <PanelHeader
                  title={t('dashboard.talentGraphTitle')}
                  description={t('dashboard.talentGraphDesc')}
                />
                <div className="talent-layout">
                  <RadarChart data={analysis.talentScores} title={t('dashboard.radarTitle')} />
                  <div className="skill-breakdown">
                    {analysis.skillGroups.map((group) => (
                      <SkillBar key={group.label} {...group} />
                    ))}
                  </div>
                </div>
              </section>

              <aside className="right-rail">
                <section className="panel score-panel">
                  <PanelHeader title={t('dashboard.assessmentScore')} description={t('dashboard.assessmentScoreDesc')} />
                  <div className="score-rings">
                    <ScoreRing label={t('dashboard.cvScore')} value={analysis.cvScore} color="#7c3aed" />
                    <ScoreRing label={t('dashboard.interviewLabel')} value={latestInterviewScore} color="#10b981" />
                  </div>
                </section>

                <section className="panel cv-panel">
                  <PanelHeader
                    title={t('dashboard.cvStatus')}
                    description={hasUploadedCv ? t('dashboard.cvStatusUploaded') : t('dashboard.cvStatusDemo')}
                  />
                  <div className="cv-file">
                    <div className="file-icon"><Icon name="file" /></div>
                    <div>
                      <strong>{analysis.fileName}</strong>
                      <span>
                        {formatUploadDate(analysis.uploadedAt)} / {formatFileSize(analysis.fileSize)}
                      </span>
                    </div>
                  </div>
                  <div className="tag-list" aria-label={t('upload.extractedSkills')}>
                    {analysis.skills.slice(0, 6).map((skill) => (
                      <span key={skill}>{skill}</span>
                    ))}
                  </div>
                </section>
              </aside>

              <section className="panel recommendation-panel">
                <PanelHeader title={t('dashboard.aiRecommendation')} description={t('dashboard.aiRecommendationDesc')} />
                <p>{analysis.recommendation}</p>
                <p className="role-hint">{t('upload.suggestedRole')}: {roleLabel}</p>
                <div className="focus-list">
                  <span>{t('dashboard.focusLambda')}</span>
                  <span>{t('dashboard.focusDynamo')}</span>
                  <span>{t('dashboard.focusBehavioral')}</span>
                </div>
              </section>

              <section className="panel history-panel">
                <PanelHeader title={t('dashboard.recentInterviews')} description={t('dashboard.recentInterviewsDesc')} />
                <div className="interview-table" role="table" aria-label={t('dashboard.recentInterviews')}>
                  <div className="table-row table-head" role="row">
                    <span role="columnheader">{t('dashboard.position')}</span>
                    <span role="columnheader">{t('dashboard.date')}</span>
                    <span role="columnheader">{t('dashboard.scoreCol')}</span>
                    <span role="columnheader">{t('dashboard.status')}</span>
                  </div>
                  {interviewRows.map((interview) => (
                    <div className="table-row" role="row" key={`${interview.role}-${interview.date}`}>
                      <span role="cell">{interview.role}</span>
                      <span role="cell">{interview.date}</span>
                      <span role="cell">{interview.score}/100</span>
                      <span role="cell">
                        <span className={`status-pill ${interview.status.toLowerCase()}`}>
                          {translateStatus(interview.status, t)}
                        </span>
                      </span>
                    </div>
                  ))}
                </div>
              </section>

              <section className="panel quick-panel">
                <PanelHeader title={t('dashboard.quickActions')} description={t('dashboard.quickActionsDesc')} />
                <div className="action-list">
                  {actions.map((action) => (
                    <button
                      className={`action-button ${action.tone}`}
                      type="button"
                      key={action.labelKey}
                      onClick={() => onNavigate(action.page)}
                    >
                      <Icon name={action.icon} />
                      <span>{t(action.labelKey)}</span>
                    </button>
                  ))}
                </div>
              </section>
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}

function Sidebar({ currentPage, onNavigate, onLogout, t }) {
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
        {navItems.slice(0, 5).map((item) => (
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
        {navItems.slice(5).map((item) => (
          <button
            className="nav-item"
            type="button"
            key={item.id}
            onClick={() => onNavigate(item.id)}
          >
            <Icon name={item.icon} />
            <span>{t(item.labelKey)}</span>
          </button>
        ))}
      </nav>

      <button className="logout-button" type="button" onClick={onLogout}>
        <Icon name="logout" />
        {t('common.logOut')}
      </button>
    </aside>
  )
}

function Topbar({ currentUser, t }) {
  return (
    <header className="topbar">
      <div className="topbar-title">
        <button className="icon-button" type="button" aria-label={t('common.goBack')} title={t('common.goBack')}>
          <Icon name="arrowLeft" />
        </button>
        <div>
          <p>{t('dashboard.pageTitle')}</p>
          <h2>{t('dashboard.pageSubtitle')}</h2>
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
  )
}

function WorkflowStep({ icon, label, status, active = false }) {
  return (
    <div className={`workflow-step ${active ? 'active' : ''}`}>
      <span className="workflow-icon"><Icon name={icon} /></span>
      <strong>{label}</strong>
      <small>{status}</small>
    </div>
  )
}

function StatCard({ label, value, suffix, icon, tone }) {
  return (
    <article className={`stat-card ${tone}`}>
      <div className="stat-icon"><Icon name={icon} /></div>
      <div>
        <span>{label}</span>
        <strong>{value}<small>{suffix}</small></strong>
      </div>
    </article>
  )
}

function PanelHeader({ title, description }) {
  return (
    <div className="panel-header">
      <div>
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  )
}

function SkillBar({ label, value, skills, tone }) {
  return (
    <div className="skill-row">
      <div className="skill-meta">
        <strong>{label}</strong>
        <span>{skills}</span>
      </div>
      <div className="skill-score">
        <span>{value}%</span>
        <div className="skill-track">
          <div className={`skill-fill ${tone}`} style={{ width: `${value}%` }} />
        </div>
      </div>
    </div>
  )
}

function ScoreRing({ label, value, color }) {
  return (
    <div className="score-ring-item">
      <div
        className="score-ring"
        style={{ '--score': `${value}%`, '--ring-color': color }}
        aria-label={`${label} ${value}/100`}
      >
        <strong>{value}%</strong>
      </div>
      <span>{label}</span>
    </div>
  )
}

function RadarChart({ data, title }) {
  const center = 120
  const radius = 76
  const angleStep = (Math.PI * 2) / data.length

  const pointFor = (index, scale) => {
    const angle = angleStep * index - Math.PI / 2
    return {
      x: center + Math.cos(angle) * radius * scale,
      y: center + Math.sin(angle) * radius * scale,
    }
  }

  const polygonPoints = data
    .map((item, index) => {
      const point = pointFor(index, item.score / 100)
      return `${point.x},${point.y}`
    })
    .join(' ')

  const gridPolygons = [0.25, 0.5, 0.75, 1].map((scale) =>
    data
      .map((_, index) => {
        const point = pointFor(index, scale)
        return `${point.x},${point.y}`
      })
      .join(' '),
  )

  return (
    <div className="radar-wrap" aria-label={title}>
      <svg viewBox="0 0 240 240" role="img">
        <title>{title}</title>
        {gridPolygons.map((points) => (
          <polygon className="radar-grid" points={points} key={points} />
        ))}
        {data.map((item, index) => {
          const axisPoint = pointFor(index, 1)
          const labelPoint = pointFor(index, 1.28)
          return (
            <g key={item.label}>
              <line className="radar-axis" x1={center} y1={center} x2={axisPoint.x} y2={axisPoint.y} />
              <text className="radar-label" x={labelPoint.x} y={labelPoint.y} textAnchor="middle">
                {item.label}
              </text>
            </g>
          )
        })}
        <polygon className="radar-shape" points={polygonPoints} />
        {data.map((item, index) => {
          const point = pointFor(index, item.score / 100)
          return <circle className="radar-dot" cx={point.x} cy={point.y} r="3.5" key={`${item.label}-dot`} />
        })}
      </svg>
    </div>
  )
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
    check: <path d="M20 6 9 17l-5-5" />,
    upload: <path d="M12 16V4M7 9l5-5 5 5M5 20h14" />,
    play: <path d="M8 5v14l11-7z" />,
    logout: <path d="M10 17l5-5-5-5M15 12H3M21 4v16" />,
    arrowLeft: <path d="M15 18l-6-6 6-6" />,
  }

  return (
    <svg className="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      {paths[name]}
    </svg>
  )
}
