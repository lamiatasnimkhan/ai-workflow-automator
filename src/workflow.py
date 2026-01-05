from src.llm_module import generate_summary
from src.utils import save_result

def run_workflow(input_text: str):
    summary = generate_summary(input_text)
    save_result(summary)
    return summary
