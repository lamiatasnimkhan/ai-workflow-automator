AI Workflow Automator 🚀

Automate text workflows with AI! This project uses Google Gemini (GenAI API) for text summarization, FastAPI for the backend API, and a React frontend for easy interaction. Perfect for showcasing AI, ML, and full-stack skills on GitHub.

Demo
<img width="676" height="568" alt="image" src="https://github.com/user-attachments/assets/e721de22-47d3-4f8d-b623-076115e33819" />


Features

Summarize text automatically using Google Gemini.

Full REST API built with FastAPI.

React UI for user-friendly interactions.

Save results locally in /results/.

Easily extendable for additional workflows.

Tech Stack
Layer	Technology
Backend	Python, FastAPI, Pydantic
AI / LLM	Google Gemini (GenAI API)
Frontend	React, Tailwind CSS (optional)
Version Control	Git + GitHub
Project Structure
Ai workflow automator/
├─ venv/                  # Python virtual environment
├─ src/
│  ├─ main.py             # FastAPI server entry point
│  ├─ workflow.py         # Workflow logic
│  ├─ utils.py            # Helper functions
│  ├─ list.py             # Gemini model listing script
├─ frontend/              # React frontend app
│  ├─ package.json
│  └─ src/
├─ results/               # Generated summaries and outputs
├─ requirements.txt       # Python dependencies
├─ .gitignore
└─ README.md

Setup & Installation
1. Clone the repository
git clone https://github.com/lamiatasnimkhan/ai-workflow-automator.git
cd ai-workflow-automator

2. Setup Python Backend
# Create virtual environment
python -m venv venv

# Activate
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

3. Set Gemini API Key

GEMINI_API_KEY=your_api_key_here

4. Run Backend
python src/main.py

Visit http://127.0.0.1:8000/ → Should see a running message.

API endpoint: POST http://127.0.0.1:8000/run-workflow

Example payload:

{
  "text": "Artificial Intelligence is transforming healthcare, finance, and education by automating decision-making."
}

5. Run Frontend (React)
cd frontend
npm install
npm start


Opens React UI at http://localhost:3000.

Enter text and run workflows visually.

Usage

Enter your text in the React UI or via the API endpoint.

Text is summarized via Gemini LLM.

Results are saved in /results/sample_output.txt.

Notes / Limitations

Ensure your Gemini API key has sufficient quota.

Currently supports text summarization only.

Gemini model names and versions may change → check list.py for available models.

