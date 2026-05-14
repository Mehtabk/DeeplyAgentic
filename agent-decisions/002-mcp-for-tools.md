# ADR-002: Use MCP for All Tool Connections

## Status
Accepted

## Context
Agents need to connect to external tools (APIs, databases, file systems). Options:
- Hardcode tool calls per agent
- Use function calling with custom schemas
- Use Model Context Protocol (MCP) as a standard interface

## Decision
All tool connections go through MCP servers. Agents discover tools dynamically at runtime via the MCP handshake.

## Consequences
**Positive:**
- Agents are tool-agnostic — swap tools without changing agent code
- New tools can be added without redeploying agents
- Standardized interface reduces integration bugs
- Community MCP servers available for common tools

**Negative:**
- MCP adds a layer of abstraction (slight latency)
- Not all tools have MCP servers yet
- Debugging requires understanding the MCP protocol

## Alternatives Considered
- **Direct API calls**: Faster but tightly coupled
- **LangChain tools**: Mature but vendor-locked to LangChain ecosystem
