import { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const runWorkflow = async () => {
    if (!text.trim()) {
      setResult("⚠️ Please enter some text");
      return;
    }

    setLoading(true);
    setResult("");

    try {
      const response = await fetch("http://127.0.0.1:8000/run-workflow", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
      });

      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      setResult("❌ Server error");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🤖 AI Workflow Automator</h1>
      <p>Summarize text using Gemini AI</p>

      <textarea
        placeholder="Paste text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button onClick={runWorkflow} disabled={loading}>
        {loading ? "Running..." : "Run AI Workflow"}
      </button>

      <div className="output">
        <h3>Result</h3>
        <p>{result || "Your AI output will appear here..."}</p>
      </div>
    </div>
  );
}

export default App;
