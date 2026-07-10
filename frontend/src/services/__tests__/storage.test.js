import test from 'node:test'
import assert from 'node:assert/strict'

import { loadCvAnalysis, saveCvAnalysis } from '../cvStorage.js'
import { loadInterviewHistory, saveInterviewResult } from '../interviewStorage.js'

class MemoryStorage {
  constructor() {
    this.store = new Map()
  }

  getItem(key) {
    return this.store.has(key) ? this.store.get(key) : null
  }

  setItem(key, value) {
    this.store.set(key, String(value))
  }

  removeItem(key) {
    this.store.delete(key)
  }

  clear() {
    this.store.clear()
  }
}

globalThis.window = { localStorage: new MemoryStorage() }
globalThis.localStorage = globalThis.window.localStorage

test('cv data is stored and loaded separately per user', () => {
  saveCvAnalysis({ cvId: 'cv-1', cvScore: 88 }, 'user-a')
  saveCvAnalysis({ cvId: 'cv-2', cvScore: 91 }, 'user-b')

  assert.deepEqual(loadCvAnalysis('user-a'), { cvId: 'cv-1', cvScore: 88 })
  assert.deepEqual(loadCvAnalysis('user-b'), { cvId: 'cv-2', cvScore: 91 })
})

test('interview history is stored separately per user', () => {
  saveInterviewResult({ interviewId: 'i-1', userId: 'user-a', overallScore: 82 }, 'user-a')
  saveInterviewResult({ interviewId: 'i-2', userId: 'user-b', overallScore: 90 }, 'user-b')

  assert.equal(loadInterviewHistory('user-a').length, 1)
  assert.equal(loadInterviewHistory('user-b').length, 1)
  assert.equal(loadInterviewHistory('user-a')[0].interviewId, 'i-1')
  assert.equal(loadInterviewHistory('user-b')[0].interviewId, 'i-2')
})
