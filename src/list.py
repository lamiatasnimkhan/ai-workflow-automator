import os
import google.genai as genai

# Load API key from environment
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# List available models correctly
print("Available Gemini models:")
models = client.models.list()  # <- correct method
for model in models:
    print(model.name, "-", getattr(model, "description", "No description"))
