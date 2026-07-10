import LanguageSwitcher from '../../components/LanguageSwitcher.jsx'
import { useLanguage } from '../../i18n/LanguageContext.jsx'
import { formatInterviewDate, loadInterviewResult } from '../../services/interviewStorage.js'
import './Result.css'

export default function Result({ interviewResult, currentUser, onNavigate, onLogout }) {
  const { t } = useLanguage()
  const resolvedResult = interviewResult ?? loadInterviewResult(currentUser?.userId)

  return (
    <div className="page-shell">
      <div className="page-card">
        <header className="page-header">
          <div>
            <p className="page-kicker">{t('result.pageSubtitle')}</p>
            <h1>{t('result.pageTitle')}</h1>
          </div>
          <div className="page-header-actions">
            <LanguageSwitcher compact />
            <button className="secondary-link" type="button" onClick={() => onNavigate('dashboard')}>
              {t('result.backToDashboard')}
            </button>
          </div>
        </header>

        {!resolvedResult ? (
          <section className="empty-state">
            <h2>{t('result.empty')}</h2>
            <div className="empty-actions">
              <button className="primary-action" type="button" onClick={() => onNavigate('interview')}>
                {t('dashboard.startInterview')}
              </button>
              <button className="secondary-action" type="button" onClick={() => onNavigate('history')}>
                {t('history.pageTitle')}
              </button>
            </div>
          </section>
        ) : (
          <div className="result-grid">
            <section className="panel result-summary">
              <div className="score-pill">{resolvedResult.overallScore}/100</div>
              <h2>{t('result.latestResult')}</h2>
              <p>{resolvedResult.role}</p>
              <div className="meta-list">
                <span>{t('result.role')}: {resolvedResult.role}</span>
                <span>{t('result.completedAt')}: {formatInterviewDate(resolvedResult.completedAt)}</span>
                <span>{t('dashboard.candidate')}: {currentUser?.fullName ?? 'Guest'}</span>
              </div>
            </section>

            <section className="panel result-detail">
              <h3>{t('result.strengths')}</h3>
              <ul>
                {resolvedResult.strengths?.map((item) => <li key={item}>{item}</li>)}
              </ul>
            </section>

            <section className="panel result-detail">
              <h3>{t('result.improvements')}</h3>
              <ul>
                {resolvedResult.improvements?.map((item) => <li key={item}>{item}</li>)}
              </ul>
            </section>

            <section className="panel recommendation-panel">
              <h3>{t('result.recommendation')}</h3>
              <p>{resolvedResult.recommendation}</p>
            </section>
          </div>
        )}
      </div>
    </div>
  )
}
