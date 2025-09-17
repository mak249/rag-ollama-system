@echo off
echo 🚀 RAG System Deployment Helper
echo.

echo Step 1: Initialize Git Repository
git init
git add .
git commit -m "Initial RAG system commit"

echo.
echo Step 2: GitHub Repository Setup
echo Please create a new repository on GitHub and run:
echo git remote add origin https://github.com/yourusername/rag-ollama-system.git
echo git branch -M main  
echo git push -u origin main

echo.
echo Step 3: Deployment Options
echo.
echo Frontend Deployment:
echo - Netlify: https://netlify.com (Connect GitHub repo)
echo - Vercel: https://vercel.com (Import GitHub repo)
echo.
echo Backend Deployment:
echo - Railway: npm install -g @railway/cli, then railway login, railway init, railway up
echo - Render: https://render.com (Connect GitHub repo)
echo.

echo Step 4: After Deployment
echo 1. Update frontend_simple/config.js with your backend URL
echo 2. Update backend/main.py CORS settings with your frontend URL
echo 3. Commit and push changes

echo.
echo 📖 For detailed instructions, see DEPLOYMENT_GUIDE.md
echo.
pause
