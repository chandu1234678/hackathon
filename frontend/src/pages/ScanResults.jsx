import { useState } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'

export default function ScanResults() {
  const navigate = useNavigate()
  const location = useLocation()
  const [activeNav, setActiveNav] = useState('scans')

  // Get the uploaded image from navigation state
  const previewImage = location.state?.previewImage || 'https://lh3.googleusercontent.com/aida-public/AB6AXuBmrmUJgLy3J6LtrRZUy5vfgoGO81CWsILYytvUBiZ1vhpzGOo0gcPQE7J--hbpgRuIXN1e2oaWg6-ulowLYIUFnhRRnCYbzVC36zgcE7Tz0N26Fc5pPUF4fzJtroUGU6cSwCCIGJIqTbbwCYSRKMFzRJL7GXmafGWOGE88BEoKOcnhsp-rBjz9bhV4yV5OsY2v1aSQMqg4DYpNTP0EDvFWMl8Ps54Sglu19YuSNSIE7cPKf2BtnCFmLoP3vt4JMDueufOFmAr9i7g'

  return (
    <div className="min-h-screen flex flex-col bg-light text-slate-900 font-display">
      {/* Header Navigation */}
      <header className="flex items-center bg-white p-4 border-b border-slate-200 sticky top-0 z-10">
        <button
          onClick={() => navigate('/foot-scan-analysis')}
          className="text-primary flex size-10 items-center justify-center cursor-pointer hover:bg-slate-100 rounded-lg transition-colors"
        >
          <span className="material-symbols-outlined">arrow_back</span>
        </button>
        <h2 className="text-slate-900 text-lg font-bold leading-tight flex-1 text-center">Scan Results</h2>
        <button className="text-slate-900 hover:bg-slate-100 rounded-lg p-2 transition-colors">
          <span className="material-symbols-outlined">share</span>
        </button>
      </header>

      <main className="flex-1 overflow-y-auto pb-24">
        {/* Visual Comparison Section */}
        <div className="grid grid-cols-2 gap-3 p-4">
          <div className="flex flex-col gap-2">
            <div
              className="w-full aspect-square bg-slate-200 rounded-xl bg-cover bg-center"
              style={{
                backgroundImage: `url('${previewImage}')`
              }}
            ></div>
            <p className="text-slate-600 text-sm font-medium text-center">Original Photo</p>
          </div>
          <div className="flex flex-col gap-2">
            <div
              className="w-full aspect-square bg-slate-200 rounded-xl bg-cover bg-center relative overflow-hidden"
              style={{
                backgroundImage: `url('${previewImage}')`
              }}
            >
              {/* Heatmap Overlay Effect */}
              <div className="absolute inset-0 bg-gradient-to-tr from-red-500/40 via-yellow-400/20 to-transparent mix-blend-overlay"></div>
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-16 h-16 bg-red-500/60 blur-xl rounded-full animate-pulse"></div>
            </div>
            <p className="text-slate-600 text-sm font-medium text-center">AI Heatmap</p>
          </div>
        </div>

        {/* Detection Status */}
        <div className="px-4 text-center mt-4">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-100 text-red-600 mb-2">
            <span className="material-symbols-outlined text-sm">warning</span>
            <span className="text-xs font-bold uppercase tracking-wider">Urgent Attention</span>
          </div>
          <h1 className="text-slate-900 text-3xl font-extrabold tracking-tight">Ulcer Detected</h1>
        </div>

        {/* Metric Cards */}
        <div className="grid grid-cols-2 gap-4 p-4 mt-2">
          <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
            <p className="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Confidence</p>
            <div className="flex items-baseline gap-1">
              <p className="text-slate-900 text-2xl font-bold">98%</p>
              <span className="text-primary material-symbols-outlined text-lg">verified</span>
            </div>
          </div>
          <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
            <p className="text-slate-500 text-xs font-semibold uppercase tracking-wider mb-1">Risk Level</p>
            <div className="flex items-center gap-2">
              <p className="text-red-600 text-2xl font-bold">High</p>
              <div className="flex gap-1">
                <div className="w-2 h-4 rounded-full bg-slate-200"></div>
                <div className="w-2 h-4 rounded-full bg-slate-200"></div>
                <div className="w-2 h-4 rounded-full bg-red-500"></div>
              </div>
            </div>
          </div>
        </div>

        {/* AI Explanation Text */}
        <div className="px-4 pb-8">
          <div className="bg-primary/5 p-5 rounded-xl border border-primary/20">
            <div className="flex items-center gap-2 mb-3">
              <span className="material-symbols-outlined text-primary">auto_awesome</span>
              <h3 className="text-slate-900 font-bold">AI Analysis Summary</h3>
            </div>
            <p className="text-slate-700 text-sm leading-relaxed">
              Our AI model has identified significant tissue irregularities in the mid-foot region. The heatmap indicates localized inflammation and potential break in skin integrity. Based on visual markers, there is a high probability of a grade 2 diabetic foot ulcer.
              <br/><br/>
              <span className="font-bold text-slate-900">Recommendation:</span> We strongly advise scheduling a consultation with your podiatrist within the next 24-48 hours.
            </p>
            <button className="mt-4 w-full bg-primary text-white font-bold py-3 rounded-lg flex items-center justify-center gap-2 shadow-lg shadow-primary/30 hover:bg-primary/90 transition-colors">
              <span className="material-symbols-outlined">calendar_today</span>
              Book Appointment
            </button>
          </div>
        </div>
      </main>

      {/* Bottom Navigation Bar */}
      <nav className="bg-white border-t border-slate-200 pb-6 pt-2 px-4 shadow-[0_-4px_12px_rgba(0,0,0,0.05)] fixed bottom-0 left-0 right-0">
        <div className="flex justify-between items-center max-w-md mx-auto">
          <button
            onClick={() => {
              setActiveNav('home')
              navigate('/dashboard')
            }}
            className="flex flex-col items-center gap-1 text-slate-400 hover:text-slate-900 transition-colors"
          >
            <span className="material-symbols-outlined">home</span>
            <span className="text-[10px] font-bold uppercase">Home</span>
          </button>
          <button
            onClick={() => setActiveNav('scans')}
            className="flex flex-col items-center gap-1 text-primary"
          >
            <span className="material-symbols-outlined">camera</span>
            <span className="text-[10px] font-bold uppercase">Scans</span>
          </button>
          <button className="flex flex-col items-center gap-1 text-slate-400 hover:text-slate-900 transition-colors">
            <span className="material-symbols-outlined">bar_chart</span>
            <span className="text-[10px] font-bold uppercase">Reports</span>
          </button>
          <button className="flex flex-col items-center gap-1 text-slate-400 hover:text-slate-900 transition-colors">
            <span className="material-symbols-outlined">person</span>
            <span className="text-[10px] font-bold uppercase">Profile</span>
          </button>
        </div>
      </nav>
    </div>
  )
}
