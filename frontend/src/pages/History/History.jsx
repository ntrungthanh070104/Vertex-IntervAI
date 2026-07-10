import LanguageSwitcher from '../../components/LanguageSwitcher.jsx'
import { useLanguage } from '../../i18n/LanguageContext.jsx'
import { formatInterviewDate, loadInterviewHistory } from '../../services/interviewStorage.js'
import './History.css'

export default function History({ currentUser, onNavigate, onLogout }) {
  const { t } = useLanguage()
  const history = loadInterviewHistory(currentUser?.userId)

  return (
    <div className="page-shell">
      <div className="page-card">
        <header className="page-header">
          <div>
            <p className="page-kicker">{t('history.pageSubtitle')}</p>
            <h1>{t('history.pageTitle')}</h1>
          </div>
          <div className="page-header-actions">
            <LanguageSwitcher compact />
            <button className="secondary-link" type="button" onClick={() => onNavigate('dashboard')}>
              {t('result.backToDashboard')}
            </button>
          </div>
        </header>

        {!history.length ? (
          <section className="empty-state">
            <h2>{t('history.empty')}</h2>
            <button className="primary-action" type="button" onClick={() => onNavigate('interview')}>
              {t('dashboard.startInterview')}
            </button>
          </section>
        ) : (
          <div className="history-list">
            {history.map((item) => (
              <article className="history-item" key={item.interviewId || item.completedAt}>
                <div>
                  <h3>{item.role}</h3>
                  <p>{t('history.role')}: {item.role}</p>
                  <p>{t('history.date')}: {formatInterviewDate(item.completedAt)}</p>
                </div>
                <div className="history-meta">
                  <span className="score-badge">{item.overallScore}/100</span>
                  <span className="status-badge">{item.status}</span>
                  <button className="secondary-action" type="button" onClick={() => {
                    onNavigate('result')
                  }}>
                    {t('dashboard.viewResult')}
                  </button>
                </div>
              </article>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
