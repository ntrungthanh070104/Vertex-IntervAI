const INTERVIEW_RESULT_KEY = 'talentGraph.interviewResult'
const INTERVIEW_HISTORY_KEY = 'talentGraph.interviewHistory'

function getStorage() {
  return typeof window !== 'undefined' && window.localStorage ? window.localStorage : null
}

function getUserStorageKey(key, userId) {
  return userId ? `${key}.${userId}` : key
}

export function loadInterviewResult(userId) {
  const storage = getStorage()

  if (!storage) {
    return null
  }

  for (const key of [getUserStorageKey(INTERVIEW_RESULT_KEY, userId), INTERVIEW_RESULT_KEY]) {
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

export function loadInterviewHistory(userId) {
  const storage = getStorage()

  if (!storage) {
    return []
  }

  for (const key of [getUserStorageKey(INTERVIEW_HISTORY_KEY, userId), INTERVIEW_HISTORY_KEY]) {
    try {
      const stored = storage.getItem(key)
      const parsed = stored ? JSON.parse(stored) : []
      if (Array.isArray(parsed)) {
        return parsed
      }
    } catch {
      // fallback to next key
    }
  }

  return []
}

export function saveInterviewResult(result, userId) {
  const storage = getStorage()

  if (!storage) {
    return
  }

  const resolvedUserId = userId || result?.userId || 'default'
  const history = loadInterviewHistory(resolvedUserId)
  const nextHistory = [result, ...history.filter((item) => item.interviewId !== result.interviewId)].slice(0, 10)

  storage.setItem(getUserStorageKey(INTERVIEW_RESULT_KEY, resolvedUserId), JSON.stringify(result))
  storage.setItem(getUserStorageKey(INTERVIEW_HISTORY_KEY, resolvedUserId), JSON.stringify(nextHistory))
  storage.setItem(INTERVIEW_RESULT_KEY, JSON.stringify(result))
  storage.setItem(INTERVIEW_HISTORY_KEY, JSON.stringify(nextHistory))
}

export function createInterviewResult({ session, currentUser, cvAnalysis, answers }) {
  const completedAt = new Date().toISOString()
  const scoredAnswers = answers.filter((answer) => Number.isFinite(answer.score))
  const overallScore = scoredAnswers.length
    ? Math.round(scoredAnswers.reduce((total, answer) => total + answer.score, 0) / scoredAnswers.length)
    : 0
  const strongAnswers = scoredAnswers.filter((answer) => answer.score >= 80).length
  const weakAnswers = scoredAnswers.filter((answer) => answer.score < 60).length

  return {
    interviewId: session.interviewId,
    userId: currentUser.userId,
    candidateName: currentUser.fullName,
    role: session.role,
    cvId: cvAnalysis?.cvId,
    cvScore: cvAnalysis?.cvScore,
    overallScore,
    status: 'Completed',
    totalQuestions: session.questions.length,
    answeredQuestions: scoredAnswers.length,
    completedAt,
    focus: session.focus,
    strengths: buildStrengths(strongAnswers, overallScore),
    improvements: buildImprovements(weakAnswers, overallScore),
    recommendation: buildRecommendation(overallScore),
    answers: scoredAnswers,
  }
}

export function formatInterviewDate(value) {
  if (!value) return 'Not completed'

  return new Intl.DateTimeFormat('en', {
    month: 'short',
    day: '2-digit',
    year: 'numeric',
  }).format(new Date(value))
}

function buildStrengths(strongAnswers, overallScore) {
  if (overallScore >= 85) {
    return [
      'Clear technical communication',
      'Good project examples',
      'Strong interview readiness',
    ]
  }

  if (strongAnswers >= 2) {
    return [
      'Good technical foundation',
      'Able to connect skills with project work',
      'Ready for more practice rounds',
    ]
  }

  return [
    'Understands the interview topic',
    'Can improve with more structured answers',
    'Needs more concrete examples',
  ]
}

function buildImprovements(weakAnswers, overallScore) {
  if (overallScore >= 85 && weakAnswers === 0) {
    return [
      'Add more measurable results',
      'Explain tradeoffs more clearly',
      'Prepare deeper system design examples',
    ]
  }

  if (overallScore >= 70) {
    return [
      'Use the STAR structure more consistently',
      'Add one result or metric to each answer',
      'Explain debugging steps in more detail',
    ]
  }

  return [
    'Avoid very short answers',
    'Mention specific tools and technologies',
    'Connect every answer to one real project',
  ]
}

function buildRecommendation(overallScore) {
  if (overallScore >= 85) {
    return 'Strong performance. You can move to a harder technical round with deeper architecture, debugging, and cloud questions.'
  }

  if (overallScore >= 70) {
    return 'Good foundation. Practice adding concrete project context, measurable results, and tradeoffs to make answers more convincing.'
  }

  return 'Needs more practice before a real interview. Focus on answering with one project example, one technology, and one result for every question.'
}
