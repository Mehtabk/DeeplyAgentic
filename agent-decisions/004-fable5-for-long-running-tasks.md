# ADR-004: Why Claude Fable 5 for Long-Running Agentic Tasks

## Status
Accepted

## Context
Our multi-agent pipeline (Planner → Executor → Validator) needs a model for tasks that run autonomously for hours — codebase migrations, multi-file refactors, research synthesis. Requirements:
- Maintain coherence across 100k+ token sessions
- Self-correct without human intervention
- Manage parallel sub-tasks
- Stay within cost bounds

Available options (June 2026): Claude Fable 5, Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro.

## Decision
Use **Claude Fable 5** for long-running, complex agent tasks. Use **Opus 4.8** for shorter tasks and as the fallback when Fable 5's safety classifiers trigger.

## Rationale

**Performance on long tasks:**
- Fable 5's advantage grows with task complexity and duration
- Maintains focus across millions of tokens in long-running sessions
- Persistent memory improves output quality 3x more than it does for Opus 4.8

**Autonomous capabilities:**
- Plans work and spawns parallel subagents natively (Dynamic Workflows)
- Stripe reported: 50M-line codebase migration in 1 day (vs 2 months by a team)
- Vision-only reasoning without scaffolding (beat Pokémon FireRed start-to-finish)

**Cost efficiency:**
- $10/M input, $50/M output — less than half of Mythos Preview
- Higher per-token cost than Opus 4.8, but fewer total tokens for complex tasks due to less backtracking

**Built-in guardrails:**
- Safety classifiers route sensitive queries to Opus 4.8 automatically
- Aligns with our Guardrails Layer principle: constraints baked in, not bolted on

## Consequences
**Positive:**
- Fewer failed runs on complex tasks → less token waste on retries
- Dynamic Workflows removes need for custom sub-agent orchestration code
- Built-in fallback to Opus 4.8 means graceful degradation without extra logic

**Negative:**
- Higher per-token cost than Opus 4.8 for simple tasks (overkill)
- Safety classifiers occasionally catch harmless requests (~5% of sessions)
- Vendor lock-in to Anthropic's model routing decisions

## Alternatives Considered
- **Opus 4.8 for everything**: Cheaper, but loses coherence on 2+ hour tasks. Better for short, focused agent steps.
- **GPT-5.5**: Leads on terminal-coding benchmarks, but weaker on SWE-Bench Pro (69.2% vs Fable 5). Less suited for autonomous multi-hour sessions.
- **Gemini 3.1 Pro**: Strong on multimodal, but behind both Claude models on agentic coding evaluations.
- **Cost-routing hybrid**: Route simple tasks to Opus 4.8, complex tasks to Fable 5. This is actually what we do — see `patterns/cost-routing.md`.
