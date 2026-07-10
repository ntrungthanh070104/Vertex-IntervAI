import { createContext, useCallback, useContext, useEffect, useMemo, useState } from 'react'
import { detectDefaultLocale, translate } from './translations.js'

const LANGUAGE_STORAGE_KEY = 'talentGraph.language'

const LanguageContext = createContext(null)

export function LanguageProvider({ children }) {
  const [locale, setLocaleState] = useState(() => detectDefaultLocale())

  const setLocale = useCallback((nextLocale) => {
    if (nextLocale !== 'en' && nextLocale !== 'vi') {
      return
    }

    setLocaleState(nextLocale)
    window.localStorage.setItem(LANGUAGE_STORAGE_KEY, nextLocale)
  }, [])

  useEffect(() => {
    document.documentElement.lang = locale
  }, [locale])

  const t = useCallback((key, params) => translate(locale, key, params), [locale])

  const value = useMemo(() => ({ locale, setLocale, t }), [locale, setLocale, t])

  return <LanguageContext.Provider value={value}>{children}</LanguageContext.Provider>
}

export function useLanguage() {
  const context = useContext(LanguageContext)

  if (!context) {
    throw new Error('useLanguage must be used within LanguageProvider')
  }

  return context
}
