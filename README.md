# RAG System with Web Interface - Complete Project Package

## 🌟 Project Overview

A production-ready Retrieval-Augmented Generation (RAG) system with a modern web interface, built using FastAPI backend and vanilla JavaScript frontend. This system enables intelligent document querying using local AI models while maintaining complete data privacy.

## 📋 Deliverables Overview

This project includes all required deliverables for instructor submission:

### 1. 📄 Documentation (PDF Report)
- **File**: `RAG_Project_Documentation.md`
- **Sections**: Problem Statement & Use Case, Technical Architecture (with diagrams), Implementation (steps + code), Results (example queries, outputs), Challenges & Solutions, Conclusion & Next Steps
- **Format**: Comprehensive technical documentation ready for PDF conversion

### 2. 🎥 Demo Video Script (3-5 minutes)
- **File**: `Demo_Video_Script.md`
- **Content**: Explain → Show → Wrap-up format
- **Includes**: Web interface demo, backend server startup, query examples, error handling
- **Format**: Screen recording script with timing and backup scenarios

### 3. 📊 Presentation Slides (Industry Format, 5-7 slides)
- **File**: `Presentation_Slides.md`
- **Slides**: Title Slide, Problem & Business Context, Approach & Architecture, Implementation, Demo Results, Conclusion & Next Steps
- **Format**: Professional presentation format with speaker notes

### 4. 🏗️ Architecture Diagram
- **File**: `Architecture_Diagram.txt`
- **Content**: Complete system architecture with web interface, API flow, and component interactions
- **Format**: ASCII art diagram ready for visual conversion

## 🚀 Quick Start

### Prerequisites
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull required models
ollama pull llama3
ollama pull nomic-embed-text
```

### Setup & Run
```bash
# Navigate to project
cd ollamma

# Create virtual environment
python -m venv rag-env
rag-env\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Start Ollama service (in separate terminal)
ollama serve

# Start backend server
.\rag-env\Scripts\python.exe -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

# Start frontend server (in another terminal)
python -m http.server 3001 --directory frontend_simple

# Access the application
# Open browser to: http://localhost:3001
```

## 🚀 Deployment

### Local Development
```bash
# Clone the repository
git clone https://github.com/yourusername/rag-ollama-system.git
cd rag-ollama-system

# Install dependencies
pip install -r requirements.txt

# Run the system
./start_rag_system.bat
```

### Cloud Deployment

#### Frontend (Netlify/Vercel)
1. **Netlify**: Connect your GitHub repo and deploy
   - Build command: `echo 'Static site ready'`
   - Publish directory: `frontend_simple`

2. **Vercel**: Import your GitHub repo
   - Framework preset: Other
   - Root directory: `frontend_simple`

#### Backend (Railway/Render)
1. **Railway**:
   ```bash
   # Install Railway CLI
   npm install -g @railway/cli
   
   # Login and deploy
   railway login
   railway init
   railway up
   ```

2. **Render**: Connect GitHub repo
   - Build command: `pip install -r requirements.txt`
   - Start command: `./start.sh`

#### Environment Variables
Set these in your deployment platform:
```
OLLAMA_HOST=0.0.0.0
PYTHONPATH=/app
```

#### Update Frontend Configuration
After backend deployment, update `frontend_simple/config.js`:
```javascript
production: {
    API_BASE_URL: 'https://your-actual-backend-url.railway.app'
}
```

### GitHub Setup
```bash
# Initialize git repository
git init
git add .
git commit -m "Initial RAG system commit"

