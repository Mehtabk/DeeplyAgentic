<p align="center">
  <img src="./assets/deeplyagentic_logo.jpeg" alt="DeeplyAgentic" width="300"/>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/github/stars/Mehtabk/DeeplyAgentic?style=flat&color=8b5cf6" alt="Stars">
  <img src="https://img.shields.io/github/last-commit/Mehtabk/DeeplyAgentic?color=10b981" alt="Last Commit">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
</p>

<p align="center">
  Architecture, prompts, and tools for AI agent systems that actually work in production.<br/>
  🚀 <strong>Harness AI. Reclaim Time. Amplify Impact.</strong>
</p>

<p align="center">
  <a href="https://www.deeplyagentic.com">🌐 Website</a> ·
  <a href="https://www.linkedin.com/company/deeplyagentic">💼 LinkedIn</a> ·
  <a href="./quickstart/">⚡ Quickstart</a>
</p>

---

## 🔥 Trending This Week

| Project | Why it matters |
|---------|---------------|
| [Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) | Mythos-class model publicly available — autonomous multi-hour tasks, parallel subagents, beat Pokémon with vision alone, novel genomics research |
| [Skills.sh](https://www.skills.sh) | Open ecosystem for reusable agent skills — one `npx` command gives your agent procedural knowledge across 20+ coding agents |
| [Mirage](https://github.com/strukto-ai/mirage) | Virtual filesystem that mounts S3, Drive, Slack, Gmail, GitHub, Notion, Postgres under one root — agents use bash, zero API translation |
| [Deep Agents](https://github.com/langchain-ai/deep-agents) | LangChain's open-source Claude Code alternative — any LLM, $0, sub-agents, memory, checkpointing via LangGraph |
| [Hermes Agent](https://github.com/nesquena/hermes-webui) | Persistent AI assistant with memory across sessions — web + CLI + 10 messaging platforms, scheduled jobs |
| [CodeGraph](https://github.com/optave/ops-codegraph-tool) | MCP server that cuts Claude Code tool calls by 92% — pre-indexes your codebase into a knowledge graph |
| [Second-Me](https://github.com/mindverse/Second-Me) | Build your AI clone that runs fully offline — trains on your memories, deploys to decentralized networks |

---

## Get Started

```bash
# Option A: Local (no API keys needed)
git clone https://github.com/Mehtabk/DeeplyAgentic.git
cd DeeplyAgentic/quickstart
pip install ollama && python multi_agent_pipeline_ollama.py

# Option B: Cloud (OpenAI)
export OPENAI_API_KEY=your-key
uv run multi_agent_pipeline.py
```

---

## Projects

| Project | Description |
|---------|-------------|
| [**⚡ Quickstart**](./quickstart/) | Run a multi-agent pipeline (Planner → Executor → Validator) in 5 minutes. |
| [**📚 The Agentic Stack**](./the-agentic-stack/) | Curated tools for production agent systems — organized by architecture layer. |
| [**🧠 Agent Prompts**](./agent-prompts/) | Production-ready system prompts — Planner, Executor, Validator, Orchestrator, Summarizer. |
| [**🔍 Comparisons**](./comparisons/) | Side-by-side framework comparison: CrewAI vs AutoGen vs LangGraph vs OpenAI SDK vs Mastra. |
| [**✅ Checklists**](./checklists/) | Pre-launch checklist for agent systems. Don't ship without it. |
| [**📐 Diagrams**](./diagrams/) | Copy-paste Mermaid diagrams for agent architectures. |
| [**📝 Agent Decisions**](./agent-decisions/) | Architecture Decision Records (ADRs) for agent systems. |
| [**🔁 Patterns**](./patterns/) | Reusable architectural patterns — cost routing, escalation, retry logic. |
| [**📖 Reading List**](./reading-list/) | Curated papers, reports, talks, and courses. Updated weekly. |

---

## The 4-Layer Architecture

> Most agent projects fail not because of bad models — but because of missing architecture.

```mermaid
flowchart TB
    subgraph Orchestration["🎯 Orchestration Layer"]
        Router[Router] --> Coordinator[Coordinator]
    end
    subgraph Agents["🧠 Agent Layer"]
        A1[Planner] --> A2[Executor]
        A2 --> A3[Validator]
    end
    subgraph Tools["🔌 Tool Layer - MCP"]
        T1[APIs] --> T2[Databases]
        T2 --> T3[Services]
    end
    subgraph Guardrails["🛡️ Guardrails"]
        G1[Validation] --> G2[Escalation]
    end
    Orchestration --> Agents
    Agents --> Tools
    Guardrails -.->|enforces| Orchestration
    Guardrails -.->|enforces| Agents
    Guardrails -.->|enforces| Tools
```

---

## Key Stats (May 2026)

| Stat | Source |
|------|--------|
| 80% of enterprise apps embed at least one AI agent | Gartner Q1 2026 |
| 40% of agentic AI projects cancelled without architecture | Gartner |
| 1,600+ agents per enterprise by year-end | IBM 2026 |
| 1,445% surge in multi-agent inquiries | Gartner |

---

## Community

| | |
|---|---|
| 💼 [LinkedIn](https://www.linkedin.com/company/deeplyagentic) | Architecture breakdowns, tool reviews, and weekly agent ecosystem updates |
| 🌐 [Website](https://www.deeplyagentic.com) | Landing page and resource hub |
| 📰 [Changelog](./CHANGELOG.md) | Weekly updates to the repo |

> **Want to be featured?** If you're using DeeplyAgentic patterns in production, open a PR to add your story.

---

## Contributing

We welcome contributions! See individual project folders for guidelines.

**Quick ways to contribute:**
- 🐛 Found a broken link? Open an issue
- 📚 Know a tool that belongs here? Submit a PR
- ⭐ Star this repo to help others find it

---

MIT License © 2026 DeeplyAgentic
