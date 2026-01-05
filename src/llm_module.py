import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_summary(text: str) -> str:
    try:
        response = client.models.generate_content(
            model="models/gemini-2.0-flash-001",
            contents=f"Summarize the following text in 2–3 concise sentences:\n{text}"
        )
        return response.text.strip()
    except Exception as e:
        return f"ERROR: Gemini call failed: {str(e)}"
