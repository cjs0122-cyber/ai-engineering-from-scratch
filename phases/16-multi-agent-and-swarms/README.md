# Phase 16: Multi-Agent & Swarms

> Coordination, emergence, and collective intelligence.

## Why this phase exists

In Phase 14 you built a single agent, and in Phase 15 you made it run on its own.
Both work — right up until the task gets too big for one agent to hold in its head.
The context window fills up. One prompt is trying to research, code, and review all
at once, and does all three badly. That's the single-agent ceiling, and you hit it
on every real problem.

The fix isn't a bigger agent. It's *more* agents — a team that divides the work,
each with its own fresh context and its own job. But the moment you have more than
one agent, you have new problems that don't exist for a single agent: How do they
talk to each other? Who decides what? What happens when two of them disagree, or one
of them hallucinates a "fact" the others start trusting?

This phase is about those problems. It covers how agents coordinate (supervisors,
hierarchies, swarms), how they communicate (protocols, shared memory, handoffs), how
they reach agreement (voting, debate, consensus), and how surprisingly *smart*
behavior can emerge from many simple agents interacting — along with the failure
modes that emerge just as easily.

## What you need first

- **Phase 14 (Agent Engineering)** — you need to be comfortable building a single
  agent: tools, the reasoning loop, context management. Everything here assumes one
  working agent as the building block.
- **Phase 15 (Autonomous Systems)** — long-running, self-directed agents. Multi-agent
  systems are autonomous systems that talk to each other, so the durability and
  safety ideas from Phase 15 carry straight over.

A few lessons also lean on ideas from earlier phases (reinforcement learning shows up
in Lesson 20), but each lesson says what it assumes. If you've done Phases 14 and 15,
you're ready. This is advanced material, but it's built up step by step from
primitives you already know — you won't be dropped in the deep end.

## What you'll be able to do after this phase

- Split a task that's too big for one agent across a coordinated team
- Pick the right architecture for the job — supervisor, hierarchy, swarm, or group chat
- Wire agents together with real protocols (MCP, A2A) instead of ad-hoc string passing
- Make a group of agents agree on an answer through voting, debate, and consensus
- Recognize and defend against the classic multi-agent failure modes (groupthink,
  memory poisoning, cascading errors, monoculture)
- Read any new multi-agent framework release and place it on a small map of primitives

## The lessons

Do them in order. The early lessons build the primitives; everything later is a
variation or combination of them.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Why Multi-Agent?** | The case for many agents over one bigger agent — where the single-agent ceiling comes from and why teams break through it. | ~60 min |
| 02 | **Heritage of FIPA-ACL and Speech Acts** | The 2000-era agent communication standard that today's protocols are quietly reinventing — history that tells you which 2026 ideas are new. | ~60 min |
| 03 | **Communication Protocols** | The shared contracts (MCP, A2A, ACP, ANP) that let agents actually talk instead of shouting strings into the void. | ~120 min |
| 04 | **The Multi-Agent Primitive Model** | The four primitives — agent, handoff, shared state, orchestrator — that every framework is built from. Learn these and you can read any release. | ~60 min |
| 05 | **Supervisor / Orchestrator-Worker Pattern** | One lead agent plans and delegates to specialized workers — the pattern behind Anthropic's Research system. | ~75 min |
| 06 | **Hierarchical Architecture and Its Failure Mode** | Supervisors nested into an org chart — the natural pattern for big tasks, and the one most likely to collapse into managerial looping. | ~60 min |
| 07 | **Society of Mind and Multi-Agent Debate** | Many agents propose, critique, and update over rounds — and beat a single agent thinking alone. | ~60 min |
| 08 | **Role Specialization — Planner, Critic, Executor, Verifier** | The most common team decomposition of 2026, and why the verifier role is the one you can't skip. | ~60 min |
| 09 | **Parallel / Swarm / Networked Architectures** | Decentralized coordination with no central decider — trading determinism for scale. | ~75 min |
| 10 | **Group Chat and Speaker Selection** | N agents share one conversation and a selector picks who speaks next — the archetype of emergent multi-agent talk. | ~60 min |
| 11 | **Handoffs and Routines — Stateless Orchestration** | OpenAI Swarm's minimal design: an agent is a prompt plus tools, and a handoff is a function that returns another agent. | ~60 min |
| 12 | **A2A — The Agent-to-Agent Protocol** | The peer-to-peer standard for agents built by different teams to discover and work with each other. | ~75 min |
| 13 | **Shared Memory and Blackboard Patterns** | The only stateful part of a multi-agent system — and where the nastiest bug, memory poisoning, lives. | ~75 min |
| 14 | **Consensus and Byzantine Fault Tolerance for Agents** | Getting agents to agree even when one is lying, sycophantic, or wrong in the same way as everyone else. | ~75 min |
| 15 | **Voting, Self-Consistency, and Debate Topology** | Cheap aggregation by majority vote, and how the shape of the conversation (star, chain, tree, graph) changes the result. | ~75 min |
| 16 | **Negotiation and Bargaining** | Agents haggling over resources, prices, and task allocation — and the structural tricks that raise deal rates. | ~75 min |
| 17 | **Generative Agents and Emergent Simulation** | The Smallville architecture (memory, reflection, plan) where a party organized itself among 25 agents nobody scripted. | ~75 min |
| 18 | **Theory of Mind and Emergent Coordination** | Agents reasoning about what other agents believe — and the finding that this coordination is prompt- and model-dependent, not free. | ~75 min |
| 19 | **Swarm Optimization for LLMs (PSO, ACO)** | Bio-inspired optimization repurposed for prompts, model weights, and agent routing. | ~75 min |
| 20 | **MARL — MADDPG, QMIX, MAPPO** | The reinforcement-learning heritage of multi-agent coordination that still shapes how agent teams are trained. | ~90 min |
| 21 | **Agent Economies, Token Incentives, Reputation** | The economic layer for long-horizon agents — identity, settlement, and fairly rewarding who contributed what. | ~75 min |
| 22 | **Production Scaling — Queues, Checkpoints, Durability** | Running thousands of concurrent agents without losing work when a worker crashes — plus the "start simple" counterpoint. | ~75 min |
| 23 | **Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors** | The reference taxonomy of how multi-agent systems break, treated as first-class engineering targets. | ~75 min |
| 24 | **Evaluation and Coordination Benchmarks** | How to actually measure a multi-agent system, and why passing one benchmark isn't evidence it generalizes. | ~75 min |
| 25 | **Case Studies and the 2026 State of the Art** | Three production systems read end-to-end, plus the current framework landscape — the capstone that ties it together. | ~90 min |

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

**Start with the foundation:** do **01 → 04** in order. These are the concepts and
primitives the rest of the phase assumes — don't skip them.

**Then the core architectures:** **05 → 13** walk through the main coordination and
communication patterns (supervisor, hierarchy, debate, swarm, group chat, handoffs,
protocols, shared memory). This is the heart of the phase.

**Then agreement and emergence:** **14 → 21** cover consensus, voting, negotiation,
and the surprising behaviors that emerge when many agents interact.

**Finish with production reality:** **22 → 25** are scaling, failure modes,
evaluation, and case studies. Lesson 25 is the capstone — save it for last.

If you're short on time, lessons 01, 04, 05, 09, 13, and 23 give you the load-bearing
mental model; the rest deepen it.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
