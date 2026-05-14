# Quickstart

> Build your first multi-agent system in 5 minutes.

## Option 1: Python (OpenAI Agents SDK)

The simplest way to run a Planner → Executor → Validator pipeline.

### Setup

```bash
# Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Run
cd quickstart
export OPENAI_API_KEY=your-key-here
uv run multi_agent_pipeline.py
```

That's it. `uv run` handles dependency resolution automatically from `pyproject.toml`.

### Alternative (pip)

```bash
cd quickstart
pip install .
python multi_agent_pipeline.py
```

## Option 2: TypeScript (Mastra)

```bash
npm install mastra
export OPENAI_API_KEY=your-key-here
node multi_agent_pipeline.mjs
```

## What It Does

This example implements the 4-layer architecture:

1. **Orchestrator** receives a task and routes it
2. **Planner** breaks it into steps
3. **Executor** runs each step
4. **Validator** checks the output before delivery

See the full architecture in [The Agentic Stack](../the-agentic-stack/).
