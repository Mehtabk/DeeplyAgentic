# ADR-006: Grounding Is a Tool-Design Choice; Safety Is a Gate, Not a Prompt

## Status
Accepted

## Context
Two failure modes recur in agent projects, and both are usually blamed on the
model when they are actually architecture problems:

1. **Hallucination** — the agent answers fluently but invents facts.
2. **Prompt injection** — a crafted input talks the model into an action it
   should not take (e.g. a write).

We tested both deterministically while building the same information-assistant
agent on two stacks (AWS Bedrock AgentCore and Azure AI Foundry, Oct 2026). The
results were identical across stacks, which is why they are recorded as a decision
rather than an anecdote.

## Decision
Treat **grounding as a property of the tool set**, not the model, and treat
**safety as a capability you remove or gate**, not an instruction you write.

## Rationale

**Grounding is the tool list.**
With only a review tool bound, the agent asked "which facilities does this entity
have?" *fabricated* concrete facilities from a bare numeric score. Binding the
correct data tool (the real domain data source) replaced the fiction with named,
verifiable facts. The model did not change — the available tools did. A fluent
answer is not a grounded one; grounding is decided when you choose which tools the
agent can call.

**Safety is a gate, not a sentence.**
A prompt instruction ("never write without approval") can be argued against by a
crafted input, because the instruction lives exactly where the model reads — and
can be overridden. A human-in-the-loop *gate* in the code path blocks the write
even when the model is fully compromised. Proven deterministically: with no gate,
a malicious prompt produced a write (created: 1); with the HITL gate on, the same
prompt produced none (created: 0). A model resisting an injection is luck. The
gate is security.

## Consequences
**Positive:**
- Reframes two "model quality" complaints as architecture decisions the team
  controls — tool selection and a code-level gate.
- Portable: holds identically on AWS and Azure, so it is a design rule, not a
  vendor behavior.

**Trade-offs:**
- A gate adds a human step to sensitive actions by design — that latency is the
  security, not a bug to optimize away.
- Requires discipline to keep safety-critical constraints in code, never only in
  the prompt.

## Related
- ADR-003 (Validator before output) — the same instinct, applied to correctness.
- The Guardrails Layer: constraints baked in, not bolted on.
