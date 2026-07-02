# Phase 11: LLM Engineering

> Put LLMs to work in production applications.

## Why this phase exists

In the last phase you built a language model from scratch. That taught you how the
machine works. This phase is different: it teaches you how to *use* one to build
things people actually rely on.

Most real AI engineering is not training models — it's everything around them.
Writing prompts the model follows literally. Retrieving the right documents so it
can answer questions about *your* data (RAG). Fine-tuning it cheaply when prompting
isn't enough. Making it call tools so it can act, not just talk. Serving it under
real traffic without going broke on token bills, and testing it so quality doesn't
quietly rot every time you change a prompt.

By the end you will have wired all of it into a single production service — the
difference between a demo that impresses a friend and a system that survives its
first ten thousand users.

## What you need first

This phase builds directly on what came before:

- **Phase 10 (LLMs from Scratch)** — you should understand what a language model is,
  how it generates tokens, and what instruction tuning does. Nearly every lesson
  here assumes it.
- **Phase 7 (Transformers)** — the architecture underneath everything you'll be
  prompting, embedding, and fine-tuning.
- **Phase 0 (Setup & Tooling)** — specifically the *APIs & Keys* lesson, since most
  of this phase calls real models (OpenAI, Anthropic, and others) over the network.

If that sounds like a lot, don't worry. You don't need to have memorized the math.
You need to be comfortable that a model takes tokens in and produces tokens out, and
willing to run code and read what comes back. Each lesson starts from the problem and
builds up.

## What you'll be able to do after this phase

- Write prompts and structure context so a model returns reliable, usable output
- Build a RAG pipeline that answers questions grounded in your own documents
- Fine-tune an open model on a single consumer GPU using LoRA / QLoRA
- Give a model tools it can call — the foundation of every AI agent
- Evaluate, cache, cost-optimize, and guard an LLM app so it holds up in production
- Ship a complete production LLM service that streams, tracks cost, and fails gracefully

## The lessons

Do them in order — later lessons lean heavily on earlier ones, and the final lesson
ties everything together.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Prompt Engineering: Techniques & Patterns** | Every token you send is an instruction the model follows literally — better instructions, better output. | ~90 min |
| 02 | **Few-Shot, Chain-of-Thought, Tree-of-Thought** | Showing a model *how to think* can move the same model from 78% to 91% accuracy on the same task. | ~45 min |
| 03 | **Structured Outputs: JSON, Schema Validation, Constrained Decoding** | Turns free-text model output into typed data your application can actually trust. | ~90 min |
| 04 | **Embeddings & Vector Representations** | The bridge from text to math that powers semantic search, similarity, and RAG. | ~75 min |
| 05 | **Context Engineering: Windows, Budgets, Memory, and Retrieval** | Deciding what goes into the model's window, in what order — the whole game, not just the prompt. | ~90 min |
| 06 | **RAG (Retrieval-Augmented Generation)** | Retrieves relevant documents into the prompt so the model can answer about your data — the most deployed pattern in production AI. | ~90 min |
| 07 | **Advanced RAG (Chunking, Reranking, Hybrid Search)** | The difference between a demo that works on 10 documents and a system that works on 10 million. | ~90 min |
| 08 | **Fine-Tuning with LoRA & QLoRA** | Fine-tune a 7B model in 6GB by training under 1% of its parameters — the trick the open-source ecosystem runs on. | ~75 min |
| 09 | **Function Calling & Tool Use** | The nervous system connecting the model (the brain) to real tools (the hands) — the basis of every agent. | ~75 min |
| 10 | **Evaluation & Testing LLM Applications** | The only thing standing between your app and silent degradation every time a prompt changes. | ~45 min |
| 11 | **Caching, Rate Limiting & Cost Optimization** | Treat every API call as a financial transaction — the discipline that keeps AI products alive. | ~45 min |
| 12 | **Guardrails, Safety & Content Filtering** | Your app will be attacked within 48 hours of launch; this decides whether it folds or holds. | ~45 min |
| 13 | **Building a Production LLM Application** | The capstone: wire every component from lessons 01–12 into one real service that handles real traffic. | ~120 min |
| 14 | **Model Context Protocol (MCP)** | The default wire format for connecting any LLM to any tool or data source — write one server, every host talks to it. | ~75 min |
| 15 | **Prompt Caching and Context Caching** | Keeps a warm prefix on the provider's side to cut inference cost 50–90% and first-token latency 40–85%. | ~60 min |
| 16 | **LangGraph — State Machines for Agents** | Turns a hand-written ReAct loop into a graph you can checkpoint, interrupt, branch, and time-travel through. | ~75 min |
| 17 | **Agent Framework Tradeoffs — LangGraph vs CrewAI vs AutoGen vs Agno** | How to pick the framework whose abstractions match your problem instead of writing glue twice. | ~45 min |

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

Go straight down 01 → 17. This phase is more tightly ordered than most: prompting and
context (01–05) come first because everything else uses them, retrieval and RAG (06–07)
build on embeddings, and function calling (09) unlocks tools, agents (16–17), and MCP (14).

If you're short on time, the essential spine is **01 → 03 → 04 → 06 → 09 → 10 → 13** —
prompt, structure, embed, retrieve, call tools, evaluate, then ship. Come back for
fine-tuning (08), the cost and safety lessons (11–12, 15), and the agent frameworks
(16–17) when a project needs them. Do the capstone (13) only after the lessons it
depends on.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
