# Phase 19: Capstone Projects

> Prove everything you learned. Build portfolio-grade systems.

## Why this phase exists

Every phase before this one taught you a piece: the math, the models, the
training loops, the agents, the infrastructure, the safety layer. This phase is
where the pieces stop being lessons and start being *systems*. You take
everything you learned and build things a stranger could look at and understand
what you can do.

These are not toy demos. Each project mirrors the shape a real 2026 product
actually ships in — a coding agent that opens pull requests, a voice assistant
under an 800ms latency budget, a RAG chatbot that has to pass a red team. You
build them end to end, measure them against public benchmarks or a golden set,
and end up with something you can put in front of an employer. This is the
portfolio phase.

## What you need first

Broadly, the rest of the curriculum. The big flagship capstones are integrative
by design — a single one might lean on your LLM engineering, your agents, your
infrastructure, and your safety work all at once. **Every project lists its own
prerequisites** at the top of its doc, so you can check exactly which earlier
phases a given project draws on before you start it.

Two things to keep in mind:

- **These are projects, not lessons.** You are not meant to march through all 85
  in order. You pick the ones that match your interests and the phases you feel
  strongest in. A vision person and an infrastructure person will leave this
  phase with very different portfolios, and that is the point.
- **You don't need to have mastered everything.** Many of the projects are
  ~90-minute "build one component from scratch" lessons grouped into tracks —
  start there to warm up, then take on a multi-day flagship capstone when you're
  ready. Pick a project slightly harder than what feels comfortable.

## What you'll be able to do after this phase

- Ship an end-to-end AI system, not just a notebook — CLI or API in, real output out
- Measure your own work honestly against public benchmarks, golden sets, and red teams
- Wire together retrieval, models, tools, agents, and infrastructure into one product
- Build the unglamorous parts that make a system production-grade: sandboxes, eval harnesses, observability, safety gates
- Reproduce the architecture behind a named 2026 product and explain the trade-offs it made
- Walk into an interview with a portfolio of systems you can defend line by line

## The projects

There are 85 projects here — far too many for one flat table — so they're grouped
by theme. The first group is the big, multi-day **flagship capstones**: full
production systems, 25-40 hours each. The rest are **tracks** of shorter
(~90-minute) "build one piece from scratch" projects that assemble into a
complete system by the end of the track. Pick a group that matches your
interests.

### Flagship capstones (full production systems, 25-40 hours each)

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 01 | **Capstone 01 — Terminal-Native Coding Agent** | Build a Claude-Code-shaped agent — CLI in, pull request out — and measure it on SWE-bench Pro. | ~35 hrs |
| 02 | **Capstone 02 — RAG over Codebase (Cross-Repo Semantic Search)** | The internal code search every serious org runs: 2M lines, 10 repos, incremental re-indexing on every push. | ~30 hrs |
| 03 | **Capstone 03 — Real-Time Voice Assistant (ASR to LLM to TTS)** | A voice agent under an 800ms latency budget that handles barge-in and survives packet loss. | ~30 hrs |
| 04 | **Capstone 04 — Multimodal Document QA (Vision-First PDF, Tables, Charts)** | Vision-first late-interaction document QA that beats OCR-then-text on 10k real pages. | ~30 hrs |
| 05 | **Capstone 05 — Autonomous Research Agent (AI-Scientist Class)** | An agent that plans, runs, and writes up experiments end to end under a $30-per-paper budget. | ~40 hrs |
| 06 | **Capstone 06 — DevOps Troubleshooting Agent for Kubernetes** | An SRE agent that reads telemetry, ranks root causes, and posts human-gated remediations. | ~30 hrs |
| 07 | **Capstone 07 — End-to-End Fine-Tuning Pipeline (Data to SFT to DPO to Serve)** | Data to SFT to DPO to a quantized, speculatively-decoded served endpoint, reproducibly. | ~35 hrs |
| 08 | **Capstone 08 — Production RAG Chatbot for a Regulated Vertical** | A guarded, observed, RAGAS-graded chatbot that has to pass a golden set and a red team. | ~30 hrs |
| 09 | **Capstone 09 — Code Migration Agent (Repo-Level Language / Runtime Upgrade)** | Deterministic AST rewrites plus an agent layer, migrating 50 real repos with a failure taxonomy. | ~30 hrs |
| 10 | **Capstone 10 — Multi-Agent Software Engineering Team** | An architect, parallel coders, a reviewer, and a tester — evaluated on SWE-bench Pro. | ~40 hrs |
| 11 | **Capstone 11 — LLM Observability & Eval Dashboard** | Self-hosted tracing and eval that catches an injected regression in under five minutes. | ~25 hrs |
| 12 | **Capstone 12 — Video Understanding Pipeline (Scene, QA, Search)** | Ingest 100 hours of video and answer with timestamps plus frame previews. | ~30 hrs |
| 13 | **Capstone 13 — MCP Server with Registry and Governance** | The default 2026 tool-use spec, done right: StreamableHTTP, OAuth 2.1, policy gating, a registry. | ~25 hrs |
| 14 | **Capstone 14 — Speculative-Decoding Inference Server** | Serve two open models at 2.5x+ baseline throughput with a full tail-latency report. | ~30 hrs |
| 15 | **Capstone 15 — Constitutional Safety Harness + Red-Team Range** | A layered safety harness plus an autonomous red team that produces a measurable harmlessness delta. | ~25 hrs |
| 16 | **Capstone 16 — GitHub Issue-to-PR Autonomous Agent** | Label an issue, get a PR: the self-hosted version of Cursor/Codex/Jules, compared on cost and pass rate. | ~30 hrs |
| 17 | **Capstone 17 — Personal AI Tutor (Adaptive, Multimodal, with Memory)** | A Socratic, multimodal tutor with a learner model, run through a two-week efficacy study. | ~30 hrs |

