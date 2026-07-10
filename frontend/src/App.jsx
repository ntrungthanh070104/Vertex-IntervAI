import { useEffect, useState } from 'react'
import Dashboard from './pages/Dashboard/Dashboard.jsx'
import History from './pages/History/History.jsx'
import Interview from './pages/Interview/Interview.jsx'
import Login from './pages/Login/Login.jsx'
import LandingPage from './pages/Landing/LandingPage.jsx'
import Profile from './pages/Profile/Profile.jsx'
import Result from './pages/Result/Result.jsx'
import UploadCV from './pages/UploadCV/UploadCV.jsx'
import { loadAuthUser, logoutAuthUser } from './services/authService.js'
import { loadCvAnalysis } from './services/cvStorage.js'
import { loadInterviewResult } from './services/interviewStorage.js'

const availablePages = ['dashboard', 'upload-cv', 'interview', 'profile', 'result', 'history']

function App() {
  const [currentUser, setCurrentUser] = useState(() => loadAuthUser())
  const [currentPage, setCurrentPage] = useState('dashboard')
  const [showLanding, setShowLanding] = useState(() => !loadAuthUser())
  const [cvAnalysis, setCvAnalysis] = useState(() => loadCvAnalysis(loadAuthUser()?.userId))
  const [interviewResult, setInterviewResult] = useState(() => loadInterviewResult(loadAuthUser()?.userId))

  useEffect(() => {
    if (!currentUser?.userId) {
      setCvAnalysis(null)
      setInterviewResult(null)
      return
    }

    setCvAnalysis(loadCvAnalysis(currentUser.userId))
    setInterviewResult(loadInterviewResult(currentUser.userId))
  }, [currentUser?.userId])

  function handleNavigate(page) {
    if (availablePages.includes(page)) {
      setCurrentPage(page)
    }
  }

  function handleUploadComplete(analysis) {
    setCvAnalysis(analysis)
  }

  function handleInterviewComplete(result) {
    setInterviewResult(result)
  }

  function handleLogin(user) {
    setCurrentUser(user)
    setShowLanding(false)
    setCurrentPage('dashboard')
  }

  function handleLogout() {
    logoutAuthUser()
    setCurrentUser(null)
    setShowLanding(true)
    setCurrentPage('dashboard')
  }

  function handleStartAuth(mode = 'login') {
    setShowLanding(false)
    setCurrentPage('dashboard')
    if (mode === 'register') {
      return
    }
  }

  if (showLanding && !currentUser) {
    return <LandingPage onStartAuth={handleStartAuth} />
  }

  if (!currentUser) {
    return <Login onLogin={handleLogin} />
  }

  if (currentPage === 'upload-cv') {
    return (
      <UploadCV
        cvAnalysis={cvAnalysis}
        currentUser={currentUser}
        onNavigate={handleNavigate}
        onLogout={handleLogout}
        onUploadComplete={handleUploadComplete}
      />
    )
  }

  if (currentPage === 'interview') {
    return (
      <Interview
        cvAnalysis={cvAnalysis}
        currentUser={currentUser}
        onNavigate={handleNavigate}
        onLogout={handleLogout}
        onInterviewComplete={handleInterviewComplete}
      />
    )
  }

  if (currentPage === 'profile') {
    return (
      <Profile
        cvAnalysis={cvAnalysis}
        currentUser={currentUser}
        onNavigate={handleNavigate}
        onLogout={handleLogout}
      />
    )
  }

  if (currentPage === 'result') {
    return (
      <Result
        interviewResult={interviewResult}
        currentUser={currentUser}
        onNavigate={handleNavigate}
        onLogout={handleLogout}
      />
    )
  }

  if (currentPage === 'history') {
    return (
      <History
        currentUser={currentUser}
        onNavigate={handleNavigate}
        onLogout={handleLogout}
      />
    )
  }

  return (
    <Dashboard
      cvAnalysis={cvAnalysis}
      interviewResult={interviewResult}
      currentUser={currentUser}
      onNavigate={handleNavigate}
      onLogout={handleLogout}
    />
  )
}

export default App
