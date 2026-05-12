Why Did My Model Break? 🧹

An AI-powered debugging assistant that analyzes your ML error logs and training metrics — and tells you exactly what went wrong and how to fix it.


🚀 Demo
<img width="1777" height="919" alt="Screenshot 2026-05-12 175226" src="https://github.com/user-attachments/assets/937712b4-d059-4925-b31f-869707fe932a" /><img width="1890" height="981" alt="Screenshot 2026-05-12 174904" src="https://github.com/user-attachments/assets/f25acaad-4e19-4f64-b8a8-bcfb1d5a38ad" />



🧩 Problem It Solves
Every ML developer faces this: model trains perfectly, hits 99% accuracy, then breaks in production or fails on validation data. Debugging takes hours of Googling. This tool gives you an instant, structured diagnosis — just paste your log and get answers in seconds.

⚙️ How It Works
User pastes error log / training metrics
        ↓
Streamlit UI sends POST request
        ↓
FastAPI backend receives the input
        ↓
LangChain formats it into a structured prompt
        ↓
Groq (LLaMA 3.1) analyzes and diagnoses
        ↓
Structured response returned to UI

🛠️ Tech Stack
LayerTechnologyFrontendStreamlitBackendFastAPILLMLLaMA 3.1 via Groq APILLM FrameworkLangChainContainerizationDockerLanguagePython 3.10

📁 Project Structure
ml-debug-assistant/
├── app/
│   ├── main.py          # FastAPI backend
│   ├── analyzer.py      # LangChain + Groq logic
│   └── prompts.py       # Prompt templates
├── ui/
│   └── streamlit_app.py # Streamlit frontend
├── .env                 # API keys (not committed)
├── requirements.txt
└── Dockerfile

🏃 How to Run Locally
1. Clone the repo
bashgit clone https://github.com/Uttkarsha26/ml-debug-assistant
cd ml-debug-assistant
2. Create virtual environment
bashpython -m venv venv
source venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
4. Add your API key
Create a .env file:
GROQ_API_KEY=your_groq_api_key_here
Get free key at: https://console.groq.com
5. Run FastAPI backend
bashuvicorn app.main:app --reload
6. Run Streamlit UI (new terminal)
bashstreamlit run ui/streamlit_app.py
7. Open browser
http://localhost:8501

🐳 Run with Docker
bashdocker build -t ml-debug-assistant .
docker run -p 8000:8000 --env-file .env ml-debug-assistant

💡 Example Inputs to Try
# Overfitting
Epoch 12/20
Training Accuracy: 99%
Validation Accuracy: 48%
Validation loss increasing continuously.
# NaN error
ValueError: Input contains NaN.
Check your training data pipeline.
# Memory error
CUDA out of memory. Tried to allocate 2.50 GiB
batch_size=128, model=ResNet50

📊 What the Diagnosis Covers

✅ Problem identification
✅ Root cause explanation
✅ Step-by-step fix
✅ Prevention tips


🔮 Future Improvements

 Stage 5: HuggingFace + FAISS semantic fallback for offline use
 Upload .log or .txt files directly
 History of past diagnoses
 Support for TensorFlow training logs


👤 Author
Uttkarsha Karhadkar

GitHub: @Uttkarsha26
LinkedIn: uttkarsha-karhadkar


📄 License
MIT License
