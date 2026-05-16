# Quickstart

> Build your first multi-agent system in 5 minutes.

## Option A: Local with Ollama (No API keys needed) ⭐

Run a Planner → Executor → Validator pipeline entirely on your machine. Free. Private.

```bash
# Install Ollama and pull a model
brew install ollama && ollama pull llama3.1:8b

# Run
cd quickstart
pip install ollama
python multi_agent_pipeline_ollama.py
```

That's it. Zero API keys. Zero cost. Everything stays on your machine.

---

## Option B: Cloud with OpenAI Agents SDK

Uses OpenAI's multi-agent SDK. Requires an API key.

```bash
# Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Run
cd quickstart
export OPENAI_API_KEY=your-key-here
uv run multi_agent_pipeline.py
```

`uv run` handles dependency resolution automatically from `pyproject.toml`.

---

## What It Does

Both options implement the same 4-layer architecture:

1. **Orchestrator** receives a task and routes it
2. **Planner** breaks it into steps
3. **Executor** runs each step
4. **Validator** checks the output before delivery

```
Task → 🎯 Orchestrator → 🧠 Planner → ⚡ Executor → 🔍 Validator → ✅ Output
```

See the full architecture in [The Agentic Stack](../the-agentic-stack/).

---

## Which should I pick?

| | Ollama (Local) | OpenAI (Cloud) |
|---|---|---|
| **Cost** | Free | Pay per token |
| **Privacy** | 100% local | Data sent to OpenAI |
| **Quality** | Good (8B model) | Best (GPT-4o) |
| **Speed** | Depends on hardware | Fast |
| **Setup** | `brew install ollama` | Need API key |
| **Best for** | Learning, privacy, offline | Production, complex tasks |
