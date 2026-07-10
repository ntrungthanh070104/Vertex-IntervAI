import { useEffect, useMemo, useState } from 'react'
import LanguageSwitcher from '../../components/LanguageSwitcher.jsx'
import { useLanguage } from '../../i18n/LanguageContext.jsx'
import { formatFileSize, formatUploadDate } from '../../services/cvStorage.js'
import { getProfileFromAws, saveProfileToAws } from '../../services/profileApi.js'
import '../Dashboard/Dashboard.css'
import './Profile.css'

const PROFILE_STORAGE_KEY = 'talentGraph.profile'

const navItems = [
  { id: 'dashboard', labelKey: 'nav.dashboard', icon: 'dashboard' },
  { id: 'upload-cv', labelKey: 'nav.uploadCv', icon: 'file' },
  { id: 'interview', labelKey: 'nav.aiInterview', icon: 'mic' },
  { id: 'result', labelKey: 'nav.result', icon: 'chart' },
  { id: 'history', labelKey: 'nav.history', icon: 'history' },
]

const defaultProfile = {
  fullName: 'Nguyen Huy Dat',
  headline: 'Frontend Developer Intern',
  email: 'huydat@example.com',
  phone: '+84 901 234 567',
  location: 'Ho Chi Minh City, Vietnam',
  university: 'Software Engineering Student',
  github: 'github.com/huydat123',
  linkedin: 'linkedin.com/in/huydat',
  portfolio: 'vertex-intervai.vercel.app',
  goal: 'Build a strong AI interview platform and prepare for frontend/cloud internship roles.',
}

const fallbackUser = {
  userId: 'user_demo_001',
  fullName: 'Nguyen Huy Dat',
  email: 'user@talentgraph.ai',
  initials: 'HD',
  role: 'user',
}

