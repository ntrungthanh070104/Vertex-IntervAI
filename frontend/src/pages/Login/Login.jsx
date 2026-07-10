import { useState } from 'react'
import LanguageSwitcher from '../../components/LanguageSwitcher.jsx'
import { useLanguage } from '../../i18n/LanguageContext.jsx'
import { demoAccounts, loginWithDemoAccount, registerUser } from '../../services/authService.js'
import './Login.css'

export default function Login({ onLogin = () => {} }) {
  const { t } = useLanguage()
  const [mode, setMode] = useState('login')
  const [fullName, setFullName] = useState('')
  const [email, setEmail] = useState(demoAccounts[0].email)
  const [password, setPassword] = useState(demoAccounts[0].password)
  const [confirmPassword, setConfirmPassword] = useState('')
  const [error, setError] = useState('')
  const [success, setSuccess] = useState('')
  const selectedAccount = demoAccounts.find((account) => account.email === email) ?? demoAccounts[0]

  function handleSubmit(event) {
    event.preventDefault()
    setError('')
    setSuccess('')

    if (mode === 'register') {
      if (!fullName.trim()) {
        setError(t('errors.fullNameRequired'))
        return
      }

      if (password !== confirmPassword) {
        setError(t('errors.passwordMismatch'))
        return
      }

      try {
        const user = registerUser({ fullName, email, password })
        setSuccess(t('login.accountCreated'))
        onLogin(user)
      } catch (loginError) {
        if (loginError.code === 'EMAIL_EXISTS') {
          setError(t('errors.emailExists'))
        } else if (loginError.code === 'MISSING_FIELDS') {
          setError(t('errors.missingFields'))
        } else {
          setError(loginError.message)
        }
      }

      return
    }

    try {
      const user = loginWithDemoAccount(email, password)
      onLogin(user)
    } catch (loginError) {
      if (loginError.code === 'INVALID_CREDENTIALS') {
        setError(t('errors.invalidCredentials'))
      } else {
        setError(loginError.message)
      }
    }
  }

  function fillAccount(account) {
    setEmail(account.email)
    setPassword(account.password)
    setConfirmPassword(account.password)
    setMode('login')
    setError('')
    setSuccess('')
  }

  return (
    <main className="login-page">
      <section className="login-shell">
        <LanguageSwitcher compact />

        <div className="login-brand-panel">
          <div className="login-brand">
            <div className="login-mark"><Icon name="brain" /></div>
            <div>
              <strong>Vertex-IntervAI</strong>
              <span>{t('common.brandSubtitle')}</span>
            </div>
          </div>

          <div className="login-copy">
            <p className="login-eyebrow">{t('login.secureWorkspace')}</p>
            <h1>{t('login.title')}</h1>
            <p>{t('login.subtitle')}</p>
          </div>

          <div className="role-preview">
            <span className={`role-badge ${selectedAccount.role}`}>{selectedAccount.role}</span>
            <strong>{selectedAccount.fullName}</strong>
            <small>{selectedAccount.email}</small>
          </div>
        </div>

        <form className="login-form-panel" onSubmit={handleSubmit}>
          <div className="login-form-header">
            <p>{mode === 'register' ? t('login.createAccount') : t('login.accountLogin')}</p>
            <h2>{mode === 'register' ? t('login.signUpTitle') : t('login.welcomeBack')}</h2>
          </div>

          <div className="login-mode-toggle" role="tablist" aria-label={t('login.accountType')}>
            <button type="button" className={mode === 'login' ? 'active' : ''} onClick={() => { setMode('login'); setError(''); setSuccess('') }}>
              {t('login.signIn')}
            </button>
            <button type="button" className={mode === 'register' ? 'active' : ''} onClick={() => { setMode('register'); setError(''); setSuccess('') }}>
              {t('login.signUp')}
            </button>
          </div>

          {mode === 'register' ? (
            <label className="login-field">
              <span>{t('login.fullName')}</span>
              <input
                type="text"
                value={fullName}
                autoComplete="name"
                onChange={(event) => setFullName(event.target.value)}
              />
            </label>
          ) : null}

          <label className="login-field">
            <span>{t('common.email')}</span>
            <input
              type="email"
              value={email}
              autoComplete="email"
              onChange={(event) => setEmail(event.target.value)}
            />
          </label>

          <label className="login-field">
            <span>{t('common.password')}</span>
            <input
              type="password"
              value={password}
              autoComplete={mode === 'register' ? 'new-password' : 'current-password'}
              onChange={(event) => setPassword(event.target.value)}
            />
          </label>

          {mode === 'register' ? (
            <label className="login-field">
              <span>{t('login.confirmPassword')}</span>
              <input
                type="password"
                value={confirmPassword}
                autoComplete="new-password"
                onChange={(event) => setConfirmPassword(event.target.value)}
              />
            </label>
          ) : null}

          {error ? <p className="login-error">{error}</p> : null}
          {success ? <p className="login-success">{success}</p> : null}

          <button className="login-submit" type="submit">
            <Icon name="login" />
            {mode === 'register' ? t('login.createAccountButton') : t('login.signIn')}
          </button>

          <p className="login-helper-text">
            {mode === 'register' ? t('login.haveAccount') : t('login.needAccount')}
          </p>

          <div className="demo-account-list" aria-label={t('login.demoAccounts')}>
            {demoAccounts.map((account) => (
              <button
                className={`demo-account ${account.role}`}
                type="button"
                key={account.email}
                onClick={() => fillAccount(account)}
              >
                <span>{account.initials}</span>
                <div>
                  <strong>{account.role === 'admin' ? t('common.admin') : t('common.user')}</strong>
                  <small>{account.email}</small>
                </div>
              </button>
            ))}
          </div>
        </form>
      </section>
    </main>
  )
}

function Icon({ name }) {
  const paths = {
    brain: <path d="M9 4a3 3 0 0 0-3 3v1a3 3 0 0 0 0 6v1a3 3 0 0 0 5 2.2M15 4a3 3 0 0 1 3 3v1a3 3 0 0 1 0 6v1a3 3 0 0 1-5 2.2M12 5v14M8 10h3M13 10h3M8 15h3M13 15h3" />,
    login: <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4M10 17l5-5-5-5M15 12H3" />,
  }

  return (
    <svg className="login-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      {paths[name]}
    </svg>
  )
}
