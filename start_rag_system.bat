@echo off
echo Starting RAG System...

echo.
echo 1. Starting Backend Server...
start "Backend Server" cmd /k "cd /d %~dp0 && .\rag-env\Scripts\python.exe -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload"

echo.
echo 2. Waiting for backend to start...
timeout /t 8 /nobreak >nul

echo.
echo 3. Starting Frontend Server...
start "Frontend Server" cmd /k "cd /d %~dp0\frontend_simple && python -m http.server 3001"

echo.
echo 4. Opening web browser...
timeout /t 3 /nobreak >nul
start http://localhost:3001

echo.
echo RAG System is now running!
echo - Frontend: http://localhost:3001
echo - Backend API: http://localhost:8000/docs
echo - Ollama: Already running on port 11434
echo.
echo Press any key to exit...
pause >nul
