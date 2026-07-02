# Phase 15: Autonomous Systems

> Agents that run without human intervention — safely.

## Why this phase exists

Up to now, your agents have mostly worked in short bursts with a human watching:
ask, answer, check, repeat. This phase is about what happens when you let go of the
wheel — when an agent runs for minutes, hours, or days on a single task, taking
actions in the real world without someone approving each step.

That shift breaks almost every assumption you built around chat. A run that lasts
longer than lunch can rack up surprise bills, get stuck in a loop, reward-hack its
own scoring, or take an action you never intended. So this phase is really two
things braided together: how to *build* long-horizon and self-improving agents, and
how to *bound* them — kill switches, budgets, checkpoints, human-in-the-loop review,
and the safety frameworks the frontier labs actually use. Autonomy without the
guardrails is not a feature; it is an incident waiting to happen.

## What you need first

This is one of the last phases in the curriculum, and it builds directly on
**Phase 14 (Agent Engineering)** — especially the agent loop and tool use. If you
can build an agent that plans, calls tools, and reacts to results, you have what you
need. Several lessons also lean on **Phase 13 (Reasoning and Chain-of-Thought)** for
the self-improvement material.

You don't need to have memorized every earlier phase. Each lesson names its own
prerequisites at the top and re-explains the ideas it depends on, so if something
feels shaky you'll know exactly where to look back.

## What you'll be able to do after this phase

- Reason about long-horizon agents — why runs that last hours change cost, trust,
  and failure modes
- Build and critique self-improvement loops (STaR, evolutionary coding, self-modifying
  agents) and spot where they reward-hack
- Wire real safety controls: action budgets, kill switches, circuit breakers, canary
  tokens, and propose-then-commit review
- Run agents durably in the background so they survive crashes and deploys
- Design human-in-the-loop checkpoints and rollback plans that actually catch bad
  actions
- Read and compare the frontier safety frameworks (Anthropic RSP, OpenAI Preparedness,
  DeepMind FSF, METR evaluations) and know their honest limits

## The lessons

Work through them in order — the phase is arranged as a deliberate arc, from what
long-horizon agents are, through how they self-improve, to how you keep them safe.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **The Shift from Chatbots to Long-Horizon Agents** | Frames the whole phase: why hours-long runs break every assumption built around single-turn chat. | ~45 min |
| 02 | **STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning** | The smallest self-improvement loop — a model fine-tuning on its own correct rationales — and why it isn't magic. | ~60 min |
| 03 | **AlphaEvolve — Evolutionary Coding Agents** | Shows how a coding model plus an evolutionary loop and a rigorous evaluator can beat decades-old human results. | ~60 min |
| 04 | **Darwin Godel Machine — Open-Ended Self-Modifying Agents** | An agent that edits its own source code — including the moment it learned to reward-hack. | ~60 min |
| 05 | **AI Scientist v2 — Workshop-Level Autonomous Research** | The full research loop run end to end, and the sober independent evaluation of where it fails. | ~60 min |
| 06 | **Automated Alignment Research (Anthropic AAR)** | Automating alignment research is the step that compresses the timeline to the very risks it aims to detect. | ~60 min |
| 07 | **Recursive Self-Improvement — Capability vs Alignment** | Why RSI is now an engineering topic, and the alignment-faking failure mode it would amplify. | ~60 min |
| 08 | **Bounded Self-Improvement Designs** | The four primitives for bounding a self-improvement loop — and why none of them is a proof of safety. | ~60 min |
| 09 | **The Autonomous Coding Agent Landscape (2026)** | How scaffolding now matters as much as the model, and how benchmark numbers hide easy tasks. | ~45 min |
| 10 | **Claude Code as an Autonomous Agent: Permission Modes and Auto Mode** | The permission modes and safety classifiers that decide what an agent may do unattended. | ~45 min |
| 11 | **Browser Agents and Long-Horizon Web Tasks** | Real capability gains on the web — and the prompt-injection attack surface that can't be fully patched. | ~45 min |
| 12 | **Long-Running Background Agents: Durable Execution** | How production agents checkpoint, retry, and replay so they survive crashes and deploys. | ~60 min |
| 13 | **Action Budgets, Iteration Caps, and Cost Governors** | The controls that stop an agent from finding a loop and quietly spending your budget inside it. | ~60 min |
| 14 | **Kill Switches, Circuit Breakers, and Canary Tokens** | The tripwires held outside the agent's edit surface that let you stop it fast when it misbehaves. | ~60 min |
| 15 | **Human-in-the-Loop: Propose-Then-Commit** | The precise 2026 pattern for review — persist, surface intent and blast radius, commit, verify. | ~60 min |
| 16 | **Checkpoints and Rollback** | How to persist state, recover from crashes, and undo actions — with idempotency to avoid double-execution. | ~60 min |
| 17 | **Constitutional AI and Rule Overrides** | Reason-based alignment, the priority hierarchy, and what operators can and cannot override. | ~60 min |
| 18 | **Llama Guard and Input/Output Classification** | Classifying inputs and outputs for safety — and why classifiers are a layer, not a solution. | ~45 min |
| 19 | **Anthropic Responsible Scaling Policy v3.0** | How one frontier lab decides when a model is too capable to ship — and where v3.0 regressed. | ~45 min |
| 20 | **OpenAI Preparedness Framework and DeepMind Frontier Safety Framework** | The other two major safety frameworks, their autonomy thresholds, and their stated limits. | ~45 min |
| 21 | **METR Time Horizons and External Capability Evaluation** | How an independent evaluator measures agent capability — and why a time horizon is an upper bound. | ~60 min |
| 22 | **CAIS, CAISI, and Societal-Scale Risk** | Zooming out to the societal risk frameworks, organizations, and emerging regulation. | ~45 min |

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

Go straight down 01 → 22. The phase is built as one continuous argument: lessons
01–09 cover long-horizon and self-improving agents, 10–16 are the practical safety
engineering (permissions, budgets, tripwires, human review, rollback), and 17–22 are
the alignment techniques and safety frameworks that govern the whole picture.

If you're short on time, the load-bearing minimum is **01, 08, 10, 13, 14, 15, 16** —
the framing plus the core safety controls. But the self-improvement lessons (02–07)
are what make the safety lessons make sense, so come back for them.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
