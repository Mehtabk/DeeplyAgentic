# ADR-001: Separate Planner and Executor Agents

## Status
Accepted

## Context
We need to handle complex, multi-step tasks. A single agent trying to plan AND execute tends to:
- Lose track of the overall goal mid-execution
- Skip steps when context gets long
- Mix planning reasoning with execution output

## Decision
Split into two dedicated agents:
- **Planner**: Decomposes goals into steps. Never executes.
- **Executor**: Follows plans step-by-step. Never modifies the plan without escalating.

## Consequences
**Positive:**
- Each agent has a focused, testable responsibility
- Plans can be reviewed before execution
- Failures are easier to diagnose (was it a bad plan or bad execution?)

**Negative:**
- Adds one extra LLM call per task
- Requires an orchestrator to manage handoffs
- Simple tasks get slightly over-engineered

## Alternatives Considered
- **Single agent with planning prompt**: Simpler but unreliable for 5+ step tasks
- **ReAct loop**: Good for exploration, but less predictable for production workflows
