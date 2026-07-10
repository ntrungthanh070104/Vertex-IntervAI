import { useLanguage } from '../i18n/LanguageContext.jsx'
import './LanguageSwitcher.css'

export default function LanguageSwitcher({ compact = false }) {
  const { locale, setLocale, t } = useLanguage()

  return (
    <div
      className={`language-switcher ${compact ? 'compact' : ''}`}
      role="group"
      aria-label={t('common.language')}
    >
      <button
        type="button"
        className={locale === 'vi' ? 'active' : ''}
        onClick={() => setLocale('vi')}
        aria-pressed={locale === 'vi'}
      >
        VI
      </button>
      <button
        type="button"
        className={locale === 'en' ? 'active' : ''}
        onClick={() => setLocale('en')}
        aria-pressed={locale === 'en'}
      >
        EN
      </button>
    </div>
  )
}
