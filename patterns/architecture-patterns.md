# Agent Architecture Patterns

> 8 canonical patterns for building production agent systems. Choose the pattern first, then the framework.

## The 8 Patterns at a Glance

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT ARCHITECTURE PATTERNS                    │
├────────────────────┬────────────────────────────────────────────┤
│  SINGLE-AGENT      │  COLLABORATIVE MULTI-AGENT                 │
│                    │                                            │
│  1. ReAct          │  3. Supervisor–Worker                      │
│  2. Reflexion      │  4. Role-Based Team                        │
├────────────────────┼────────────────────────────────────────────┤
│  COMPETITIVE       │  ORCHESTRATION TOPOLOGY                    │
│                    │                                            │
│  5. Debate         │  7. Graph-Based                            │
│  6. Verifier–Critic│  8. Swarm                                  │
└────────────────────┴────────────────────────────────────────────┘
```

## Pattern 1 — ReAct (Reasoning + Acting)

Think → Act → Observe → Repeat.

**Best for:** Tool use, search, Q&A with external data.
**Failure mode:** Infinite loops when reasoning doesn't converge. Always set a max iteration limit.
**Frameworks:** LangGraph, OpenAI Agents SDK, LangChain.

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│  Reason  │────▶│   Act    │────▶│ Observe  │
└──────────┘     └──────────┘     └──────────┘
      ▲                                  │
      └──────────────────────────────────┘
```

## Pattern 2 — Reflexion (Self-Critique Loop)

After each output, the agent critiques its own reasoning and refines the answer.

**Best for:** Tasks where factual accuracy is critical — legal, financial, code review.
**Failure mode:** Expensive compute. Set max reflection iterations (2–3 is usually enough).
**Frameworks:** LangGraph (native), AutoGen.

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ Generate │────▶│ Critique │────▶│  Refine  │
└──────────┘     └──────────┘     └──────────┘
                       │                  │
                       └──── if pass ────▶ OUTPUT
```

## Pattern 3 — Supervisor–Worker (Hierarchical)

A supervisor agent decomposes tasks and delegates to specialized workers.

**Best for:** Complex multi-step workflows, research pipelines, software development.
**Failure mode:** Supervisor bottleneck — if it fails, everything fails.
**Frameworks:** LangGraph (subgraphs), CrewAI, AutoGen.

```
                ┌──────────────┐
                │  Supervisor  │
                └──┬───┬───┬──┘
                   │   │   │
          ┌────────┘   │   └────────┐
          ▼            ▼            ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ Worker A │ │ Worker B │ │ Worker C │
    │ Research │ │  Code    │ │  Review  │
    └──────────┘ └──────────┘ └──────────┘
```

## Pattern 4 — Role-Based Team

Agents are assigned distinct roles and collaborate on a shared workflow.

**Best for:** Content production, customer support pipelines, analysis workflows.
**Failure mode:** Role overlap → duplicate work. Role gaps → dropped tasks.
**Frameworks:** CrewAI (primary strength), Semantic Kernel.

## Pattern 5 — Debate (Multi-Agent Verification)

Two or more agents produce competing outputs. A judge selects the best reasoning path.

**Best for:** High-stakes decisions, factual verification, legal/medical reasoning.
**Failure mode:** Debate without clear evaluation criteria is inconclusive.
**Frameworks:** AutoGen (group chat mode).

## Pattern 6 — Verifier–Critic

A dedicated Critic agent reviews output against predefined quality criteria. Stricter than Reflexion because the Critic is a separate agent.

**Best for:** Code generation (Critic checks for bugs), financial outputs (Critic validates calculations).
**Failure mode:** Vague criteria → weak criticism. Be explicit about what "good" means.
**Frameworks:** CrewAI (task chains), LangGraph.

## Pattern 7 — Graph-Based Orchestration

The workflow is a directed graph. Each node is a reasoning step. Decision paths branch based on results. Every step is auditable.

**Best for:** Enterprise workflows, compliance-sensitive automation, debugging-heavy deployments.
**Failure mode:** Graph complexity grows fast. Keep nodes focused.
**Frameworks:** LangGraph (primary strength), Microsoft Agent Framework.

```
    ┌───────┐     ┌───────┐
    │ Parse │────▶│ Route │
    └───────┘     └───┬───┘
                      │
            ┌─────────┼─────────┐
            ▼         ▼         ▼
       ┌────────┐ ┌────────┐ ┌────────┐
       │ Simple │ │  Code  │ │Complex │
       │  Path  │ │  Path  │ │  Path  │
       └───┬────┘ └───┬────┘ └───┬────┘
           └──────────┬──────────┘
                      ▼
               ┌────────────┐
               │  Validate  │
               └────────────┘
