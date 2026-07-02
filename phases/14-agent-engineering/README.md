# Phase 14: Agent Engineering

> The core of modern AI engineering. Build agents from first principles.

## Why this phase exists

An LLM on its own is autocomplete: you send text, you get text back. It can't read
a file, run a query, open a browser, or check whether its own answer is true. An
*agent* is the thing that closes that gap — a loop that lets the model pause, call a
tool, read the result, and keep going until the job is done.

This is the heart of the whole curriculum. Every agent you've heard of — Claude Code,
Cursor, Devin, Operator — is a variant of the same small loop, wrapped in memory,
planning, and verification. This phase builds that loop from scratch, then layers on
every technique that turns a demo into something you'd actually trust in production.

You won't just call a framework. You'll implement the patterns the frameworks are made
of, so that when one breaks (and they break), you know exactly what's happening
underneath and how to fix it.

## What you need first

This phase assumes two earlier phases are behind you:

- **Phase 11 (LLM Engineering)** — you're comfortable calling a model, shaping prompts,
  and reasoning about tokens and context windows.
- **Phase 13 (Tools and Protocols)** — you understand function calling and how a model
  hands work off to external tools.

If you have those, you're ready. If a specific idea feels shaky, that's normal — this
is the deepest phase in the curriculum, and every lesson starts from the problem it
solves before it shows you any code. Read → build → verify → move on.

## What you'll be able to do after this phase

- Build an agent loop from scratch and extend it with planning, reflection, and search
- Give an agent durable memory that survives past a single context window
- Choose the right framework for a job (LangGraph, AutoGen, CrewAI, the OpenAI and
  Claude Agent SDKs) and know what each one is really doing underneath
- Evaluate agents against real benchmarks and instrument them with proper observability
- Defend against prompt injection and the common ways agents fail in the wild
- Assemble a reusable "agent workbench" that makes any repo safe for an agent to work in

## The lessons