### Track A — Build a coding-agent harness (~90 min each)

The harness is the agent; the model is a coprocessor. Build the loop, the tools,
the sandbox, and the eval, then plug a model into the seam.

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 20 | **Agent Harness Loop Contract** | Freeze the plan-act-observe loop contract any model can wire into. | ~90 min |
| 21 | **Tool Registry with Schema Validation** | A tool the agent cannot validate is a tool it cannot call — build the checker first. | ~90 min |
| 22 | **JSON-RPC 2.0 Over Newline-Delimited Stdio** | Hand-roll the transport so you know what every framing layer is paying for. | ~90 min |
| 23 | **Function Call Dispatcher** | Timeouts, retries, dedupe, and error mapping all live on this one seam. | ~90 min |
| 24 | **Plan-Execute Control Flow** | A plan that survives a failure is an agent; one that doesn't is a script. | ~90 min |
| 25 | **Capstone Lesson 25: Verification Gates and the Observation Budget** | The gate chain that decides what a tool may run and how much output the model may see. | ~90 min |
| 26 | **Capstone Lesson 26: Sandbox Runner with Denylist and Path Jail** | The layer between the model and the OS: denylist, path jail, output truncation, wall-clock kill. | ~90 min |
| 27 | **Capstone Lesson 27: Eval Harness with Fixture Tasks** | pass@1, pass@k, latency, and cost — the source of truth that separates a regression from a refactor. | ~90 min |
| 28 | **Capstone Lesson 28: Observability with OTel GenAI Spans and Prometheus Metrics** | OTel GenAI spans and Prometheus metrics so the agent stops being a black box that costs money. | ~90 min |
| 29 | **Capstone Lesson 29: End-to-End Coding Agent on the Harness** | Stitch the gate chain, sandbox, eval, and spans into one working coding agent. | ~90 min |

### Track B — Build an LLM from scratch (~90 min each)

Tokenizer to GPT to fine-tuning to eval, every piece by hand.

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 30 | **BPE Tokenizer From Scratch** | Bytes in, ids out, ids back to the same bytes — where every text model starts. | ~90 min |
| 31 | **Tokenized Dataset with Sliding Window** | The conveyor that feeds token ids into a pretraining run. | ~90 min |
| 32 | **Token and Positional Embeddings** | The two lookup tables that turn integers into the vectors a model can learn from. | ~90 min |
| 33 | **Multi-Head Self-Attention** | The attention block as the model actually uses it: three views, H heads, one mask. | ~90 min |
| 34 | **Transformer Block from Scratch** | The unit of every modern decoder — pre-LN vs post-LN, built side by side. | ~90 min |
| 35 | **GPT Model Assembly** | Stack the blocks into a working 124M-parameter GPT that generates text. | ~90 min |
| 36 | **Training Loop and Evaluation** | AdamW, warmup-plus-cosine, held-out eval — the skeleton that trains every decoder LLM. | ~90 min |
| 37 | **Loading Pretrained Weights** | Map and load GPT-2-style safetensors into your own architecture, no opaque loaders. | ~90 min |
| 38 | **Capstone Lesson 38: Classifier Fine-Tuning by Head Swap** | Swap the head for a classifier and compare final-layer-only vs full fine-tuning. | ~90 min |
| 39 | **Capstone Lesson 39: Instruction Tuning by Supervised Fine-Tuning** | An Alpaca-style SFT loop that masks instruction tokens and trains only the response. | ~90 min |
| 40 | **Capstone Lesson 40: Direct Preference Optimization from Scratch** | Derive and train DPO from the reward-difference identity, with the math pinned by tests. | ~90 min |
| 41 | **Capstone Lesson 41: Full Evaluation Pipeline** | Four heterogeneous evals plus a local mock judge, aggregated into one report. | ~90 min |

