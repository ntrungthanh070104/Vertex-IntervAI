function getStorage() {
  return typeof window !== 'undefined' && window.localStorage ? window.localStorage : null
}

function getPreferenceKey(userId, key) {
  return userId ? `talentGraph.${key}.${userId}` : `talentGraph.${key}`
}

export function getUserPreference(userId, key, fallback = null) {
  const storage = getStorage()

  if (!storage) {
    return fallback
  }

  const stored = storage.getItem(getPreferenceKey(userId, key))

  if (stored === null) {
    return fallback
  }

  try {
    return JSON.parse(stored)
  } catch {
    return stored
  }
}

export function setUserPreference(userId, key, value) {
  const storage = getStorage()

  if (!storage) {
    return
  }

  storage.setItem(getPreferenceKey(userId, key), JSON.stringify(value))
}

export function getPreferredInterviewRole(userId, fallback = 'Frontend Developer Intern') {
  return getUserPreference(userId, 'preferredInterviewRole', fallback) || fallback
}

export function setPreferredInterviewRole(userId, value) {
  if (!value) {
    return
  }

  setUserPreference(userId, 'preferredInterviewRole', value)
}
