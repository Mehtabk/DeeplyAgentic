# ADR-003: Validator Runs Before Every User-Facing Output

## Status
Accepted

## Context
Agent outputs can contain:
- Hallucinated facts
- Incomplete responses (missed steps)
- Inconsistencies with prior context
- Quality issues (unclear, unstructured)

Shipping unvalidated output erodes user trust.

## Decision
Every output that reaches the user must pass through the Validator agent first. No exceptions.

## Consequences
**Positive:**
- Catches errors before they reach users
- Builds systematic quality into the pipeline
- Validator can be tuned independently of other agents
- Creates an audit trail of quality decisions

**Negative:**
- Adds latency (one extra LLM call)
- Validator can be overly conservative (false FAILs)
- Increases token cost by ~20-30%

## Alternatives Considered
- **Validate only high-stakes outputs**: Saves cost but inconsistent quality
- **Rule-based checks only**: Fast but misses semantic issues
- **User feedback loop**: Good supplement but not a replacement for pre-delivery checks