export default function Profile({
  cvAnalysis,
  currentUser = fallbackUser,
  onNavigate = () => {},
  onLogout = () => {},
}) {
  const { t } = useLanguage()
  const readinessItems = useMemo(() => [
    { label: t('profile.cvUploaded'), value: 92, tone: 'purple' },
    { label: t('profile.profileCompleteness'), value: 86, tone: 'blue' },
    { label: t('profile.interviewReadiness'), value: 78, tone: 'green' },
  ], [t])

  const [profile, setProfile] = useState(() => loadProfile(currentUser))
  const [isEditing, setIsEditing] = useState(false)
  const [saved, setSaved] = useState(false)
  const [syncStatus, setSyncStatus] = useState(t('profile.syncLocal'))
  const analysis = cvAnalysis ?? null

  useEffect(() => {
    let isMounted = true

    async function loadAwsProfile() {
      try {
        const awsProfile = await getProfileFromAws(currentUser.userId)

        if (!isMounted) return

        setProfile((current) => ({ ...current, ...awsProfile }))
        setSyncStatus(t('profile.syncAws'))
      } catch {
        if (isMounted) {
          setSyncStatus(t('profile.syncSavedLocal'))
        }
      }
    }

    loadAwsProfile()

    return () => {
      isMounted = false
    }
  }, [currentUser.userId, t])

  const topSkills = useMemo(() => {
    const fromAnalysis = analysis?.skills?.slice(0, 8)
    return fromAnalysis?.length ? fromAnalysis : ['React', 'JavaScript', 'Python', 'AWS Lambda', 'DynamoDB', 'REST API']
  }, [analysis])

  function updateField(field, value) {
    setProfile((current) => ({ ...current, [field]: value }))
    setSaved(false)
  }

  async function handleSave() {
    window.localStorage.setItem(getProfileStorageKey(currentUser.userId), JSON.stringify(profile))

    try {
      const savedProfile = await saveProfileToAws(profile, currentUser.userId)
      setProfile((current) => ({ ...current, ...savedProfile }))
      setSyncStatus(t('profile.syncSavedAws'))
    } catch {
      setSyncStatus(t('profile.syncSavedLocal'))
    } finally {
      setIsEditing(false)
      setSaved(true)
    }
  }

  return (
    <div className="dashboard-page profile-page">
      <div className="dashboard-frame">
        <ProfileSidebar currentPage="profile" onNavigate={onNavigate} onLogout={onLogout} t={t} />

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
                <p>{t('profile.pageTitle')}</p>
                <h2>{t('profile.pageSubtitle')}</h2>
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

          <div className="dashboard-content profile-content">
            <section className="profile-hero panel">
              <div className="profile-identity">
                <div className="profile-avatar">{currentUser.initials}</div>
                <div>
                  <p className="eyebrow">{t('profile.candidateIdentity')}</p>
                  <h1>{profile.fullName}</h1>
                  <span>{profile.headline}</span>
                </div>
              </div>

              <div className="profile-actions">
                {saved ? <span className="save-status">{t('profile.saved')}</span> : null}
                <span className="sync-status">{syncStatus}</span>
                <button className="secondary-upload-action" type="button" onClick={() => setIsEditing((value) => !value)}>
                  <Icon name="edit" />
                  {isEditing ? t('common.cancel') : t('profile.editProfile')}
                </button>
                <button className="primary-upload-action" type="button" onClick={handleSave}>
                  <Icon name="save" />
                  {t('common.save')}
                </button>
              </div>
            </section>

            <section className="profile-grid">
              <div className="panel profile-form-panel">
                <PanelHeader title={t('profile.personalInfo')} description={t('profile.personalInfoDesc')} />
                <div className="profile-form-grid">
                  <ProfileField label={t('profile.fullName')} value={profile.fullName} editing={isEditing} onChange={(value) => updateField('fullName', value)} />
                  <ProfileField label={t('profile.headline')} value={profile.headline} editing={isEditing} onChange={(value) => updateField('headline', value)} />
                  <ProfileField label={t('common.email')} value={profile.email} editing={isEditing} onChange={(value) => updateField('email', value)} />
                  <ProfileField label={t('profile.phone')} value={profile.phone} editing={isEditing} onChange={(value) => updateField('phone', value)} />
                  <ProfileField label={t('profile.location')} value={profile.location} editing={isEditing} onChange={(value) => updateField('location', value)} />
                  <ProfileField label={t('profile.education')} value={profile.university} editing={isEditing} onChange={(value) => updateField('university', value)} />
                </div>
              </div>

              <aside className="panel readiness-panel">
                <PanelHeader title={t('profile.readiness')} description={t('profile.readinessDesc')} />
                <div className="readiness-list">
                  {readinessItems.map((item) => (
                    <ReadinessBar key={item.label} {...item} />
                  ))}
                </div>
              </aside>

              <div className="panel profile-goal-panel">
                <PanelHeader title={t('profile.careerGoal')} description={t('profile.careerGoalDesc')} />
                {isEditing ? (
                  <textarea
                    className="profile-textarea"
                    value={profile.goal}
                    onChange={(event) => updateField('goal', event.target.value)}
                    rows="5"
                  />
                ) : (
                  <p>{profile.goal}</p>
                )}
              </div>

              <aside className="panel cv-summary-panel">
                <PanelHeader title={t('profile.latestCv')} description={analysis ? t('profile.latestCvConnected') : t('profile.latestCvEmpty')} />
                <div className="profile-cv-card">
                  <div className="file-icon"><Icon name="file" /></div>
                  <div>
                    <strong>{analysis?.fileName ?? t('profile.noCvYet')}</strong>
                    <span>
                      {analysis
                        ? `${formatUploadDate(analysis.uploadedAt)} / ${formatFileSize(analysis.fileSize)}`
                        : t('profile.uploadToUnlock')}
                    </span>
                  </div>
                </div>
                <div className="profile-score">
                  <strong>{analysis?.cvScore ?? 0}</strong>
                  <span>{t('profile.cvScore')}</span>
                </div>
              </aside>

              <div className="panel skills-panel">
                <PanelHeader title={t('profile.technicalSkills')} description={t('profile.technicalSkillsDesc')} />
                <div className="tag-list profile-tags">
                  {topSkills.map((skill) => (
                    <span key={skill}>{skill}</span>
                  ))}
                </div>
              </div>

              <aside className="panel links-panel">
                <PanelHeader title={t('profile.candidateLinks')} description={t('profile.candidateLinksDesc')} />
                <div className="link-list">
                  <LinkField icon="github" label={t('profile.github')} value={profile.github} editing={isEditing} onChange={(value) => updateField('github', value)} />
                  <LinkField icon="linkedin" label={t('profile.linkedin')} value={profile.linkedin} editing={isEditing} onChange={(value) => updateField('linkedin', value)} />
                  <LinkField icon="globe" label={t('profile.portfolio')} value={profile.portfolio} editing={isEditing} onChange={(value) => updateField('portfolio', value)} />
                </div>
              </aside>
            </section>
          </div>
        </main>
      </div>
    </div>
  )
}

