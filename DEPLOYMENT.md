# MedVision AI - Deployment Guide

## 🚀 Quick Start (Local Development)

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: http://localhost:8000
API Documentation: http://localhost:8000/docs

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at: http://localhost:5173

---

## 🌐 Render Deployment

### Prerequisites
- GitHub account with repository
- Render account (free tier available)

### Deploy to Render

#### Option 1: Blueprint (Recommended)
1. Push code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Click "New" → "Blueprint"
4. Connect your repository
5. Render will automatically detect `render.yaml` and deploy all services

#### Option 2: Manual Setup

**Backend:**
1. New Web Service
2. Connect repository
3. Settings:
   - **Build Command:** `cd backend && pip install -r requirements.txt`
   - **Start Command:** `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Health Check Path:** `/health`
4. Environment Variables:
   - `PYTHON_VERSION`: 3.11.0
   - `SECRET_KEY`: (generate random string)
   - `ENVIRONMENT`: production

**Frontend:**
1. New Static Site
2. Connect repository
3. Settings:
   - **Build Command:** `cd frontend && npm install && npm run build`
   - **Publish Directory:** `frontend/dist`
4. Environment Variables:
   - `VITE_API_URL`: Your backend URL from step above

---

## 🔒 Environment Variables

### Backend (.env)
```env
SECRET_KEY=your-secret-key-min-32-characters
DATABASE_URL=postgresql://user:password@host:5432/dbname
ENVIRONMENT=production
JWT_SECRET_KEY=your-jwt-secret
CORS_ORIGINS=https://your-frontend.onrender.com
```

### Frontend (.env)
```env
VITE_API_URL=https://your-backend.onrender.com
```

---

## 🏥 Health Check Endpoints

The backend includes multiple health check endpoints to prevent sleeping:

- `GET /health` - Main health check (used by Render)
- `GET /health/ping` - Simple uptime ping
- `GET /health/ready` - Readiness probe
- `GET /health/live` - Liveness probe
- `GET /health/status` - Detailed system status

### Keep-Alive Strategy
To prevent Render free tier from sleeping:
1. Use external monitoring service (e.g., UptimeRobot, Cronitor)
2. Ping `/health/ping` every 10-14 minutes
3. Configure in monitoring service dashboard

Recommended Services:
- [UptimeRobot](https://uptimerobot.com/) - Free, 5-minute intervals
- [Cronitor](https://cronitor.io/) - Free tier available
- [Better Uptime](https://betteruptime.com/) - Free tier available

---

## 📦 Other Deployment Platforms

### Heroku
```bash
# Login
heroku login

# Create app
heroku create medvision-ai-backend

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Deploy
git push heroku main

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
```

### Railway
1. Connect GitHub repository
2. Railway auto-detects Python/Node.js
3. Add PostgreSQL database
4. Set environment variables in dashboard

### Vercel (Frontend Only)
```bash
cd frontend
npm install -g vercel
vercel deploy
```

---

## 🗄️ Database Setup

### Local (SQLite)
- Automatically created on first run
- Location: `backend/medvision.db`

### Production (PostgreSQL)
```bash
# Render automatically provides DATABASE_URL
# Or use external provider:
# - Neon (Free tier)
# - Supabase (Free tier)
# - ElephantSQL (Free tier)
```

---

## ✅ Pre-Deployment Checklist

- [ ] Update `SECRET_KEY` and `JWT_SECRET_KEY` (min 32 characters)
- [ ] Configure database (PostgreSQL for production)
- [ ] Set `CORS_ORIGINS` to your frontend URL
- [ ] Update `VITE_API_URL` in frontend
- [ ] Test health endpoints locally
- [ ] Run `npm run build` to verify frontend builds
- [ ] Test API endpoints with Postman/curl
- [ ] Set up monitoring/keep-alive service
- [ ] Configure custom domain (optional)

---

## 🔧 Troubleshooting

### Backend won't start
- Check Python version (3.9+)
- Verify all environment variables set
- Check database connection
- Review logs: `heroku logs --tail` or Render dashboard

### Frontend shows API errors
- Verify `VITE_API_URL` matches backend URL
- Check CORS settings in backend
- Inspect browser console for errors

### App goes to sleep
- Set up monitoring service pinging `/health/ping`
- Upgrade to paid tier for always-on
- Use multiple free-tier services with monitoring

---

## 📊 Monitoring

### Health Checks
- `/health` - Service status
- `/health/status` - System metrics
- `/metrics` - Prometheus metrics

### Logs
- **Render**: Dashboard → Your Service → Logs
- **Heroku**: `heroku logs --tail`
- **Railway**: Dashboard logs tab

---

## 🎯 Production Best Practices

1. **Security**
   - Use strong secret keys (min 32 characters)
   - Enable HTTPS only
   - Restrict CORS origins
   - Set secure cookie flags

2. **Performance**
   - Enable CDN for frontend static assets
   - Use Redis for caching (optional)
   - Optimize images before upload
   - Enable gzip compression

3. **Monitoring**
   - Set up uptime monitoring
   - Configure error tracking (Sentry)
   - Monitor API response times
   - Set up log aggregation

4. **Backup**
   - Regular database backups
   - Store model weights externally (S3, Cloudinary)
   - Version control all code changes

---

## 📝 API Documentation

Once deployed, visit:
- Swagger UI: `https://your-backend.onrender.com/docs`
- ReDoc: `https://your-backend.onrender.com/redoc`

---

## 🆘 Support

For issues:
1. Check logs in deployment dashboard
2. Test health endpoints
3. Verify environment variables
4. Review this deployment guide

Common endpoints:
- Backend Health: `https://your-backend.onrender.com/health`
- Frontend: `https://your-frontend.onrender.com`
- API Docs: `https://your-backend.onrender.com/docs`
