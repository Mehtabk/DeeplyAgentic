# Agentic AI Reading List

> Curated papers, articles, talks, and resources on building AI agent systems.

Updated weekly. Star this repo to stay current.

---

## Foundational Papers

| Paper | Year | Key Insight |
|-------|------|-------------|
| [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) | 2022 | Interleaving reasoning traces with tool actions |
| [Toolformer](https://arxiv.org/abs/2302.04761) | 2023 | LLMs learning to use tools autonomously |
| [Generative Agents](https://arxiv.org/abs/2304.03442) | 2023 | Believable simulacra with memory and reflection |
| [Voyager](https://arxiv.org/abs/2305.16291) | 2023 | Lifelong learning agent with skill library |
| [AutoGen](https://arxiv.org/abs/2308.08155) | 2023 | Multi-agent conversation framework |
| [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) | 2022 | Step-by-step reasoning improves complex tasks |
| [Self-Refine](https://arxiv.org/abs/2303.17651) | 2023 | Iterative self-feedback without human input |
| [BES: Backward-Forward Evolutionary Search](https://github.com/Embodied-Minds-Lab/BES) | 2025 | Self-improving AI on hard reasoning — forward recombination + backward sub-goal decomposition beats standard post-training |

## Architecture & Orchestration

| Resource | Type | Topic |
|----------|------|-------|
| [Building Effective Agents (Anthropic)](https://www.anthropic.com/research/building-effective-agents) | Guide | Patterns for reliable agent systems |
| [OpenAI Multi-Agent Research](https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf) | Paper | Governance of agentic systems |
| [Microsoft AutoGen Paper](https://arxiv.org/abs/2308.08155) | Paper | Multi-agent orchestration patterns |
| [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) | Docs | Stateful agent workflows |
| [Model Context Protocol Spec](https://modelcontextprotocol.io/) | Spec | Standard for agent-tool communication |

## Open-Source Tools & Projects

| Project | Stars | Description |
|---------|-------|-------------|
| [OpenSandbox](https://github.com/alibaba/OpenSandbox) | 11k | Secure sandbox runtime for coding agents — Docker/K8s backends, gVisor/Kata/Firecracker isolation, egress policy, MCP server, audit trails |
| [LiteParse v2](https://github.com/run-llama/liteparse) | — | Fastest open-source PDF parser — 457 pages in 0.7s, Rust core, 50+ doc types, runs local on Python/Node/browser/edge |
| [Mirage](https://github.com/strukto-ai/mirage) | — | Virtual filesystem mounting S3, Drive, Slack, Gmail, GitHub, Notion, Postgres — agents use bash commands, snapshot/rollback workspaces |
| [Obsidian Second Brain](https://github.com/eugeniughelbur/obsidian-second-brain) | 1.5k | Writable agent memory via Obsidian — 43 commands, mutation over accumulation, works across Claude Code, Codex, Gemini, OpenCode |
| [Deep Agents](https://github.com/langchain-ai/deep-agents) | — | LangChain's open-source Claude Code alternative — any LLM, sub-agents, persistent memory, checkpointing, MCP support |
| [Hermes Agent](https://github.com/nesquena/hermes-webui) | — | Persistent AI assistant with memory across sessions — web + CLI + 10 messaging platforms, scheduled offline jobs |
| [Second-Me](https://github.com/mindverse/Second-Me) | 10k+ | Build your AI clone — trains on your memories, runs fully offline, deploys to decentralized networks |
| [CodeGraph](https://github.com/optave/ops-codegraph-tool) | 50+ | MCP server that pre-indexes codebases into a knowledge graph — cuts tool calls by 92%, supports 11+ languages |
| [Transformer Explainer](https://github.com/poloclub/transformer-explainer) | — | Interactive visualization of GPT-2 running live in your browser — see embeddings, attention, and token ranking in real time |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 50k | Multi-agent orchestration framework |
| [OpenHands](https://github.com/OpenHands/OpenHands) | 76k | AI-driven development platform — SDK, CLI, RBAC, Kubernetes, GitHub/GitLab/Slack/Jira integrations |
| [SkillSpector](https://github.com/nvidia/skillspector) | — | NVIDIA's security scanner for agent skills — detects vulnerabilities, malicious patterns, risk scores. LangGraph workflow, SARIF output |
| [Skills Best Practices](https://github.com/mgechev/skills-best-practices) | — | Definitive guide to structuring agent skills — folder conventions, lazy loading, description triggers, 500-line max |
| [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | — | 230+ lessons across 20 phases — math to agents, MCP, swarms. Python, TypeScript, Rust, Julia |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 30k | Build agents as stateful graphs |
| [AutoGen](https://github.com/microsoft/autogen) | 57k | Multi-agent conversation framework |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | 25k | Lightweight multi-agent workflows |
| [Haystack](https://github.com/deepset-ai/haystack) | 25k | Production RAG & agent pipelines |

## Industry Reports (2026)

| Report | Source | Key Finding |
|--------|--------|-------------|
| [Global AI Diffusion Report](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/) | Microsoft | 17.8% global AI adoption, 4% work usage |
| [IBM Think 2026](https://www.ibm.com/think/news/think-2026-ai-recap) | IBM | 1,600+ agents per enterprise by year-end |
| [Salesforce Connectivity Report 2026](https://www.salesforce.com/news/stories/connectivity-report-announcement-2026/) | Salesforce | Orgs average 12 agents, 67% growth projected |
| [Agentic AI Poised for Progress](https://www.cio.com/article/4116514/agentic-ai-poised-for-progress-in-2026-if-cios-get-it-right.html) | CIO/Gartner | 40% of agent projects cancelled without architecture |

## Talks & Videos

| Talk | Speaker | Topic |
|------|---------|-------|
| [Code w/ Claude 2026 — Full Playlist (15 talks)](https://youtube.com/playlist?list=PLmWCw1CzcFinm44PAkEoR2glf-iNPhulP) | Anthropic | Subagents, MCP, scaling to real codebases, managed agents, proactive workflows |
| [Spec-Driven Development: How AI Changed Everything](https://lnkd.in/eAqVETdw) | Simon Martinelli | Why specs matter more with AI agents |
| [Agentic RAG with OpenAI Agents SDK + MCP](https://www.linkedin.com/in/eddonner) | Ed Donner | Building RAG agents with MCP servers |

## Free Courses

| Course | Provider | Level |
|--------|----------|-------|
| [Introduction to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills) | Anthropic Academy | Beginner |
| [Introduction to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | Anthropic Academy | Intermediate |
| [MCP: Advanced Topics](https://anthropic.skilljar.com/mcp-advanced-topics) | Anthropic Academy | Advanced |
| [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | Anthropic Academy | Intermediate |
| [Building with the Claude API](https://anthropic.skilljar.com/building-with-the-claude-api) | Anthropic Academy | Intermediate |

## Newsletters & Blogs

| Name | Focus |
|------|-------|
| [Anthropic Research Blog](https://www.anthropic.com/research) | Agent safety, capabilities |
| [LangChain Blog](https://blog.langchain.dev/) | Agent frameworks, LangGraph |
| [Hugging Face Blog](https://huggingface.co/blog) | Open-source AI, trends |
| [ByteByteGo](https://blog.bytebytego.com/) | System design + AI architecture |

---

## Contributing

Found something that belongs here? Open a PR.

**Format:** `| [Title](url) | Type/Source | One-line description |`

**Rules:**
- Must be directly relevant to building agent systems
- Prefer primary sources over summaries
- No paywalled content without a free alternative

---

*Last updated: 2026-06-20*
