import os

def save_result(text: str):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(base_dir, "results")
    os.makedirs(results_dir, exist_ok=True)

    file_path = os.path.join(results_dir, "sample_output.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
