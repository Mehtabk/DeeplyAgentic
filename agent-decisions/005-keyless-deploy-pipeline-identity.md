# ADR-005: Deploy Agents with Pipeline-Bound Identity, Not Runner-Held Keys

## Status
Accepted

## Context
A production agent has to call models and tools from inside a hosted runtime
(a CI pipeline, a managed agent runtime). The naive path is to hand the runner
a long-lived API key or static credential and let it authenticate. That key then
lives in the runner's environment, leaks into logs and forks, and never expires.

We validated the alternative on two independent hosting stacks in October 2026:
- **AWS Bedrock AgentCore** — deploy-by-push, identity minted for the pipeline.
- **Azure AI Foundry (Hosted Agent / Responses API)** — `DefaultAzureCredential`
  over Entra ID, no API key in the project at all.

The question: where should the credential live, and what should authenticate the
deploy?

## Decision
Bind the credential to the **pipeline identity**, not to the runner or the code.
The agent authenticates as a short-lived, scoped identity issued at deploy time;
no static API key is stored in the repo, the `.env`, or the runner's environment.

## Rationale
- **Nothing to leak.** There is no long-lived secret in the repo or the runner,
  so a fork, a log line, or a compromised build step exposes nothing reusable.
- **Short-lived by construction.** The identity is minted per deploy and expires
  on its own — the opposite of a static key that stays valid until someone
  remembers to rotate it.
- **Scoped to the job.** The pipeline identity carries exactly the permissions the
  deploy needs, so the blast radius of a compromise is bounded.
- **Same shape on both clouds.** AWS AgentCore and Azure Foundry differ in the
  mechanics, but the principle is identical: the deploy proves *who the pipeline
  is*, not *what key it holds*. The agent code is unchanged; only the credential
  origin moves.

## Consequences
**Positive:**
- No secret rotation chore, no key-in-repo incident class.
- Portable mental model across AWS and Azure — the architecture travels even when
  the vendor does not.

**Trade-offs:**
- Requires the hosting platform to support an issued identity (both AgentCore and
  Foundry do; a bare container may not).
- First-time setup is more involved than pasting a key — the payoff is that there
  is no key to manage afterward.

## Related
- ADR-002 (MCP for tools) — tool access is likewise brokered, not hard-wired.
- The Guardrails Layer principle: security is a property of the system's design,
  not a secret bolted onto the runner.
