# Phase 13: Tools & Protocols

> The interfaces between AI and the real world.

## Why this phase exists

A language model, on its own, only produces text. It cannot check the weather,
query a database, book a flight, or call another program. Everything useful an AI
system does in the real world happens through an *interface* — a contract that lets
the model request an action and lets your code carry it out and report back.

This phase is about those interfaces. You'll learn tool use and function calling
(how a model asks to run code), structured output (how you get reliable JSON back
instead of a paragraph you have to parse), and MCP — the Model Context Protocol —
which standardizes how any AI client talks to any tool server so integrations stop
being one-off glue. From there it widens out to agent-to-agent protocols, tracing,
routing, security, and the production plumbing that holds a real tool ecosystem
together.

If Phase 11 taught you to talk to a model, this phase teaches the model to reach
out and touch the world.

## What you need first

- **Phase 11 (LLM Engineering)** — you should be comfortable calling a completion
  API and reading its response. That's the foundation every lesson here builds on.
- **Phase 0 (Setup & Tooling)**, especially **APIs & Keys** — several lessons make
  real calls to OpenAI, Anthropic, and Gemini, so you'll want working keys.

You don't need to have memorized any provider's SDK. Each lesson shows the exact
request and response shapes, and the early lessons deliberately build the loop from
scratch before pointing you at the library everyone actually uses.

## What you'll be able to do after this phase

- Run the full tool-call loop against OpenAI, Anthropic, and Gemini — and port code
  between them without it breaking
- Get reliable, schema-valid structured output instead of hoping the model returns
  clean JSON
- Build and run your own MCP server *and* client, covering tools, resources, and
  prompts
- Choose and configure the right MCP transport, auth (OAuth 2.1), and gateway for a
  production deployment
- Wire agents together with the A2A protocol and trace every tool call end-to-end
  with OpenTelemetry
- Recognize and defend against tool-poisoning and other MCP-specific security attacks

## The lessons

Work through them in order — the MCP chapter (06 onward) assumes the tool-calling
foundation from 01-05, and the later lessons build directly on the MCP server and
client you write early on.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **The Tool Interface — Why Agents Need Structured I/O** | Names the four-step loop that every tool-calling stack — function calling, MCP, A2A — is really just a different encoding of. | ~45 min |
| 02 | **Function Calling Deep Dive — OpenAI, Anthropic, Gemini** | The three providers share one loop but diverge on everything else; this diffs them so your code survives a port. | ~75 min |
| 03 | **Parallel Tool Calls and Streaming with Tools** | Run independent tool calls at once and reassemble streamed arguments — with the id-correlation trap called out. | ~75 min |
| 04 | **Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding** | Constrained decoding closes the 5-15% gap where "please return JSON" quietly fails. | ~75 min |
| 05 | **Tool Schema Design — Naming, Descriptions, Parameter Constraints** | Naming and descriptions swing tool-selection accuracy by 10-20 points; this names the rules. | ~45 min |
| 06 | **MCP Fundamentals — Primitives, Lifecycle, JSON-RPC Base** | The six primitives, three-phase lifecycle, and wire format that make the rest of the MCP chapter just reading. | ~45 min |
| 07 | **Building an MCP Server — Python + TypeScript SDKs** | Builds a real server — tools, resources, prompts, capability negotiation, structured errors — end to end. | ~75 min |
| 08 | **Building an MCP Client — Discovery, Invocation, Session Management** | The hard orchestration lives on the client: spawning, negotiation, and merging many servers into one tool namespace. | ~75 min |
| 09 | **MCP Transports — stdio vs Streamable HTTP vs SSE Migration** | Picking the right transport buys a remote-hostable server; picking wrong costs a migration. | ~45 min |
| 10 | **MCP Resources and Prompts — Context Exposure Beyond Tools** | The two under-used server primitives: expose data for reading and reusable templates as slash-commands. | ~45 min |
| 11 | **MCP Sampling — Server-Requested LLM Completions and Agent Loops** | Lets a server ask the client's LLM to decide, enabling server-hosted agent loops without owning model credentials. | ~75 min |
| 12 | **Roots and Elicitation — Scoping and Mid-Flight User Input** | Two client primitives that fix hard-coded paths and under-specified tool arguments. | ~45 min |
| 13 | **Async Tasks (SEP-1686) — Call-Now, Fetch-Later for Long-Running Work** | A Tasks primitive for work that takes minutes to hours, without dropped connections or blocked UIs. | ~75 min |
| 14 | **MCP Apps — Interactive UI Resources via `ui://`** | Return sandboxed interactive HTML — dashboards, forms, maps — rendered inline in the host. | ~75 min |
| 15 | **MCP Security I — Tool Poisoning, Rug Pulls, Cross-Server Shadowing** | Malicious tool descriptions hit >70% attack success; this names the classes and builds a CI detector. | ~45 min |
| 16 | **MCP Security II — OAuth 2.1, Resource Indicators, Incremental Scopes** | Remote servers need authorization; this implements the step-up OAuth flow as a state machine. | ~75 min |
| 17 | **MCP Gateways and Registries — Enterprise Control Planes** | Where auth, RBAC, audit, and rate limiting centralize behind a single merged MCP endpoint. | ~45 min |
| 18 | **MCP Auth in Production — Enrollment, JWKS Refresh, Audience-Pinned Tokens** | Models the full production auth surface across three roles, tracing every hop to a validated tool call. | ~90 min |
| 19 | **A2A — Agent-to-Agent Protocol** | Where MCP is agent-to-tool, A2A lets opaque agents on different frameworks collaborate. | ~75 min |
| 20 | **OpenTelemetry GenAI — Tracing Tool Calls End-to-End** | One trace across agents, tools, and MCP servers using the 2026 GenAI semantic conventions. | ~75 min |
| 21 | **LLM Routing Layer — LiteLLM, OpenRouter, Portkey** | One API surface with retries, failover, and cost tracking to escape provider lock-in. | ~45 min |
| 22 | **Skills and Agent SDKs — Anthropic Skills, AGENTS.md, OpenAI Apps SDK** | MCP says what tools exist; Skills say how to do a task — and how both layer together. | ~45 min |
| 23 | **Capstone — Build a Complete Tool Ecosystem** | Wires every piece into one production-shaped system you can defend end to end. | ~120 min |

## How each lesson is built

Every lesson in this whole curriculum follows the same rhythm, so once you learn the
shape you can move fast:

- **The Problem** — why this exists, in plain terms
- **The Concept** — the idea, usually with a diagram
- **Build It** — you write/run the code yourself, step by step
- **Use It** — how it's done for real (the library everyone actually uses)
- **Exercises** — check you actually got it

You're never expected to already know the answer. Read → run → verify → move on.

## Suggested path

Go straight down 01 → 23. The lessons split into two halves that build on each
other: **01-05** give you the tool-calling and structured-output foundation across
all three frontier providers, and **06 onward** is the MCP chapter plus the wider
protocol, security, and production topics.

If you're short on time on a first pass, the **Learn** lessons (01, 05, 06, 09, 15,
17, 21, 22) give you the concepts, and you can return to the longer **Build**
lessons when you need the working code. But do lessons 07 and 08 either way — almost
everything after them reuses the MCP server and client you build there. Finish with
the capstone (23), which assumes all of it.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
