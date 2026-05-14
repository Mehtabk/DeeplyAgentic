# Agent Architecture Decision Records

> Document your agent system design decisions. Like ADRs, but for AI agents.

When building agent systems, you make dozens of architectural decisions:
- Which tasks get their own agent vs. stay in one?
- When should an agent escalate vs. retry?
- How much autonomy does each agent get?

Document them here so your team (and future you) understands why.

---

## Template

Use this template for each decision:

```markdown
# ADR-[NUMBER]: [Title]

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
What is the situation that requires a decision?

## Decision
What did we decide?

## Consequences
What are the trade-offs?

## Alternatives Considered
What else did we evaluate?
```

---

## Example Decisions

| # | Decision | Status |
|---|----------|--------|
| 1 | [Separate Planner and Executor agents](./001-separate-planner-executor.md) | Accepted |
| 2 | [Use MCP for all tool connections](./002-mcp-for-tools.md) | Accepted |
| 3 | [Validator runs before every user-facing output](./003-validator-before-output.md) | Accepted |

---

## When to Write an ADR

- Adding a new agent to the system
- Changing how agents communicate
- Modifying escalation or retry logic
- Choosing between frameworks or protocols
- Setting autonomy boundaries
