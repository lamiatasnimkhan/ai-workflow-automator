AI Workflow Automator 

Automate text workflows with AI! This project uses Google Gemini (GenAI API) for text summarization, FastAPI for the backend API, and a React frontend for easy interaction.

<img width="676" height="568" alt="image" src="https://github.com/user-attachments/assets/e721de22-47d3-4f8d-b623-076115e33819" />


Features:

Summarize text automatically using Google Gemini.
Full REST API built with FastAPI.
React UI for user-friendly interactions.
Save results locally in /results/.
Easily extendable for additional workflows.

Tech Stack:
Layer	Technology
Backend	Python, FastAPI, Pydantic
AI / LLM	Google Gemini (GenAI API)
Frontend	React

Usage:

Enter your text in the React UI or via the API endpoint.
Text is summarized via Gemini LLM.
Results are saved in /results/sample_output.txt.

Notes / Limitations:

Ensure your Gemini API key has sufficient quota.
Currently supports text summarization only.
Gemini model names and versions may change → check list.py for available models.

