# The Agentic Stack

> A curated guide to building production-grade AI agent systems — organized by architecture layer.

Most agent projects fail not because of bad models, but because of missing architecture. This repo maps the tools, frameworks, and patterns you need at each layer of the stack.

## The 4-Layer Architecture

```
┌─────────────────────────────────────────┐
│  🎯  Orchestration Layer            │
├─────────────────────────────────────────┤
│  🧠  Agent Layer (Skills + Memory)  │
├─────────────────────────────────────────┤
│  🔌  Tool Layer (MCP + APIs)        │
├─────────────────────────────────────────┤
│  🛡️  Guardrails Layer              │
└─────────────────────────────────────────┘
```

---

## Layer 4: Orchestration

Routes requests to the right agent. Coordinates multi-agent workflows. Governs outputs.

| Tool | Description | Link |
|------|-------------|------|
| AWS Agent Squad | Multi-agent orchestration framework | [GitHub](https://github.com/awslabs/multi-agent-orchestrator) |
| OpenAI Swarm | Lightweight multi-agent patterns | [GitHub](https://github.com/openai/swarm) |
| Claude Flow | Multi-agent orchestration for Claude | [GitHub](https://github.com/ruvnet/claude-code-flow) |
| Microsoft Copilot Studio | Enterprise multi-agent orchestration | [Docs](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/) |
| LangGraph | Stateful agent workflows | [GitHub](https://github.com/langchain-ai/langgraph) |
| CrewAI | Role-based multi-agent framework | [GitHub](https://github.com/crewAIInc/crewAI) |
| AutoGen | Multi-agent conversation framework | [GitHub](https://github.com/microsoft/autogen) |

## Layer 3: Agents (Skills + Memory)

Individual agents with domain expertise, memory, and reasoning capabilities.

| Tool | Description | Link |
|------|-------------|------|
| Claude Code | Agentic coding in terminal | [Docs](https://docs.anthropic.com/en/docs/claude-code) |
| OpenAI Agents SDK | Build agents with tools and handoffs | [GitHub](https://github.com/openai/openai-agents-python) |
| Agno | Lightweight, high-performance agents | [GitHub](https://github.com/agno-agi/agno) |
| Mastra | TypeScript agent framework | [GitHub](https://github.com/mastra-ai/mastra) |
| Semantic Anchors | Shared vocabulary for LLM agents | [GitHub](https://github.com/LLM-Coding/Semantic-Anchors) |

## Layer 2: Tools (MCP + APIs)

Connect agents to external systems via standardized protocols.

| Tool | Description | Link |
|------|-------------|------|
| MCP Specification | Model Context Protocol standard | [Docs](https://modelcontextprotocol.io/) |
| Awesome MCP Servers | Collection of MCP servers | [GitHub](https://github.com/punkpeye/awesome-mcp-servers) |
| MCP Agent | Build agents using MCP workflows | [GitHub](https://github.com/lastmile-ai/mcp-agent) |
| Composio | 250+ tool integrations for agents | [GitHub](https://github.com/ComposioHQ/composio) |

## Layer 1: Guardrails

Hard constraints, quality hooks, and human-in-the-loop escalation.

| Tool | Description | Link |
|------|-------------|------|
| Guardrails AI | Input/output validation for LLMs | [GitHub](https://github.com/guardrails-ai/guardrails) |
| NeMo Guardrails | NVIDIA's programmable guardrails | [GitHub](https://github.com/NVIDIA/NeMo-Guardrails) |
| LLM Guard | Security toolkit for LLM interactions | [GitHub](https://github.com/protectai/llm-guard) |

---

## Key Stats (May 2026)

- 80% of enterprise apps shipped in Q1 2026 embed at least one AI agent (Gartner)
- 1,600+ agents per enterprise expected by end of 2026 (IBM)
- 40% of agentic AI projects predicted to be cancelled by 2027 without proper architecture (Gartner)
- 1,445% surge in multi-agent system inquiries Q1 2024 → Q2 2025 (Gartner)

---

## Contributing

Found a tool that belongs here? Open an issue or submit a PR.

**Rules:**
- Must fit one of the 4 layers
- Must be actively maintained
- Include: name, one-line description, and link

---

## About

Maintained by [DeeplyAgentic](https://www.linkedin.com/company/deeplyagentic) — building smart, scalable AI systems that do the heavy lifting.

🚀 Harness AI. Reclaim Time. Amplify Impact.