function getProfileStorageKey(userId) {
  return `${PROFILE_STORAGE_KEY}.${userId}`
}

function loadProfile(currentUser) {
  try {
    const stored = window.localStorage.getItem(getProfileStorageKey(currentUser.userId))
    const baseProfile = {
      ...defaultProfile,
      fullName: currentUser.fullName,
      email: currentUser.email,
    }

    return stored ? { ...baseProfile, ...JSON.parse(stored) } : baseProfile
  } catch {
    return {
      ...defaultProfile,
      fullName: currentUser.fullName,
      email: currentUser.email,
    }
  }
}

function ProfileSidebar({ currentPage, onNavigate, onLogout, t }) {
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
        <button className="nav-item active" type="button" onClick={() => onNavigate('profile')}>
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

function ProfileField({ label, value, editing, onChange }) {
  return (
    <label className="profile-field">
      <span>{label}</span>
      {editing ? (
        <input value={value} onChange={(event) => onChange(event.target.value)} />
      ) : (
        <strong>{value}</strong>
      )}
    </label>
  )
}

function LinkField({ icon, label, value, editing, onChange }) {
  return (
    <label className="link-field">
      <span className="link-icon"><Icon name={icon} /></span>
      <div>
        <small>{label}</small>
        {editing ? (
          <input value={value} onChange={(event) => onChange(event.target.value)} />
        ) : (
          <strong>{value}</strong>
        )}
      </div>
    </label>
  )
}

function ReadinessBar({ label, value, tone }) {
  return (
    <div className="readiness-row">
      <div>
        <strong>{label}</strong>
        <span>{value}%</span>
      </div>
      <div className="skill-track">
        <div className={`skill-fill ${tone}`} style={{ width: `${value}%` }} />
      </div>
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
    edit: <path d="M4 20h4l10.5-10.5a2.1 2.1 0 0 0-3-3L5 17v3zM13.5 7.5l3 3" />,
    save: <path d="M5 4h12l2 2v14H5zM8 4v6h8M8 20v-6h8" />,
    github: <path d="M9 19c-4 1.2-4-2-5.5-2.5M15 22v-3.5c0-1 .3-1.7.8-2.2 2.7-.3 5.2-1.3 5.2-6A4.7 4.7 0 0 0 19.7 7c.1-.3.6-1.7-.1-3.5 0 0-1.1-.3-3.6 1.3a12.6 12.6 0 0 0-6.5 0C7 3.2 5.9 3.5 5.9 3.5 5.2 5.3 5.7 6.7 5.8 7A4.7 4.7 0 0 0 4.5 10.3c0 4.6 2.5 5.6 5.2 6 .4.4.7 1 .8 1.9V22" />,
    linkedin: <path d="M4 9h4v11H4zM6 5.5a2 2 0 1 0 0 .1M11 9h4v1.8A4 4 0 0 1 22 13v7h-4v-6a2 2 0 0 0-4 0v6h-4z" />,
    globe: <path d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM3.6 9h16.8M3.6 15h16.8M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18" />,
    logout: <path d="M10 17l5-5-5-5M15 12H3M21 4v16" />,
    arrowLeft: <path d="M15 18l-6-6 6-6" />,
  }

  return (
    <svg className="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      {paths[name]}
    </svg>
  )
}
