# Phase 0: Setup & Tooling

> Get your environment ready for everything that follows.

## Why this phase exists

Before you can build AI, your computer has to be able to *run* it. This phase is
the workshop-setup step: installing the languages AI is written in, the tools that
manage them, and the habits (version control, notebooks, debugging) that keep you
from fighting your own machine for the next 500 lessons.

It is not glamorous. There is no model here, no training, no clever math. But
almost everyone who quits an AI course quits in the first week — not because the AI
was too hard, but because *the setup* broke and they didn't know why. This phase is
here so that never happens to you.

## New to coding? Read this first

This curriculum was written by engineers, and the lessons assume you're comfortable
in a terminal. If you're **not** a developer, that's okay — but here's the honest
picture so you're not blindsided:

- **You will be typing commands into a black window (the "terminal").** That's
  normal. Every AI engineer does this all day. Lesson `10-terminal-and-shell`
  teaches it from zero — if the command line is new to you, **do that lesson first**,
  then come back to lesson 01.
- **You don't need to understand every word to make progress.** When a lesson says
  `uv pip install numpy`, you can run it now and understand it later. Setup is the
  one place where "copy, run, verify it worked" is a completely valid strategy.
- **Errors are expected, not failure.** Half of setup is hitting an error, reading
  it, and fixing one thing. Every lesson lists what "success" looks like so you know
  when you're actually done.
- **You do not need a powerful computer or a GPU.** A normal laptop is enough for
  learning. The GPU lesson (03) is "good to know," not "required to continue."

If you get stuck, the AI assistant you're likely already using can read any error
message and walk you through it — that's genuinely part of the modern workflow, not
cheating.

## What you'll be able to do after this phase

- Run Python, and (when a lesson needs them) Node.js and Rust, on your own machine
- Install any library a lesson asks for, without version conflicts breaking things
- Track your work with git, so you never lose progress and can undo mistakes
- Open and run a Jupyter notebook — the "lab bench" you'll prototype in
- Read an error message and know where to start fixing it

## The lessons

Do them roughly in order. The first few are the real foundation; the rest you can
pull in when a later phase needs them.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Dev Environment** | Installs the languages and package managers everything else depends on. The one non-skippable lesson. | ~45 min |
| 02 | **Git & Collaboration** | Version control — how you save, undo, and never lose your work. | ~30 min |
| 03 | **GPU Setup & Cloud** | Only needed when you start training bigger models. Skip on a first pass if you have no GPU. | ~45 min |
| 04 | **APIs & Keys** | How your code talks to AI services (OpenAI, Anthropic, etc.). Needed before any lesson that calls a model over the internet. | ~30 min |
| 05 | **Jupyter Notebooks** | The interactive scratchpad where you'll prototype and see results step by step. | ~30 min |
| 06 | **Python Environments** | Keeps each project's libraries separate so they don't collide ("dependency hell"). | ~30 min |
| 07 | **Docker for AI** | Packages a whole environment into a box that runs the same everywhere. More advanced — come back when a lesson calls for it. | ~60 min |
| 08 | **Editor Setup** | Configures your code editor so it helps instead of getting in the way. | ~20 min |
| 09 | **Data Management** | How to store, load, and organize the datasets that feed your models. | ~45 min |
| 10 | **Terminal & Shell** | The command line from scratch. **Start here if the terminal is new to you.** | ~35 min |
| 11 | **Linux for AI** | The operating system almost all AI actually runs on — enough to not get stuck. | ~30 min |
| 12 | **Debugging & Profiling** | Finding out *why* something is wrong — including the silent AI bugs that don't crash but quietly ruin results. | ~60 min |

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

**If you've coded before:** go straight down 01 → 02 → 04 → 05 → 06, and pull in
03/07/09/11 when a later phase needs them.

**If you're new to coding:** do **10 (Terminal)** first, then **01 → 02 → 05 → 06**.
Treat 03, 07, and 11 as optional reading for now. Don't rush — this week of setup
pays off across every phase after it.

When your environment is ready, Phase 1 (Math Foundations) is where the actual AI
begins.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