Work through them in order — the loop in lesson 01 is the foundation everything else
builds on. The phase moves from core patterns, to memory and planning, to frameworks,
to evaluation and safety, and ends with a hands-on mini-track on making agents reliable
on real repos.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **The Agent Loop: Observe, Think, Act** | The one loop every agent is built on. Learn it cold before any framework. | ~60 min |
| 02 | **ReWOO and Plan-and-Execute: Decoupled Planning** | Plan up front, then execute — 5x fewer tokens and clearer failure modes than interleaving. | ~60 min |
| 03 | **Reflexion: Verbal Reinforcement Learning** | Let an agent learn from failure in plain language, with no gradient step. | ~60 min |
| 04 | **Tree of Thoughts and LATS: Deliberate Search** | Turn reasoning into a searchable tree so the agent can backtrack instead of committing to one bad chain. | ~75 min |
| 05 | **Self-Refine and CRITIC: Iterative Output Improvement** | One model as generator, critic, and reviser — the evaluator-optimizer pattern shipped in every framework. | ~60 min |
| 06 | **Tool Use and Function Calling** | How agents actually reach the outside world, and what's still unsolved (memory, long tool chains). | ~60 min |
| 07 | **Memory: Virtual Context and MemGPT** | Page information between finite context and unlimited external storage, like an OS manages RAM. | ~75 min |
| 08 | **Memory Blocks and Sleep-Time Compute (Letta)** | Editable memory blocks plus a background agent that consolidates memory while the main one is idle. | ~75 min |
| 09 | **Hybrid Memory: Vector + Graph + KV (Mem0)** | Fuse three memory stores — semantic, fact, and relational — into the 2026 production standard. | ~75 min |
| 10 | **Skill Libraries and Lifelong Learning (Voyager)** | Treat executable code as named, reusable skills an agent grows over time. | ~75 min |
| 11 | **Planning with HTN and Evolutionary Search** | When to use provably-correct symbolic planning versus machine-checkable evolutionary search. | ~75 min |
| 12 | **Anthropic's Workflow Patterns: Simple Over Complex** | Five workflow patterns that cover most cases — reach for an agent only when steps can't be predicted. | ~60 min |
| 13 | **LangGraph: Stateful Graphs and Durable Execution** | Model an agent as a checkpointed state machine you can resume from any failure. | ~75 min |
| 14 | **AutoGen v0.4: Actor Model and Agent Framework** | Async, event-driven agents with fault isolation and natural concurrency. | ~75 min |
| 15 | **CrewAI: Role-Based Crews and Flows** | Role-based multi-agent collaboration, plus the deterministic Flows you'd actually ship. | ~75 min |
| 16 | **OpenAI Agents SDK: Handoffs, Guardrails, Tracing** | A lightweight multi-agent SDK where handoffs are tools and tracing is on by default. | ~75 min |
| 17 | **Claude Agent SDK: Subagents and Session Store** | The library form of the Claude Code harness — subagents, hooks, and session parity. | ~75 min |
| 18 | **Agno and Mastra: Production Runtimes** | The Python and TypeScript production-runtime pairing for shipping agents at speed. | ~45 min |
| 19 | **Benchmarks: SWE-bench, GAIA, AgentBench** | The three benchmarks that anchor agent evaluation — and what they don't measure. | ~60 min |
| 20 | **Benchmarks: WebArena and OSWorld** | Web- and desktop-agent benchmarks, the human gap, and the failure modes that persist. | ~60 min |
| 21 | **Computer Use: Claude, OpenAI CUA, Gemini** | Vision-based agents that drive a screen, and why every pixel they see is untrusted input. | ~60 min |
| 22 | **Voice Agents: Pipecat and LiveKit** | Real-time voice pipelines and the sub-second latency targets production demands. | ~60 min |
| 23 | **OpenTelemetry GenAI Semantic Conventions** | The standard schema that makes agent traces mean the same thing across every vendor. | ~60 min |
| 24 | **Agent Observability: Langfuse, Phoenix, Opik** | The three open-source platforms for tracing, evals, and debugging agents in production. | ~45 min |
| 25 | **Multi-Agent Debate and Collaboration** | Multiple model instances critiquing each other to raise factuality and reasoning. | ~60 min |
| 26 | **Failure Modes: Why Agents Break** | The recurring ways agents fail — hallucinated actions, scope creep, cascading errors — and how to catch them. | ~60 min |
| 27 | **Prompt Injection and the PVE Defense** | The defining agent security problem: treat all retrieved content as arbitrary code. | ~75 min |
| 28 | **Orchestration Patterns: Supervisor, Swarm, Hierarchical** | The four multi-agent topologies, and when a single agent is still the right call. | ~60 min |
| 29 | **Production Runtimes: Queue, Event, Cron** | The six runtime shapes production agents run on — pick the shape before the framework. | ~60 min |
| 30 | **Eval-Driven Agent Development** | Evaluation isn't the last step; it's the outer loop that drives every other choice. | ~60 min |
| 31 | **Agent Workbench Engineering: Why Capable Models Still Fail** | A frontier model isn't enough — reliable agents need a workbench around them. | ~45 min |
| 32 | **The Minimal Agent Workbench** | The smallest useful workbench: an instructions router, a state file, and a task board. | ~45 min |
| 33 | **Agent Instructions as Executable Constraints** | Rewrite rules from prose wishes into constraints an agent can check at runtime. | ~50 min |
| 34 | **Repo Memory and Durable State** | Store agent state in versioned files so every session reads the same source of truth. | ~60 min |
| 35 | **Initialization Scripts for Agents** | Pay the cold-start tax once and write the answers into state instead of rediscovering them. | ~45 min |
| 36 | **Scope Contracts and Task Boundaries** | A per-task file that says where work begins, ends, and how to roll back if it spills. | ~50 min |
| 37 | **Runtime Feedback Loops** | Capture real command output so the agent reacts to facts, not to its own predictions. | ~50 min |
| 38 | **Verification Gates** | The agent doesn't get to mark its own work done — a gate answers whether the task actually is. | ~55 min |
| 39 | **Reviewer Agent: Separate Builder from Marker** | A second read-only loop grades the work, because the builder can't grade itself. | ~55 min |
| 40 | **Multi-Session Handoff** | Build the handoff packet on purpose so the next session is productive in its first minute. | ~50 min |
| 41 | **The Workbench on a Real Repo** | Run the same task prompt-only versus workbench-guided on a real app and let the numbers argue. | ~60 min |
| 42 | **Capstone: Ship a Reusable Agent Workbench Pack** | Compress the whole mini-track into a directory you can drop into any repo. | ~75 min |

## How each lesson is built

Every lesson in this curriculum follows the same rhythm, so once you learn the shape
you can move fast:

- **The Problem** — why this exists, in plain terms
- **The Concept** — the idea, usually with a diagram
- **Build It** — you write/run the code yourself, step by step
- **Use It** — how it's done for real (the library everyone actually uses)
- **Exercises** — check you actually got it

You're never expected to already know the answer. Read → run → verify → move on.

## Suggested path

**Everyone starts with 01.** The agent loop is the foundation the whole phase depends
on — don't skip it.

**Core patterns first (01–11):** loop, planning, reflection, search, tool use, memory,
and skills. These are the primitives; the frameworks later are just packaged versions
of them.

**Then frameworks and operations (12–30):** work through the framework lessons to find
the one that fits how you think, then evaluation, observability, and safety. You can
treat 18, 22, and the benchmark lessons as reference to pull in when a project needs them.

**Finish with the workbench mini-track (31–42):** this is the hands-on payoff — turning
everything above into an agent that's actually reliable on a real codebase. Do these in
order; each one builds a surface the next depends on, ending in a capstone pack you can
reuse.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
