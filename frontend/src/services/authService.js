const AUTH_STORAGE_KEY = 'talentGraph.authUser'
const AUTH_USERS_KEY = 'talentGraph.authUsers'

export const demoAccounts = [
  {
    userId: 'user_demo_001',
    fullName: 'Nguyen Huy Dat',
    email: 'user@talentgraph.ai',
    password: 'user123',
    role: 'user',
    initials: 'HD',
  },
  {
    userId: 'admin_demo_001',
    fullName: 'Admin Talent Graph',
    email: 'admin@talentgraph.ai',
    password: 'admin123',
    role: 'admin',
    initials: 'AD',
  },
]

function getStoredUsers() {
  try {
    const stored = window.localStorage.getItem(AUTH_USERS_KEY)
    const parsed = stored ? JSON.parse(stored) : []
    return Array.isArray(parsed) ? parsed : []
  } catch {
    return []
  }
}

function persistUsers(users) {
  window.localStorage.setItem(AUTH_USERS_KEY, JSON.stringify(users))
}

function getAllAccounts() {
  return [...demoAccounts, ...getStoredUsers()]
}

function toSafeUser(account) {
  const { password: _password, ...safeUser } = account
  return safeUser
}

function saveAuthUser(account) {
  const safeUser = toSafeUser(account)
  window.localStorage.setItem(AUTH_STORAGE_KEY, JSON.stringify(safeUser))
  return safeUser
}

export function loadAuthUser() {
  try {
    const stored = window.localStorage.getItem(AUTH_STORAGE_KEY)
    return stored ? JSON.parse(stored) : null
  } catch {
    return null
  }
}

export function loginWithDemoAccount(email, password) {
  const normalizedEmail = email.trim().toLowerCase()
  const account = getAllAccounts().find(
    (item) => item.email.toLowerCase() === normalizedEmail && item.password === password,
  )

  if (!account) {
    const error = new Error('INVALID_CREDENTIALS')
    error.code = 'INVALID_CREDENTIALS'
    throw error
  }

  return saveAuthUser(account)
}

export function registerUser({ fullName, email, password }) {
  const trimmedName = fullName.trim()
  const normalizedEmail = email.trim().toLowerCase()

  if (!trimmedName) {
    const error = new Error('NAME_REQUIRED')
    error.code = 'NAME_REQUIRED'
    throw error
  }

  if (!normalizedEmail || !password) {
    const error = new Error('MISSING_FIELDS')
    error.code = 'MISSING_FIELDS'
    throw error
  }

  const existingAccount = getAllAccounts().find((item) => item.email.toLowerCase() === normalizedEmail)
  if (existingAccount) {
    const error = new Error('EMAIL_EXISTS')
    error.code = 'EMAIL_EXISTS'
    throw error
  }

  const initials = trimmedName
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 2)
    .map((part) => part[0]?.toUpperCase() ?? '')
    .join('') || 'U'

  const newAccount = {
    userId: `user_${Date.now()}`,
    fullName: trimmedName,
    email: normalizedEmail,
    password,
    role: 'user',
    initials,
  }

  const users = [...getStoredUsers(), newAccount]
  persistUsers(users)

  return saveAuthUser(newAccount)
}

export function logoutAuthUser() {
  window.localStorage.removeItem(AUTH_STORAGE_KEY)
}
