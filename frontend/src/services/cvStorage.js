const CV_STORAGE_KEY = 'talentGraph.cvAnalysis'
const MAX_CV_SIZE = 10 * 1024 * 1024
const ALLOWED_EXTENSIONS = ['pdf', 'doc', 'docx']
const ALLOWED_TYPES = [
  'application/pdf',
  'application/msword',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
]

function getStorage() {
  return typeof window !== 'undefined' && window.localStorage ? window.localStorage : null
}

function getUserStorageKey(userId) {
  return userId ? `${CV_STORAGE_KEY}.${userId}` : CV_STORAGE_KEY
}

export function loadCvAnalysis(userId) {
  const storage = getStorage()

  if (!storage) {
    return null
  }

  for (const key of [getUserStorageKey(userId), CV_STORAGE_KEY]) {
    try {
      const stored = storage.getItem(key)
      if (stored) {
        return JSON.parse(stored)
      }
    } catch {
      // fallback to next key
    }
  }

  return null
}

export function saveCvAnalysis(analysis, userId) {
  const storage = getStorage()

  if (!storage) {
    return
  }

  const resolvedUserId = userId || analysis?.userId || 'default'
  storage.setItem(getUserStorageKey(resolvedUserId), JSON.stringify(analysis))
  storage.setItem(CV_STORAGE_KEY, JSON.stringify(analysis))
}

export function validateCvFile(file) {
  if (!file) {
    return 'NO_FILE'
  }

  const extension = getFileExtension(file.name)
  const hasValidExtension = ALLOWED_EXTENSIONS.includes(extension)
  const hasValidType = ALLOWED_TYPES.includes(file.type) || file.type === ''

  if (!hasValidExtension || !hasValidType) {
    return 'INVALID_FILE_TYPE'
  }

  if (file.size > MAX_CV_SIZE) {
    return 'FILE_TOO_LARGE'
  }

  return ''
}

export function createMockCvAnalysis(file) {
  const uploadedAt = new Date().toISOString()
  const fileName = file.name
  const baseName = fileName.replace(/\.[^.]+$/, '')
  const scoreOffset = Math.min(Math.round(file.size / 400000), 8)
  const cvScore = Math.max(78, 91 - scoreOffset)

  return {
    cvId: createId(),
    fileName,
    fileSize: file.size,
    uploadedAt,
    cvScore,
    suggestedPosition: 'Frontend Developer Intern',
    summary: `${baseName} was parsed successfully and is ready for AI interview generation.`,
    skills: ['React', 'JavaScript', 'Python', 'AWS Lambda', 'DynamoDB', 'REST API'],
    projects: ['Talent-Graph AI', 'CV Analysis Dashboard', 'Voice Interview Flow'],
    experience: ['Frontend development', 'API integration', 'Cloud fundamentals'],
    certificates: ['AWS Cloud Practitioner - planned', 'React fundamentals'],
    recommendation:
      'Focus on AWS Lambda error handling, DynamoDB query design, and concise system design explanations before starting the next interview.',
    talentScores: [
      { label: 'React', score: 88 },
      { label: 'Python', score: 76 },
      { label: 'AWS', score: 72 },
      { label: 'Database', score: 68 },
      { label: 'Communication', score: 82 },
      { label: 'Problem Solving', score: 79 },
    ],
    skillGroups: [
      { label: 'Frontend', value: 88, skills: 'React, JavaScript, Vite', tone: 'purple' },
      { label: 'Backend', value: 76, skills: 'Python, REST APIs, Lambda', tone: 'blue' },
      { label: 'Cloud', value: 72, skills: 'S3, Bedrock, DynamoDB', tone: 'orange' },
      { label: 'Communication', value: 82, skills: 'Clear answers, steady flow', tone: 'green' },
    ],
  }
}

export function formatFileSize(bytes) {
  if (!bytes) return '0 KB'
  if (bytes < 1024 * 1024) return `${Math.round(bytes / 1024)} KB`
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
}

export function formatUploadDate(value) {
  if (!value) return 'Not analyzed yet'

  return new Intl.DateTimeFormat('en', {
    month: 'short',
    day: '2-digit',
    year: 'numeric',
  }).format(new Date(value))
}

function getFileExtension(fileName) {
  return fileName.split('.').pop()?.toLowerCase() ?? ''
}

function createId() {
  if (window.crypto?.randomUUID) {
    return window.crypto.randomUUID()
  }

  return `cv-${Date.now()}`
}
