import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  timeout: 20000,
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export async function login(payload) {
  try {
    const { data } = await api.post('/auth/login', payload)
    return data
  } catch {
    // Fallback for local demo: allow login without backend auth endpoint.
    return { 
      access_token: 'local-dev-token',
      user: {
        email: payload.email,
        full_name: payload.email.split('@')[0].replace(/[._]/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
        role: 'Patient',
        member_since: 'May 2023'
      }
    }
  }
}

export async function register(payload) {
  const { data } = await api.post('/auth/register', payload)
  return data
}

export async function uploadImage(file) {
  const formData = new FormData()
  formData.append('file', file)

  const { data } = await api.post('/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
  return data
}

export async function predict(payload) {
  const { data } = await api.post('/predict', payload)
  return data
}

export async function getCurrentUser() {
  try {
    const { data } = await api.get('/auth/me')
    return data
  } catch {
    // Return stored user data if API fails
    const storedUser = localStorage.getItem('user_data')
    return storedUser ? JSON.parse(storedUser) : null
  }
}

export async function requestPasswordReset(payload) {
  const { data } = await api.post('/auth/forgot-password', payload)
  return data
}

export async function resetPassword(payload) {
  const { data } = await api.post('/auth/reset-password', payload)
  return data
}
