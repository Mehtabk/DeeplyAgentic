"""Multi-Agent Pipeline — DeeplyAgentic Quickstart (Ollama)

A minimal Planner → Executor → Validator pipeline using local Ollama.
Demonstrates the 4-layer architecture with zero API keys.

Usage:
    ollama pull llama3.1:8b
    pip install ollama
    python multi_agent_pipeline_ollama.py
"""

import ollama

AGENTS = {
    "Planner": "Break down the user's goal into 3-5 concrete steps. For each step: what to do, what's needed, how to verify. Be specific.",
    "Executor": "Execute the plan step by step. For each step, describe what you did and confirm the result. If stuck, suggest alternatives.",
    "Validator": "Review the output against the original goal. Check completeness, accuracy, quality. Output: PASS, PASS WITH NOTES, or FAIL with explanation.",
}

MODEL = "llama3.1:8b"


def run_agent(name: str, task: str) -> str:
    print(f"\n{'─'*50}\n🤖 {name} working...\n{'─'*50}")
    response = ollama.chat(model=MODEL, messages=[
        {"role": "system", "content": AGENTS[name]},
        {"role": "user", "content": task},
    ])
    output = response["message"]["content"]
    print(output)
    return output


def main():
    task = input("\n🎯 Enter your task: ") or "Create a project README for a Python CLI tool"
    print(f"\n🚀 Running pipeline for: {task}\n")

    plan = run_agent("Planner", task)
    execution = run_agent("Executor", f"Original goal: {task}\n\nPlan to execute:\n{plan}")
    validation = run_agent("Validator", f"Original goal: {task}\n\nExecution result:\n{execution}")

    print(f"\n{'═'*50}\n✅ Pipeline complete.\n{'═'*50}")


if __name__ == "__main__":
    main()