### Track C — Pretraining infrastructure (~90 min each)

Everything around the training loop: getting data on disk, keeping the run alive, scaling it out.

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 42 | **Large Corpus Downloader** | Streaming download, decompress, and near-dedup with a resume story worked out first. | ~90 min |
| 43 | **HDF5 Tokenized Corpus** | A resizable, chunked, memory-mapped layout the trainer can stream at line speed. | ~90 min |
| 44 | **Cosine LR with Linear Warmup** | The modern default LR schedule, plotted and proven against its boundaries. | ~90 min |
| 45 | **Gradient Clipping and Mixed Precision** | The two safety belts production training can't ship without: clipping and AMP with NaN handling. | ~90 min |
| 46 | **Gradient Accumulation** | Train at an effective batch you can't afford, one micro-batch at a time. | ~90 min |
| 47 | **Checkpoint Save and Resume** | Atomic save of model, optimizer, scheduler, and RNG state so a kill leaves a valid file. | ~90 min |
| 48 | **Distributed Data Parallel and FSDP from Scratch** | Multi-rank training as two collectives and one rule: never let the ranks disagree. | ~90 min |
| 49 | **Language Model Evaluation Harness** | Task, metric, runner, and leaderboard in one short, swappable shape. | ~90 min |

### Autonomous research agent (~90 min each)

The plan-execute-verify research loop, one component at a time.

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 50 | **Hypothesis Generator** | Force each draft hypothesis to land somewhere new instead of repeating itself. | ~90 min |
| 51 | **Literature Retrieval** | Check whether someone already proved it before spinning up a sandbox. | ~90 min |
| 52 | **Experiment Runner** | Take a spec, run it sandboxed, emit a metrics blob the evaluator can trust. | ~90 min |
| 53 | **Result Evaluator** | Turn metrics into a verdict: improvement, regression, or noise. | ~90 min |
| 54 | **Paper Writer** | Build the LaTeX skeleton as a contract that fails loudly, then fill it. | ~90 min |
| 55 | **Critic Loop** | Engineer a critic that actually converges instead of always approving or always rejecting. | ~90 min |
| 56 | **Iteration Scheduler** | Decide what to stop exploring — the decision that is the whole game. | ~90 min |
| 57 | **End-to-End Research Demo** | Compose every earlier contract into one self-terminating research run. | ~90 min |

### Vision-language model from scratch (~90 min each)

Patches to a captioning, question-answering VLM, built up layer by layer.

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 58 | **Vision Encoder Patches** | A tokenizer for pixels: cut the image into a grid, project each square, add a 2D position. | ~90 min |
| 59 | **Vision Transformer Encoder** | The 12-layer engine room of every modern vision-language model. | ~90 min |
| 60 | **Projection Layer for Modality Alignment** | The small MLP that pulls image tokens into the text embedding space — the piece that matters most for transfer. | ~90 min |
| 61 | **Cross-Attention Fusion** | Let every text token attend to every patch so words ground in regions. | ~90 min |
| 62 | **Vision-Language Pretraining** | Train the whole stack with a contrastive loss plus a captioning loss. | ~90 min |
| 63 | **Multimodal Evaluation** | Retrieval R@k, VQA exact-match, and captioning BLEU-4 from primitives. | ~90 min |

### Advanced RAG pipeline (~90 min each)

The retrieval components that separate a demo from a shippable system.

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 64 | **Chunking Strategies, Compared** | Chunking decides what your retriever can ever surface — get boundaries wrong and nothing downstream repairs it. | ~90 min |
| 65 | **Hybrid Retrieval with BM25 and Dense Embeddings** | Reciprocal rank fusion votes rather than interpolates, and the vote wins on every query class. | ~90 min |
| 66 | **Cross-Encoder Reranker** | The smartest, slowest reader, used as a second stage on the top-k so it pays for itself. | ~90 min |
| 67 | **Query Rewriting: HyDE, Multi-Query, and Decomposition** | Rewrite the user's query into something closer to what the answer looks like. | ~90 min |
| 68 | **RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance** | Grade retrieval and answer at once — different axes, different failures. | ~90 min |
| 69 | **End-to-End RAG System** | Six components, one pipeline, one eval loop, one self-terminating demo you ship. | ~90 min |

### Evaluation harness (~90 min each)

