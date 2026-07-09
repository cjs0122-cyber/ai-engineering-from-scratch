# Phase 1: Math Foundations

> The intuition behind every AI algorithm, through code — not textbooks.

## Why this phase exists

Every AI model — no matter how impressive — is built out of a small handful of
mathematical ideas: moving points around in space, measuring how wrong a guess is,
and nudging things in the direction that makes them less wrong. This phase teaches
those ideas. Not as proofs on a chalkboard, but as code you write and run until the
math stops being abstract.

Most people skip the math and treat AI as a black box. That works right up until
something breaks — a model won't learn, a result looks suspicious, a paper is
impossible to read — and then the black box wins. This phase is here so you can see
*inside* it. When you later meet a neural network, an embedding, or a loss function,
you'll recognize the pieces instead of memorizing spells.

## What you need first

- **Phase 0 (Setup & Tooling)** finished, or at least a working Python setup with
  NumPy — that's the one tool these lessons lean on everywhere.
- Comfort running a Python script or notebook and reading its output. That's it.

You do **not** need to be a mathematician, and you don't need to remember the
calculus you may have forgotten (or never took). Every idea here is built up from
scratch in code: you'll *see* a derivative before you ever see its formula, and
you'll compute it yourself. If the symbols in AI papers currently look like noise,
that's exactly the problem this phase solves.

## What you'll be able to do after this phase

- Read the math in an ML paper or codebase and know what each symbol is doing
- Work fluently with vectors, matrices, and tensors — the containers all AI data lives in
- Explain how gradients and the chain rule let a model actually learn
- Reason about probability, uncertainty, and whether a result is real or just luck
- Recognize and avoid the numerical bugs that silently wreck training runs
- Pick the right tool — a distance, a decomposition, a distribution — for a given problem

## The lessons

Do them roughly in order. Lessons 01–08 are the core spine; the rest deepen or
specialize and can be pulled in as later phases need them.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Linear Algebra Intuition** | See what neural networks actually do — move points around in space — before touching a formula. | ~60 min |
| 02 | **Vectors, Matrices & Operations** | Builds fluency in the matrix math that *is* a neural network's forward pass. | ~60 min |
| 03 | **Matrix Transformations** | Understand a matrix as a machine that reshapes space, so you know what any layer does to your data. | ~75 min |
| 04 | **Calculus for Machine Learning** | Derivatives tell you which way is "downhill" — the one thing a model needs to learn. | ~60 min |
| 05 | **Chain Rule & Automatic Differentiation** | The chain rule is the engine of backpropagation; here you build it yourself. | ~90 min |
| 06 | **Probability and Distributions** | Probability is how AI expresses uncertainty — and every output it makes. | ~75 min |
| 07 | **Bayes' Theorem** | Turn prior belief plus new evidence into updated belief — how models learn from data. | ~75 min |
| 08 | **Optimization** | Training is just finding the bottom of a valley; this shows you how. | ~75 min |
| 09 | **Information Theory** | Measures "surprise" — the idea underneath cross-entropy and every loss function. | ~60 min |
| 10 | **Dimensionality Reduction** | Find the hidden structure in high-dimensional data by viewing it from the right angle. | ~90 min |
| 11 | **Singular Value Decomposition** | The all-purpose matrix tool behind compression, embeddings, and recommendations. | ~120 min |
| 12 | **Tensor Operations** | Tensors carry every image, sentence, and gradient through a deep learning model. | ~90 min |
| 13 | **Numerical Stability** | Floating point quietly bites during training; learn to see it coming and prevent it. | ~120 min |
| 14 | **Norms and Distances** | Your distance function defines "similar" — get it wrong and everything downstream breaks. | ~90 min |
| 15 | **Statistics for Machine Learning** | Tells you whether your model really works or just got lucky. | ~120 min |
| 16 | **Sampling Methods** | How AI explores a space of possibilities instead of examining all of it. | ~120 min |
| 17 | **Linear Systems** | Solving Ax = b — an ancient problem that still runs inside your network. | ~120 min |
| 18 | **Convex Optimization** | Learn why "one valley" problems are easy and neural networks (many valleys) are not. | ~90 min |
| 19 | **Complex Numbers for AI** | The key to rotations and frequencies — groundwork for signal processing. | ~60 min |
| 20 | **The Fourier Transform** | Break any signal into the sine waves it's made of — essential for audio and images. | ~90 min |
| 21 | **Graph Theory for Machine Learning** | The math of relationships, for any data whose points are connected. | ~90 min |
| 22 | **Stochastic Processes** | Randomness with structure — the math behind random walks, Markov chains, and diffusion models. | ~75 min |

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

**Do the spine in order:** 01 → 02 → 03 (linear algebra), then 04 → 05 (calculus and
autodiff), then 06 → 07 (probability and Bayes), then 08 (optimization). These are
foundational — nearly every later phase assumes them, so don't skip them.

**If the math is familiar,** you can skim 01, 04, and 06 (the "Learn" lessons) and
spend your time in the "Build It" sections that make you write code.

**Pull in the rest as needed:** 09–17 deepen the core (information theory, SVD,
tensors, numerical stability, statistics). 18–22 are more specialized — convex
optimization, complex numbers, Fourier, graphs, stochastic processes — and are safe
to treat as optional on a first pass, then revisit when a later phase calls for them.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
