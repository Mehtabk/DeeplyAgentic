# Cost-Routing Pattern

> Route tasks to the cheapest model that can handle them. Escalate to frontier models only when complexity demands it.

## The Problem

Running every agent task through your most capable model is expensive and slow. Most tasks don't need frontier intelligence:

- Simple lookups → fast/cheap model
- Code generation → mid-tier model
- Multi-hour autonomous work → frontier model

Without routing, you're paying Fable 5 prices for tasks Haiku could handle.

## The Pattern

```
┌─────────────────────────────────────────────┐
│           Complexity Classifier             │
│  (token count, step count, domain, risk)    │
└─────────┬──────────────┬──────────────┬─────┘
          │              │              │
          ▼              ▼              ▼
    ┌──────────┐  ┌──────────────┐  ┌──────────┐
    │  Tier 1  │  │   Tier 2     │  │  Tier 3  │
    │  Haiku   │  │  Opus 4.8    │  │ Fable 5  │
    │  $0.25/M │  │  $3/M input  │  │ $10/M    │
    └──────────┘  └──────────────┘  └──────────┘
     Simple Q&A    Code gen, review   Multi-hour
     Summaries     Analysis           Migrations
     Formatting    Planning           Research
```

## Routing Criteria

| Signal | Tier 1 (Cheap) | Tier 2 (Mid) | Tier 3 (Frontier) |
|--------|----------------|--------------|-------------------|
| Estimated steps | 1-3 | 4-15 | 15+ |
| Context needed | < 10K tokens | 10K-100K | 100K+ |
| Domain | General | Specialized | Cross-domain |
| Risk if wrong | Low (retry is cheap) | Medium | High (expensive to undo) |
| Autonomy needed | None | Some | Full (multi-hour) |

## Implementation

```python
def route_task(task: Task) -> str:
    """Route to cheapest capable model."""
    
    if task.estimated_steps <= 3 and task.context_tokens < 10_000:
        return "claude-haiku"
    
    if task.estimated_steps <= 15 and task.context_tokens < 100_000:
        return "claude-opus-4.8"
    
    # Complex, long-running, or high-risk
    return "claude-fable-5"
```

## Fallback Strategy

If a lower-tier model fails or produces low-confidence output:

1. Log the failure reason
2. Escalate to next tier with the original context + failure context
3. Track escalation rate — if a task type escalates >30% of the time, promote it permanently

## Cost Impact

Based on a typical week running our Planner → Executor → Validator pipeline:

| Without routing | With routing | Savings |
|-----------------|--------------|---------|
| All Fable 5: ~$84/week | Mixed: ~$23/week | **73% reduction** |

Most tasks are Tier 1 or 2. Frontier intelligence is only needed ~15% of the time.

## When NOT to Route

- Safety-critical tasks → always use the most capable model
- Tasks where retrying is more expensive than overpaying upfront
- When latency matters more than cost (fast mode on Opus 4.8 is 2.5x faster)

## Related

- [ADR-004: Why Fable 5 for long-running tasks](../agent-decisions/004-fable5-for-long-running-tasks.md)
- [ADR-001: Separate Planner and Executor](../agent-decisions/001-separate-planner-executor.md)
