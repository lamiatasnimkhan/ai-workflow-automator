import google.generativeai as genai
import os

def setup_gemini():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_text(text: str) -> str:
    model = genai.GenerativeModel("models/gemini-2.0-flash-001")
    response = model.generate_content(
        f"Summarize the following text:\n{text}"
    )
    return response.text
