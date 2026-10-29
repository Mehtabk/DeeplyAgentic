# Changelog

All notable changes to DeeplyAgentic are documented here.

---

## [2026-10-29]

### Added
- `agent-decisions/005-keyless-deploy-pipeline-identity.md` — ADR-005: deploy agents with a short-lived pipeline-bound identity instead of runner-held API keys. Validated on AWS Bedrock AgentCore and Azure AI Foundry.
- `agent-decisions/006-grounding-is-tool-design-safety-is-a-gate.md` — ADR-006: grounding is a property of the tool set, not the model; safety is a code-level gate, not a prompt instruction. Proven deterministically across both stacks.
- "What's New" section in README highlighting the latest ADRs.

### Changed
- Refreshed "Key Stats" to verified Oct 2026 Gartner figures (adoption gap, cancellation rate, ROI, spend forecasts); replaces the stale May 2026 table.
- Relabelled "Trending This Week" → "Trending" to match the repo's actual update cadence.

---

## [2026-06-20]

### Added
- `patterns/architecture-patterns.md` — The 8 canonical agent architecture patterns (ReAct, Reflexion, Supervisor–Worker, Role-Based Team, Debate, Verifier–Critic, Graph-Based, Swarm) with decision matrix, framework support matrix, production composition guide, and common failure modes

---

## [2026-06-09]

### Added
- Claude Fable 5 to Trending This Week and Agentic Stack (Layer 3: Agents)
- Skills.sh to Trending This Week and Agentic Stack (Layer 3: Agents)
- ADR-004: Why Fable 5 for long-running agentic tasks
- `patterns/` folder with cost-routing pattern

### Changed
- Updated Key Stats section date reference

---

## [2026-05-28]

### Added
- Claude Opus 4.8 Dynamic Workflows reference
- LiteParse v2 to reading list
- OpenSandbox to Guardrails Layer
- Obsidian Second Brain to reading list

---

## [2026-05-16]

### Added
- Mirage virtual filesystem to Trending + Tool Layer
- Deep Agents (LangChain) to Trending
- Hermes Agent to Trending
- CodeGraph MCP server to Trending + Tool Layer
- Second-Me to Trending + Agent Layer
- Framework comparison: CrewAI vs AutoGen vs LangGraph vs OpenAI SDK vs Mastra
- Ollama quickstart (`multi_agent_pipeline_ollama.py`)

---

## [2026-05-15]

### Added
- Initial release
- 4-layer architecture (Orchestration → Agents → Tools → Guardrails)
- Quickstart multi-agent pipeline (Planner → Executor → Validator)
- 5 production agent prompts
- 3 Architecture Decision Records
- Pre-launch checklist
- Mermaid diagrams
- Reading list (papers, reports, talks)
- Landing page at deeplyagentic.com