# Add remote and push
git remote add origin https://github.com/yourusername/rag-ollama-system.git
git branch -M main
git push -u origin main
```

## 📁 Project Structure
```
ollamma/
├── backend/                                # FastAPI backend server
│   ├── main.py                            # API server with CORS
│   ├── rag.py                             # RAG query processing
│   └── ingestion.py                       # Document processing pipeline
├── frontend_simple/                        # Web frontend
│   └── index.html                         # Complete web interface
├── docs/                                   # Document storage
│   ├── sample.text
│   ├── cloud_computing_basics.txt
│   ├── cybersecurity_fundamentals.txt
│   └── machine_learning_overview.txt
├── chroma_db/                             # Vector database storage
├── rag-env/                               # Python virtual environment
├── requirements.txt                       # Python dependencies
├── RAG_Project_Documentation.md           # Complete technical documentation
├── Demo_Video_Script.md                   # Video recording script
├── Presentation_Slides.md                 # Industry presentation slides
├── Architecture_Diagram.txt               # System architecture diagram
└── README.md                              # This file
```

## 🎯 Key Features

- **Modern Web Interface**: Clean, responsive UI with real-time feedback
- **FastAPI Backend**: RESTful API with automatic documentation
- **Local Processing**: No external API calls - complete privacy
- **Multi-format Support**: PDF, TXT, TEXT files
- **Intelligent Retrieval**: Context-aware responses using vector similarity
- **Production Ready**: Comprehensive error handling, loading states, CORS support
- **Performance Optimized**: 2-5 second response times
- **Easy Deployment**: Simple setup with clear documentation

## 📊 Performance Metrics

- **Document Processing**: 4 documents → 4 chunks indexed
- **Query Response Time**: 2-5 seconds per query
- **Web Interface**: Real-time feedback with loading indicators
- **API Response**: JSON format with comprehensive error handling
- **Memory Usage**: Efficient local processing
- **Accuracy**: High relevance in retrieved context
- **User Experience**: Professional UI with error states and feedback

## 🛠️ Technical Stack

### Backend
- **API Framework**: FastAPI (Python 3.10+)
- **LLM Framework**: Ollama (Local LLM hosting)
- **Embeddings**: Nomic Embed Text
- **Vector Database**: ChromaDB
- **Document Processing**: LangChain Community
- **HTTP Server**: Uvicorn ASGI server

### Frontend
- **Interface**: HTML5, CSS3, JavaScript (ES6+)
- **HTTP Client**: Fetch API
- **Styling**: Modern responsive CSS with animations
- **Server**: Python built-in HTTP server

## 📝 Usage Examples

### Web Interface
1. Open browser to `http://localhost:3001`
2. Enter questions in the input field
3. Click "Ask" or press Enter
4. View real-time responses with context

### Example Queries
- "What is artificial intelligence?"
- "What are the core principles of cybersecurity?"
- "Explain supervised vs unsupervised learning"
- "Give me an overview of cloud computing"

### API Usage
```bash
# Direct API calls
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is machine learning?"}'
```

### Adding Documents
```bash
# Add more documents to docs/ folder
python backend/ingestion.py
```

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Set custom models
$env:CHAT_MODEL = "llama3"
$env:EMBED_MODEL = "nomic-embed-text"
$env:DOCS_FILE = "docs/sample.text"
```

### Tunable Parameters
- `chunk_size = 500` (Document chunk size)
- `chunk_overlap = 50` (Overlap between chunks)
- `k = 2` (Number of retrieved documents)
- `num_predict = 128` (Maximum response length)
- `timeout = 30` (Request timeout in seconds)

## 🚨 Troubleshooting

### Common Issues
1. **"Model not found"**: Run `ollama pull llama3` and `ollama pull nomic-embed-text`
2. **"Connection refused"**: Start Ollama with `ollama serve`
3. **Backend not starting**: Check if port 8000 is available
4. **Frontend not loading**: Ensure port 3001 is available
5. **CORS errors**: Backend includes CORS middleware for cross-origin requests
6. **Slow responses**: Reduce `num_predict` or use smaller models

### Error Messages
- **API errors**: Check browser developer tools for detailed error messages
- **Timeout errors**: Increase timeout in backend configuration
- **Import errors**: Ensure all packages are installed with `pip install -r requirements.txt`
- **Path errors**: Ensure ChromaDB directory exists and is accessible

## 📈 Future Enhancements

### Short-term (1-2 months)
- Document upload functionality through web interface
- Query history and favorites
- Advanced chunking strategies
- User authentication and session management
- Enhanced error reporting and logging

### Medium-term (3-6 months)
- Multi-modal document support (images, audio)
- Real-time document synchronization
- Analytics dashboard for query patterns
- Custom model fine-tuning interface

### Long-term (6+ months)
- Distributed architecture for scalability
- Enterprise features (RBAC, audit logs)
- Advanced RAG techniques (re-ranking, multi-step reasoning)
- Mobile-responsive progressive web app

## 📚 Additional Resources

### Documentation Files
- `RAG_Project_Documentation.md` - Complete technical documentation
- `Demo_Video_Script.md` - Step-by-step demo script
- `Presentation_Slides.md` - Industry presentation format
- `Architecture_Diagram.txt` - System architecture visualization

### Learning Resources
- [Ollama Documentation](https://ollama.ai/docs)
- [LangChain Documentation](https://python.langchain.com/docs)
- [ChromaDB Documentation](https://docs.trychroma.com/)

## 🤝 Contributing

This project is designed as a learning exercise and demonstration. Feel free to:
- Add new document types
- Implement additional features
- Optimize performance
- Extend the architecture

## 📄 License

This project is for educational purposes. Please ensure you have appropriate licenses for any models or data you use.

---

**Project Status**: ✅ Complete  
**Last Updated**: [Current Date]  
**Author**: [Your Name]  
**Version**: 1.0

---

*For instructor submission, convert the markdown files to PDF format and record the demo video following the provided script.*
