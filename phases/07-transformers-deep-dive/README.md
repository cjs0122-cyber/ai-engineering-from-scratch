# Phase 7: Transformers Deep Dive

> The architecture that changed everything. Understand every layer.

## Why this phase exists

Almost every modern AI system — the chatbots, the image models, the speech
recognizers, the protein folders — runs on one architecture: the transformer.
It was proposed in a single 2017 paper, "Attention Is All You Need," and it now
dominates language, vision, audio, and biology. Same block, different inputs.

Most people treat the transformer as a black box: they import it from a library
and hope for the best. This phase does the opposite. You'll take it apart layer
by layer — attention, positional encoding, the feed-forward blocks, the masks —
and build a working transformer yourself, from scratch, one piece at a time.
By the end there is no magic left in it, only mechanisms you understand.

## What you need first

This is a build-heavy, math-aware phase. Before starting, you should have:

- **Phase 3 (Deep Learning Core)** — you need to be comfortable with neural
  networks, backpropagation, and training loops. Attention is just matrix
  multiplications and a softmax, but you have to be at home with those.
- **Phase 5 (NLP)** — especially text representation, sequence-to-sequence
  models, and the attention mechanism lesson. This phase picks up exactly where
  those left off.
- **Phase 1 (Math Foundations)** — matrix multiplication, dot products, and a
  little calculus. You don't need to derive anything by hand, but you should
  recognize what the operations are doing.

If that sounds like a lot, don't worry: each lesson rebuilds the ideas it needs
from the ground up, and the early lessons deliberately go slowly. If you can
follow a `for` loop and a matrix multiply, you can follow this.

## What you'll be able to do after this phase

- Implement self-attention and multi-head attention from scratch, no library
- Explain and code the full transformer — encoder, decoder, and the pieces that
  hold them together (residuals, normalization, feed-forward, cross-attention)
- Tell apart the major model families — BERT, GPT, T5/BART — and know why each
  is shaped the way it is
- Apply the same architecture beyond text: to images (ViT) and audio (Whisper)
- Make transformers faster and cheaper at inference with the KV cache, Flash
  Attention, Mixture of Experts, and speculative decoding
- Build a complete, working transformer from scratch as a capstone project

## The lessons

Do them in order — this phase builds a single model across the whole sequence,
and later lessons assume the ones before them.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Why Transformers — The Problems with RNNs** | Explains the architectural bet — process all tokens at once, not one at a time — that reshaped every scaling curve after 2017. | ~45 min |
| 02 | **Self-Attention from Scratch** | The core mechanism: every word asks "who matters to me?" and learns the answer. Everything else is built on this. | ~90 min |
| 03 | **Multi-Head Attention** | One head learns one relationship; many heads learn many, for the same parameter budget. The default in every real transformer. | ~75 min |
| 04 | **Positional Encoding — Sinusoidal, RoPE, ALiBi** | Attention ignores order on its own; these three algorithms are how a model knows which word came first. | ~45 min |
| 05 | **The Full Transformer — Encoder + Decoder** | Assembles attention with residuals, normalization, and feed-forward layers into the complete block you can stack deep. | ~75 min |
| 06 | **BERT — Masked Language Modeling** | Predicting a missing word instead of the next one — the training choice behind a generation of embedding models. | ~45 min |
| 07 | **GPT — Causal Language Modeling** | The triangle mask that lets a model see only the past, and turns a transformer into a text generator. | ~75 min |
| 08 | **T5, BART — Encoder-Decoder Models** | Combining an encoder that understands with a decoder that generates, for input-to-output tasks like translation and summarization. | ~45 min |
| 09 | **Vision Transformers (ViT)** | Shows that an image is just a grid of patches — so the same transformer that reads text can also see. | ~45 min |
| 10 | **Audio Transformers — Whisper Architecture** | Treats audio as an image of frequency over time, letting a transformer transcribe speech. | ~45 min |
| 11 | **Mixture of Experts (MoE)** | Activating only a fraction of a model's parameters per token — the sparsity idea behind today's largest, most efficient models. | ~45 min |
| 12 | **KV Cache, Flash Attention & Inference Optimization** | The tricks that make generation fast: training is FLOP-bound, but inference is memory-bound and needs different tools. | ~75 min |
| 13 | **Scaling Laws** | How compute splits between model size and training tokens — and why the "obvious" split was wrong for years. | ~45 min |
| 14 | **Build a Transformer from Scratch — The Capstone** | Thirteen lessons, one model, no shortcuts: assemble everything you've learned into a working transformer. | ~120 min |
| 15 | **Attention Variants — Sliding Window, Sparse, Differential** | Bending the shape of attention to recover the memory cost of every token seeing every token. | ~60 min |
| 16 | **Speculative Decoding — Draft, Verify, Repeat** | Breaking the serial chain of generation: a cheap model drafts tokens, the expensive model verifies them all at once. | ~60 min |

## How each lesson is built

Every lesson in this whole curriculum follows the same rhythm, so once you learn
the shape you can move fast:

- **The Problem** — why this exists, in plain terms
- **The Concept** — the idea, usually with a diagram
- **Build It** — you write/run the code yourself, step by step
- **Use It** — how it's done for real (the library everyone actually uses)
- **Exercises** — check you actually got it

You're never expected to already know the answer. Read → run → verify → move on.

## Suggested path

Go straight down the list, 01 → 16. This phase is unusually linear: it builds one
transformer across many lessons, and the capstone (14) expects you to have done
everything before it.

- **The core (01 → 05):** the foundation — why transformers exist, self-attention,
  multi-head attention, positional encoding, and the full architecture. Don't skip
  or skim these; everything after them assumes they're solid.
- **The model families (06 → 10):** BERT, GPT, T5/BART, ViT, and Whisper — the same
  block applied to different training objectives and modalities.
- **Scale and speed (11 → 13):** Mixture of Experts, inference optimization, and
  scaling laws — how these models are made large, fast, and efficient.
- **The capstone (14):** put it all together and build one yourself.
- **Going further (15 → 16):** attention variants and speculative decoding, the
  modern tricks layered on top once the fundamentals are second nature.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
