# Phase 10: LLMs from Scratch

> Build, train, and understand large language models.

## Why this phase exists

Most people who work with large language models only ever use someone else's
finished model. They download a checkpoint, call an API, and treat the thing
inside as magic. This phase removes the magic. You start with raw text and end
with a model you built, trained, aligned, evaluated, and served — every stage in
your own hands.

By the time you finish, an LLM is no longer a black box. It's tokenizers turning
words into integers, a transformer predicting the next one, training loops that
teach it, alignment steps that make it useful, and inference tricks that make it
fast. When you know how each piece is made, you can debug, extend, and reason
about any model you meet — including the frontier ones from 2025 and 2026.

## What you need first

This is one of the most demanding phases in the curriculum, and it builds
directly on earlier work:

- **Phase 7 (Transformers)** — you need to understand attention, the transformer
  block, and the KV cache. This phase assembles those parts into full models.
- **Phase 3 (Deep Learning)** — training loops, backprop, optimizers, and loss
  functions are assumed knowledge here.
- **Phase 5 (NLP Foundations)** — text preprocessing and the vocabulary of
  language modeling.

If you've done those phases, you have what you need. You don't have to memorize
every detail from them — but if a lesson leans on attention or backprop and it
feels shaky, go back and refresh before pushing on. This phase is much easier
when the foundations are solid.

## What you'll be able to do after this phase

- Build a tokenizer from scratch and understand how text becomes model input
- Pre-train a GPT-2-scale model from raw data on a single GPU
- Turn a raw next-token predictor into a helpful assistant with SFT, RLHF, DPO,
  and Constitutional AI
- Evaluate models honestly and quantize them to fit real hardware
- Optimize inference with quantization, KV-cache tricks, and speculative decoding
- Read a 2026 frontier open model (Llama, DeepSeek-V3, Mixtral, Jamba) and name
  exactly where its architecture diverges from the GPT-2 you built

## The lessons

Do them in order — this phase is a single arc from raw text to a served,
optimized model, and later lessons assume the earlier ones. The final stretch
(14 onward) reads real 2025–2026 architectures against the model you built.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Tokenizers: BPE, WordPiece, SentencePiece** | Your model reads integers, not text — the tokenizer decides whether those integers carry meaning. | ~90 min |
| 02 | **Building a Tokenizer from Scratch** | Move past the toy: build a real, trainable tokenizer you fully control. | ~90 min |
| 03 | **Data Pipelines for Pre-Training** | The model reflects its data — clean, well-built pipelines are the difference between fluency and garbage. | ~90 min |
| 04 | **Pre-Training a Mini GPT (124M Parameters)** | Train a real GPT-2 Small from scratch on one GPU — the moment the model stops being a mystery. | ~120 min |
| 05 | **Scaling: Distributed Training, FSDP, DeepSpeed** | When a model no longer fits on one GPU, distributed training is the only path forward. | ~120 min |
| 06 | **Instruction Tuning (SFT)** | SFT is the bridge from a raw token predictor to a model that actually follows instructions. | ~90 min |
| 07 | **RLHF: Reward Model + PPO** | Teaches the model which response is *better*, encoding human judgment into its behavior. | ~90 min |
| 08 | **DPO: Direct Preference Optimization** | Get RLHF's results from a single training loop — no reward model, no PPO instability. | ~90 min |
| 09 | **Constitutional AI and Self-Improvement** | Replace most humans in the loop with the model itself critiquing and improving its own outputs. | ~45 min |
| 10 | **Evaluation: Benchmarks, Evals, LM Harness** | Benchmarks get gamed — the only eval that matters is yours, on your task and your data. | ~90 min |
| 11 | **Quantization: Making Models Fit** | Shrink a model from needing two A100s to running on a MacBook, with control over the tradeoffs. | ~120 min |
| 12 | **Inference Optimization** | Prefill and decode have different bottlenecks — every real speedup targets one or both. | ~120 min |
| 13 | **Building a Complete LLM Pipeline** | The capstone: wire every stage into one end-to-end run with a manifest, eval gate, and rollback plan. | ~120 min |
| 14 | **Open Models: Architecture Walkthroughs** | Read Llama 3, DeepSeek-V3, Mixtral, Qwen, and Gemma side by side and see exactly where each diverges from GPT-2. | ~45 min |
| 15 | **Speculative Decoding and EAGLE-3** | The production view of how a tiny draft model delivers 3×–6.5× speedups with no quality loss. | ~75 min |
| 16 | **Differential Attention (V2)** | Cancel attention's noise floor by subtracting two softmaxes — the fix for signal drowning at long context. | ~60 min |
| 17 | **Native Sparse Attention (DeepSeek NSA)** | A hardware-aligned, natively trainable sparse attention that beats full attention at 64k context. | ~60 min |
| 18 | **Multi-Token Prediction (MTP)** | Add a second next-next-token loss for free throughput and a built-in speculative drafter. | ~60 min |
| 19 | **DualPipe Parallelism** | Overlap forward/backward compute with expert all-to-all comms so GPUs stop sitting idle at scale. | ~60 min |
| 20 | **DeepSeek-V3 Architecture Walkthrough** | Read a 671B/37B frontier model top to bottom and derive every parameter count from its published config. | ~75 min |
| 21 | **Jamba — Hybrid SSM-Transformer** | Understand why mixing Mamba and Transformer layers has outlasted pure-SSM and pure-Transformer long-context bets. | ~60 min |
| 22 | **Async and Hogwild! Inference** | A new axis of parallelism: run N model instances against one shared KV cache and let them self-coordinate. | ~60 min |
| 25 | **Speculative Decoding and EAGLE** | The exact math behind guessing 3–5 tokens cheaply and verifying them for a 4–5× speedup at matched output. | ~75 min |
| 34 | **Gradient Checkpointing and Activation Recomputation** | Trade FLOPs for memory by recomputing activations — the key to training huge models at long context. | ~70 min |

## How each lesson is built

Every lesson in this curriculum follows the same rhythm, so once you learn the
shape you can move fast:

- **The Problem** — why this exists, in plain terms
- **The Concept** — the idea, usually with a diagram
- **Build It** — you write/run the code yourself, step by step
- **Use It** — how it's done for real (the library everyone actually uses)
- **Exercises** — check you actually got it

You're never expected to already know the answer. Read → run → verify → move on.

## Suggested path

**Go in order.** Lessons 01–13 are one continuous build: tokenize, pre-train,
scale, align, evaluate, quantize, serve, then wire it all together in the
capstone. Don't skip ahead — each stage feeds the next.

**Lessons 14–34 are the frontier tier.** Once you've built and served a model,
these read real 2025–2026 architectures (DeepSeek-V3, Jamba, NSA, MTP) against
the one you made. They're heavier and often *Learn*-type walkthroughs rather than
hands-on builds — pull them in as your interest and hardware allow. Lesson 14 is
the right entry point to that tier.

Take this phase slowly. It's long and demanding, but it's the point where you go
from *using* LLMs to genuinely *understanding* them.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
