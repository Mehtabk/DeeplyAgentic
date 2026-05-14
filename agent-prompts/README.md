# Agent Prompts

> Production-ready prompts for AI agent systems — organized by role.

These aren't chat prompts. They're system instructions for agents that plan, execute, validate, and orchestrate.

## Prompt Categories

| Role | Description | File |
|------|-------------|------|
| Planner | Decomposes goals into executable steps | [planner.md](./planner.md) |
| Executor | Takes actions, calls tools, writes code | [executor.md](./executor.md) |
| Validator | Reviews outputs, checks quality, flags issues | [validator.md](./validator.md) |
| Orchestrator | Routes tasks, manages agent coordination | [orchestrator.md](./orchestrator.md) |
| Summarizer | Condenses meetings, threads, docs into briefs | [summarizer.md](./summarizer.md) |

## How to Use

1. Pick the role your agent needs
2. Copy the system prompt
3. Adapt the `[CONTEXT]` placeholders to your domain
4. Deploy as system instructions in your agent framework

## Contributing

Submit a PR with new prompts. Follow the template format in each file.
