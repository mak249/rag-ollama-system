# 🚀 RAG System Deployment Guide

## Overview
This guide covers deploying your RAG system to the cloud with separate frontend and backend hosting.

## Architecture
- **Frontend**: Static hosting (Netlify/Vercel)
- **Backend**: Server hosting (Railway/Render) - Required for Ollama

---

## 📋 Pre-Deployment Checklist

### 1. GitHub Repository Setup
```bash
# Navigate to your project
cd d:\ollamma

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "RAG system ready for deployment"

# Create GitHub repository and push
git remote add origin https://github.com/yourusername/rag-ollama-system.git
git branch -M main
git push -u origin main
```

### 2. Environment Configuration
Ensure these files are ready:
- ✅ `.gitignore` - Excludes sensitive files
- ✅ `requirements.txt` - Python dependencies
- ✅ `Dockerfile` - Container configuration
- ✅ `start.sh` - Startup script
- ✅ `netlify.toml` - Netlify configuration
- ✅ `vercel.json` - Vercel configuration

---

## 🌐 Frontend Deployment

### Option 1: Netlify
1. **Connect Repository**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub repository

2. **Build Settings**
   - Build command: `echo 'Static site ready'`
   - Publish directory: `frontend_simple`
   - Deploy site

3. **Custom Domain** (Optional)
   - Add your custom domain in site settings

### Option 2: Vercel
1. **Import Project**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository

2. **Configuration**
   - Framework Preset: Other
   - Root Directory: `frontend_simple`
   - Deploy

---

## 🖥️ Backend Deployment

### Option 1: Railway (Recommended)
1. **Setup Railway**
   ```bash
   # Install Railway CLI
   npm install -g @railway/cli
   
   # Login
   railway login
   ```

2. **Deploy**
   ```bash
   # Initialize project
   railway init
   
   # Deploy
   railway up
   ```

3. **Environment Variables**
   Set in Railway dashboard:
   ```
   OLLAMA_HOST=0.0.0.0
   PYTHONPATH=/app
   PORT=8000
   ```

### Option 2: Render
1. **Connect Repository**
   - Go to [render.com](https://render.com)
   - Create new "Web Service"
   - Connect GitHub repository

2. **Configuration**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `./start.sh`
   - Environment: Docker

3. **Environment Variables**
   ```
   OLLAMA_HOST=0.0.0.0
   PYTHONPATH=/app
   ```

---

## 🔧 Post-Deployment Configuration

### 1. Update Frontend Configuration
After backend deployment, get your backend URL and update:

**File**: `frontend_simple/config.js`
```javascript
const config = {
    development: {
        API_BASE_URL: 'http://127.0.0.1:8000'
    },
    production: {
        API_BASE_URL: 'https://your-actual-backend-url.railway.app'  // Update this
    }
};
```

### 2. Update CORS Settings
**File**: `backend/main.py`
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3001",
        "https://your-frontend-url.netlify.app",  # Add your frontend URL
        "https://your-frontend-url.vercel.app"   # Or Vercel URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 3. Redeploy
```bash
# Commit changes
git add .
git commit -m "Update production URLs"
git push

# Redeploy (automatic on most platforms)
```

---

## 🧪 Testing Deployment

### 1. Frontend Testing
- Visit your deployed frontend URL
- Check browser console for errors
- Test the interface loads correctly

### 2. Backend Testing
- Visit `https://your-backend-url/docs`
- Test API endpoints
- Check logs for errors

### 3. Integration Testing
- Submit a test query through the frontend
- Verify it reaches the backend
- Check response is displayed correctly

---

## 🔍 Troubleshooting

### Common Issues

#### Frontend Issues
- **CORS Errors**: Update backend CORS settings
- **API Not Found**: Check backend URL in config.js
- **Build Failures**: Verify all files are committed

#### Backend Issues
- **Ollama Not Starting**: Check Docker configuration
- **Memory Issues**: Increase server resources
- **Model Download Fails**: Check internet connectivity

#### Integration Issues
- **API Calls Failing**: Verify URLs match
- **Timeout Errors**: Increase server timeout settings

### Debug Commands
```bash
# Check backend logs
railway logs

# Test API directly
curl -X POST "https://your-backend-url/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "test"}'
```

---

## 📊 Monitoring & Maintenance

### Performance Monitoring
- Monitor response times
- Check error rates
- Monitor resource usage

### Updates
```bash
# Update dependencies
pip install --upgrade -r requirements.txt

# Commit and redeploy
git add requirements.txt
git commit -m "Update dependencies"
git push
```

---

## 💰 Cost Considerations

### Free Tier Limits
- **Netlify**: 100GB bandwidth/month
- **Vercel**: 100GB bandwidth/month
- **Railway**: $5/month after trial
- **Render**: Free tier available

### Optimization Tips
- Use CDN for static assets
- Implement caching
- Optimize model sizes
- Monitor usage

---

## 🎯 Success Checklist

- [ ] GitHub repository created and pushed
- [ ] Frontend deployed and accessible
- [ ] Backend deployed with Ollama running
- [ ] API endpoints responding correctly
- [ ] Frontend can communicate with backend
- [ ] Test queries working end-to-end
- [ ] Custom domains configured (if needed)
- [ ] Monitoring set up
- [ ] Documentation updated with live URLs

---

**Your RAG system is now live and accessible worldwide! 🌍**
