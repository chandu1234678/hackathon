// Dark mode context and utility
export const applyDarkMode = () => {
  const darkMode = localStorage.getItem('darkMode') === 'true'
  if (darkMode) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
  return darkMode
}

export const toggleDarkMode = (enabled) => {
  localStorage.setItem('darkMode', enabled ? 'true' : 'false')
  if (enabled) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
}