```

## Pattern 8 — Swarm

Agents self-organize without a central supervisor. Each agent decides which agent to hand off to based on context.

**Best for:** Dynamic, exploratory tasks where the workflow can't be predefined.
**Failure mode:** Hard to debug, trace, or govern at scale.
**Frameworks:** OpenAI Agents SDK (Swarm reference), AutoGen.

## Decision Matrix — Which Pattern to Use

| Your situation | Pattern |
|----------------|---------|
| Single task, needs external tools | ReAct |
| Accuracy is critical, errors are costly | Reflexion or Verifier–Critic |
| Complex multi-step task, one team | Supervisor–Worker |
| Defined roles, collaborative pipeline | Role-Based Team |
| High-stakes decision, need verification | Debate |
| Enterprise workflow, needs audit trail | Graph-Based |
| Dynamic, open-ended exploration | Swarm |
| Production at scale, governance required | Graph + Verifier–Critic |

## Framework Support Matrix

| Pattern | LangGraph | CrewAI | AutoGen | OpenAI SDK |
|---------|-----------|--------|---------|------------|
| ReAct | ✅ Strong | ✅ | ✅ | ✅ Strong |
| Reflexion | ✅ Native | ⚠️ | ✅ | ⚠️ |
| Supervisor–Worker | ✅ | ✅ Strong | ✅ Strong | ✅ |
| Role-Based Team | ⚠️ | ✅ Primary | ✅ | ⚠️ |
| Debate | ⚠️ | ⚠️ | ✅ Strong | ⚠️ |
| Verifier–Critic | ✅ | ✅ | ✅ | ⚠️ |
| Graph Orchestration | ✅ Primary | ⚠️ | ⚠️ | ⚠️ |
| Swarm | ⚠️ | ⚠️ | ✅ | ✅ Native |

✅ = Strong native support | ⚠️ = Partial / requires custom work

## Production Composition

Most production systems combine 2–3 patterns:

```
Graph-Based backbone (Pattern 7)
  └── Supervisor–Worker for task delegation (Pattern 3)
       └── Reflexion at the agent level (Pattern 2)
            └── Verifier–Critic before output (Pattern 6)
```

This is the architecture behind the DeeplyAgentic stack:
- **Orchestration** → Graph-Based (Pattern 7)
- **Agents** → Supervisor–Worker (Pattern 3) + Reflexion (Pattern 2)
- **Tools** → ReAct loop for tool use (Pattern 1)
- **Guardrails** → Verifier–Critic (Pattern 6)

## Common Failure Modes

| Failure | Root Cause | Fix |
|---------|-----------|-----|
| Agent loops forever | No max iteration limit on ReAct | Set `max_steps=10` |
| Hallucinations propagate | No Reflexion or Critic layer | Add Pattern 2 or 6 |
| Wrong pattern for task | Using ReAct for multi-agent work | Upgrade to Pattern 3 |
| Can't debug failures | No observability in orchestration | Use Graph-Based (Pattern 7) |
| Governance gaps | Swarm without guardrails | Add Verifier–Critic gate |

## Related

- [Cost Routing Pattern](./cost-routing.md) — route to cheapest capable model
- [ADR-001: Separate Planner and Executor](../agent-decisions/001-separate-planner-executor.md)
- [ADR-003: Validator Before Output](../agent-decisions/003-validator-before-output.md)
- [The Agentic Stack](../the-agentic-stack/README.md)
