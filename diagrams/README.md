# Agent Architecture Diagrams

> Copy-paste Mermaid diagrams for agent system design. Use in docs, PRs, and presentations.

## Multi-Agent Pipeline

```mermaid
flowchart LR
    User([User]) --> Orchestrator
    Orchestrator --> Planner
    Planner --> Executor
    Executor --> Validator
    Validator -->|PASS| User
    Validator -->|FAIL| Executor
```

## The 4-Layer Stack

```mermaid
flowchart TB
    subgraph Orchestration["\ud83c\udfaf Orchestration Layer"]
        Router[Router] --> Coordinator[Coordinator]
    end
    subgraph Agents["\ud83e\udde0 Agent Layer"]
        A1[Planner] --> A2[Executor]
        A2 --> A3[Validator]
    end
    subgraph Tools["\ud83d\udd0c Tool Layer - MCP"]
        T1[APIs] --> T2[Databases]
        T2 --> T3[External Services]
    end
    subgraph Guardrails["\ud83d\udee1\ufe0f Guardrails"]
        G1[Input Validation] --> G2[Output Checks]
        G2 --> G3[Human Escalation]
    end
    Orchestration --> Agents
    Agents --> Tools
    Guardrails -.->|enforces| Orchestration
    Guardrails -.->|enforces| Agents
    Guardrails -.->|enforces| Tools
```

## Agent Decision Flow

```mermaid
flowchart TD
    Task([New Task]) --> Ambiguous{Is it ambiguous?}
    Ambiguous -->|Yes| Planner[Send to Planner]
    Ambiguous -->|No| Executor[Send to Executor]
    Planner --> Executor
    Executor --> Success{Success?}
    Success -->|Yes| Validator[Send to Validator]
    Success -->|No| Retry{Retried?}
    Retry -->|No| Executor
    Retry -->|Yes| Escalate[Escalate to Human]
    Validator --> Quality{Quality OK?}
    Quality -->|PASS| Deliver([Deliver to User])
    Quality -->|FAIL| Executor
```

## Agentic RAG Flow

```mermaid
flowchart LR
    Query([User Query]) --> Retrieve[Retrieve Context]
    Retrieve --> Plan[Plan Steps]
    Plan --> Execute[Execute]
    Execute --> Verify[Verify Output]
    Verify --> Memory[(Update Memory)]
    Memory --> Adapt[Adapt for Future]
    Adapt -.->|improves| Retrieve
    Verify -->|verified| Response([Response])
```

## Multi-Agent Orchestration (Fan-out/Fan-in)

```mermaid
flowchart TD
    Task([Complex Task]) --> Orchestrator
    Orchestrator --> A1[Agent: Research]
    Orchestrator --> A2[Agent: Code]
    Orchestrator --> A3[Agent: Review]
    A1 --> Collect[Collect Results]
    A2 --> Collect
    A3 --> Collect
    Collect --> Synthesize[Synthesize]
    Synthesize --> Output([Final Output])
```

---

## How to Use

These diagrams render natively on GitHub, Notion, and most documentation tools.

To use in your own docs:
1. Copy the mermaid code block
2. Paste into any markdown file
3. It renders automatically on GitHub

For presentations, use [mermaid.live](https://mermaid.live) to export as PNG/SVG.