Build a real eval harness from first principles — the tool you'll reach for on every later system.

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 70 | **Task Spec Format** | Freeze the JSONL shape and metric vocabulary before writing a single scorer. | ~90 min |
| 71 | **Classical Metrics** | BLEU, ROUGE-L, F1, exact-match, accuracy — implemented so you know what the number means. | ~90 min |
| 72 | **Code Exec Metric** | Extract generated code, run it without crashing the host, and tally pass-rates honestly. | ~90 min |
| 73 | **Perplexity and Calibration** | Calibration is half of trustworthy eval; perplexity tells you if the model finds the text plausible at all. | ~90 min |
| 74 | **Leaderboard Aggregation** | Per-model rankings across heterogeneous tasks, with the significance testing everyone skips. | ~90 min |
| 75 | **End-to-End Eval Runner** | Glue the spec, adapters, scorers, calibration, and leaderboard into one runner. | ~90 min |

### Distributed training from scratch (~90 min each)

The collectives and sharding strategies behind every large training run, built over a simulated mesh.

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 76 | **Collective Ops From Scratch** | allreduce, broadcast, allgather, reduce_scatter — every framework primitive is a wrapper around these four. | ~90 min |
| 77 | **Data Parallel DDP From Scratch** | DDP is a backward hook on top of allreduce, about 200 lines. | ~90 min |
| 78 | **ZeRO Optimizer State Sharding** | Shard the optimizer across ranks for a linear memory drop on the largest allocation. | ~90 min |
| 79 | **Pipeline Parallel and Bubble Analysis** | Split the model across ranks and minimize the pipeline bubble — the whole craft. | ~90 min |
| 80 | **Sharded Checkpoint and Atomic Resume** | Parallel per-rank shards plus a manifest so a node failure costs 30 minutes, not 30 hours. | ~90 min |
| 81 | **End-to-End Distributed Training** | Assemble DDP, ZeRO-1, and a sharded checkpoint into one resumable training run. | ~90 min |

### Safety harness (~90 min each)

Name the attack, detect it, measure the defense — the safety layer, from taxonomy to gate.

| # | Project | Why it matters | Time |
|---|---------|----------------|------|
| 82 | **Capstone 82 — Jailbreak Taxonomy** | Name the attack before you defend it — a harness without a taxonomy is a coin flip. | ~90 min |
| 83 | **Capstone 83 — Prompt Injection Detector** | A function from prompt to confidence and category; anything else is a vibe. | ~90 min |
| 84 | **Capstone 84 — Refusal Evaluation** | Helpfulness on benign prompts and refusal on harmful ones are two metrics — measure both. | ~90 min |
| 85 | **Capstone 85 — Content Classifier Integration** | Output-side classifiers answer a different question than input-side rules; both need a policy router. | ~90 min |
| 86 | **Capstone 86 — Constitutional Rules Engine** | A rule is a name, a predicate, and an explanation — missing one makes it a vibe. | ~90 min |
| 87 | **Capstone 87 — End-to-End Safety Gate** | Pre-gen, during-gen, post-gen: three checkpoints, one verdict, an audit trail per request. | ~90 min |

## How each project is built

Every project follows the same rhythm as the rest of the curriculum, so once you
know the shape you can move fast:

- **The Problem** — why this system exists, in plain terms
- **The Concept** — the architecture, usually with a diagram
- **Build It** — you write and run the code yourself, step by step
- **Use It** — how it's done for real, and what named 2026 products do here
- **Exercises** — check you actually got it

Capstones are bigger and more integrative than a normal lesson. The flagship
projects add a **Ship It** step — deploying, benchmarking, and writing up results
— because a system you can't measure or run isn't finished. The ~90-minute track
projects are smaller, but each one composes into a working end-to-end system by
the last lesson of its track.

## Suggested path

There is no single order here. Choose by interest and by strength:

- **Warm up with a track.** If you want reps before a multi-day build, pick a
  track that matches a phase you enjoyed — Track A (agents), Track B (LLMs from
  scratch), the RAG pipeline, the safety harness — and do it in order. Each track
  ends in a working system.
- **Then take on a flagship.** Pick one big capstone in the domain you want to be
  hired for. Check its prerequisites, make sure you're solid on those phases, and
  build it end to end, including Ship It.
- **Follow the field you care about.** Vision people: 04, 12, and the VLM track.
  Infrastructure people: 07, 14, and the distributed-training and pretraining
  tracks. Agent people: 01, 10, 16, and Track A. Safety people: 15 and the safety
  harness track.

You don't need to do all 85. Two or three flagship capstones plus the tracks
behind them make a portfolio that speaks for itself.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
