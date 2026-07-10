import LanguageSwitcher from '../../components/LanguageSwitcher.jsx'
import { useLanguage } from '../../i18n/LanguageContext.jsx'
import './LandingPage.css'

export default function LandingPage({ onStartAuth = () => {} }) {
  const { t } = useLanguage()

  return (
    <div className="landing-page">
      <header className="landing-header">
        <div className="brand-block">
          <div className="brand-mark">AI</div>
          <div>
            <strong>Vertex-IntervAI</strong>
            <span>{t('landing.tagline')}</span>
          </div>
        </div>

        <div className="landing-actions">
          <LanguageSwitcher compact />
          <button className="secondary-landing-button" type="button" onClick={() => onStartAuth('login')}>
            {t('landing.signIn')}
          </button>
        </div>
      </header>

      <main className="landing-main">
        <section className="hero-panel">
          <div className="hero-copy">
            <p className="eyebrow">{t('landing.eyebrow')}</p>
            <h1>{t('landing.title')}</h1>
            <p className="hero-description">{t('landing.description')}</p>
            <div className="hero-actions">
              <button className="primary-landing-button" type="button" onClick={() => onStartAuth('login')}>
                {t('landing.startNow')}
              </button>
              <button className="ghost-landing-button" type="button" onClick={() => onStartAuth('login')}>
                {t('landing.exploreFeatures')}
              </button>
            </div>
            <div className="hero-stats">
              <div>
                <strong>4.9/5</strong>
                <span>{t('landing.statRating')}</span>
              </div>
              <div>
                <strong>24/7</strong>
                <span>{t('landing.statSupport')}</span>
              </div>
              <div>
                <strong>AI</strong>
                <span>{t('landing.statAi')}</span>
              </div>
            </div>
          </div>

          <div className="hero-card">
            <div className="hero-card-glow" />
            <h3>{t('landing.heroCardTitle')}</h3>
            <ul>
              <li>{t('landing.heroPoint1')}</li>
              <li>{t('landing.heroPoint2')}</li>
              <li>{t('landing.heroPoint3')}</li>
            </ul>
          </div>
        </section>

        <section className="feature-grid">
          <article className="feature-card">
            <div className="feature-icon">✦</div>
            <h3>{t('landing.featureInterviewTitle')}</h3>
            <p>{t('landing.featureInterviewDesc')}</p>
          </article>
          <article className="feature-card">
            <div className="feature-icon">⬢</div>
            <h3>{t('landing.featureCvTitle')}</h3>
            <p>{t('landing.featureCvDesc')}</p>
          </article>
          <article className="feature-card">
            <div className="feature-icon">◌</div>
            <h3>{t('landing.featureInsightTitle')}</h3>
            <p>{t('landing.featureInsightDesc')}</p>
          </article>
        </section>

        <section className="about-panel">
          <div>
            <p className="eyebrow">{t('landing.aboutEyebrow')}</p>
            <h2>{t('landing.aboutTitle')}</h2>
            <p>{t('landing.aboutDescription')}</p>
          </div>
          <div className="about-points">
            <div>{t('landing.aboutPoint1')}</div>
            <div>{t('landing.aboutPoint2')}</div>
            <div>{t('landing.aboutPoint3')}</div>
          </div>
        </section>
      </main>

      <footer className="landing-footer">
        <span>© 2026 Vertex-IntervAI</span>
        <div>
          <a href="#">Privacy</a>
          <a href="#">Terms</a>
          <a href="#">Contact</a>
        </div>
      </footer>
    </div>
  )
}
