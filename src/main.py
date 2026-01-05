from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.workflow import run_workflow

app = FastAPI(title="AI Workflow Automator")

class WorkflowInput(BaseModel):
    text: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "AI Workflow Automator is running 🚀"}

@app.post("/run-workflow")
def run(data: WorkflowInput):
    result = run_workflow(data.text)
    return {
        "result": result
    }