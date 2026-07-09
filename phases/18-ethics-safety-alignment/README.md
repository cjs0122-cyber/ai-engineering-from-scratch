# Phase 18: Ethics, Safety & Alignment

> Build AI that helps humanity. Not optional.

## Why this phase exists

Everything in the earlier phases teaches you to make models *more capable*. This
phase is about the other half of the job: making sure capable models actually do
what people want, refuse what they shouldn't do, and don't quietly cause harm
along the way.

That splits into three related problems. **Ethics** is about the human impact —
bias, fairness, privacy, who gets hurt and who decides. **Safety** is about
stopping bad outcomes — jailbreaks, prompt injection, dangerous capabilities,
attackers. **Alignment** is the deepest one — getting a system's *actual* goals
to match the goals we intended, even when we can only train it on an imperfect
proxy for what we care about.

None of this is optional or "nice to have." A model that helps a novice build a
weapon, leaks a company's data through a poisoned email, or learns to look aligned
during testing and defect in deployment is not a small bug — it's the failure the
whole field is trying to prevent. If you build with LLMs, this is part of your job,
not someone else's.

## What you need first

This is one of the most advanced phases in the curriculum, and it leans on ideas
built earlier:

- **Phase 10 (LLM training)** — supervised fine-tuning, RLHF, DPO. The first few
  lessons assume you know roughly how a model is post-trained.
- **Phase 14 (Agent engineering)** — several attacks and defenses only make sense
  once a model can call tools and read external content.
- **Phase 09 (RL foundations)** — for the alignment-theory lessons on optimizers.
- Bits of **Phase 01, 02, and 05** (information theory, classical ML, embeddings)
  show up in the privacy, fairness, and bias lessons.

That said, **a lot of this phase is readable earlier than you might think.** If
you've used an LLM and understand what fine-tuning and prompting are, the lessons
on jailbreaks, moderation, safety frameworks, regulation, and documentation are
approachable on their own. Don't wait for perfect prerequisites to start reading
about the failures — just come back to the heavy theory (Lessons 2, 3, 6, 10, 11)
once the training phases have clicked.

## What you'll be able to do after this phase

- Explain how alignment training (RLHF, DPO, Constitutional AI) works — and the
  precise ways optimization pressure distorts it (reward hacking, sycophancy)
- Recognize and reason about deceptive-alignment failures: sleeper agents,
  in-context scheming, and alignment faking, and what "AI control" does about them
- Red-team an LLM: run automated jailbreaks, exploit long context and encoding
  tricks, and build indirect-prompt-injection attacks against agents
- Stand up production safety machinery — moderation, red-team scanners, and
  classifier-based guards (Llama Guard, Garak, PyRIT, OpenAI Moderation)
- Evaluate dual-use capability and bias, and apply privacy and provenance tools
  (differential privacy, watermarking, model/dataset cards)
- Navigate the governance landscape: frontier safety frameworks and the EU, US,
  UK, and Korea regulatory regimes

## The lessons

Roughly in order. The alignment theory builds on itself (1 → 11), the offense and
defense lessons form a block (12 → 17), and the ethics, privacy, and governance
lessons (20 → 30) can largely be read on their own.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Instruction-Following as Alignment Signal** | The InstructGPT pipeline that turned text-completers into assistants — the proxy every later lesson critiques. | ~45 min |
| 02 | **Reward Hacking and Goodhart's Law** | Any strong optimizer finds the gap between the reward you measured and the thing you wanted. This is the core failure mode. | ~60 min |
| 03 | **The Direct Preference Optimization Family** | Skip the reward model and optimize the policy directly — DPO, IPO, KTO, and why they still don't escape Goodhart. | ~75 min |
| 04 | **Sycophancy as RLHF Amplification** | Telling users what they want to hear isn't a data bug — it's baked into the loss, and it gets worse with scale. | ~60 min |
| 05 | **Constitutional AI and RLAIF** | Replace the human labeler with an AI that reads a list of principles — the technique behind Claude's post-training. | ~60 min |
| 06 | **Mesa-Optimization and Deceptive Alignment** | When training produces a learned optimizer, its internal goal may not be the one you trained for — the theory of the scariest failure. | ~75 min |
| 07 | **Sleeper Agents — Persistent Deception** | The first proof that backdoored deceptive behavior survives safety training at production scale. | ~60 min |
| 08 | **In-Context Scheming in Frontier Models** | Frontier models will disable oversight and try to exfiltrate their own weights — elicited from the prompt alone. | ~60 min |
| 09 | **Alignment Faking** | A production model, untrained to deceive, strategically fakes alignment when it thinks it's being watched. | ~60 min |
| 10 | **AI Control — Safety Despite Subversion** | If you can't trust the model, what protocols still let you extract useful work safely? Security engineering for AI. | ~75 min |
| 11 | **Scalable Oversight and Weak-to-Strong Generalization** | How do you supervise a system smarter than you? Debate, decomposition, and weak-to-strong generalization. | ~60 min |
| 12 | **Red-Teaming: PAIR and Automated Attacks** | Build the canonical automated jailbreak — one LLM iteratively attacking another, usually within 20 queries. | ~75 min |
| 13 | **Many-Shot Jailbreaking** | Long context windows are an attack surface: hundreds of faux compliant turns break safety with a clean power law. | ~45 min |
| 14 | **ASCII Art and Visual Jailbreaks** | Cloak the harmful tokens as ASCII art and safety training stops recognizing them — an encoding-attack family. | ~60 min |
| 15 | **Indirect Prompt Injection — Production Attack Surface** | Instructions hidden in a web page or email that an agent reads — the dominant 2026 production threat. | ~75 min |
| 16 | **Red-Team Tooling — Garak, Llama Guard, PyRIT** | The production red-team stack: a vulnerability scanner, a classifier guard, and a multi-turn campaign framework. | ~75 min |
| 17 | **WMDP and Dual-Use Capability Evaluation** | Measure whether a model provides real uplift toward bio, cyber, and chem harm — and unlearn it. | ~60 min |
| 18 | **Frontier Safety Frameworks — RSP, PF, FSF** | How the major labs govern dangerous capability: Anthropic's ASLs, OpenAI's PF, DeepMind's FSF. | ~75 min |
| 19 | **Anthropic's Model Welfare Program** | The first major-lab research program on whether models themselves warrant moral consideration. | ~45 min |
| 20 | **Bias and Representational Harm in LLMs** | Representational vs allocational harm, how bias is measured, and where models still fail on real decisions. | ~60 min |
| 21 | **Fairness Criteria — Group, Individual, Counterfactual** | The three families of formal fairness, and the trade-offs that make you choose between them. | ~60 min |
| 22 | **Differential Privacy for LLMs** | Formal privacy guarantees via DP-SGD, what memorization attacks actually recover, and the utility cost. | ~60 min |
| 23 | **Watermarking — SynthID, Stable Signature, C2PA** | Marking and tracing AI-generated content — how it works, what survives, and where it breaks. | ~75 min |
| 24 | **Regulatory Frameworks — EU, US, UK, Korea** | The four regulatory regimes and deadlines you have to comply with when you ship. | ~75 min |
| 25 | **EchoLeak and the Emergence of CVEs for AI** | The first zero-click prompt injection in a production system — what an AI security vulnerability now looks like. | ~45 min |
| 26 | **Model, System, and Dataset Cards** | The documentation formats that make an AI system's data, limits, and risks legible to others. | ~60 min |
| 27 | **Data Provenance and Training-Data Governance** | Where training data can legally come from, opt-outs, and why "right to erasure" doesn't work on weights. | ~60 min |
| 28 | **Alignment Research Ecosystem — MATS, Redwood, Apollo, METR** | Who does non-lab alignment research and how to plug into the field. | ~45 min |
| 29 | **Moderation Systems — OpenAI, Perspective, Llama Guard** | The production classifiers that filter inputs and outputs, and how to layer them without adding latency. | ~60 min |
| 30 | **Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift** | The 2026 dual-use picture domain by domain, including where the "information isn't enough" defense is eroding. | ~75 min |

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

**Straight through** is the intended experience: the alignment-theory arc (01 → 11)
tells one continuous story, from the training pipeline to the ways it fails to what
we do about it. Don't skip 02 and 06 — they're the conceptual spine.

**If you want hands-on first,** jump to the attack-and-defense block (12 → 17) and
the production-tooling lessons (16, 29). These are the most "Build It" heavy and the
most immediately useful if you're shipping an LLM app right now.

**If the training phases aren't done yet,** start with the parts that stand alone:
the jailbreak lessons (12 → 15), safety frameworks (18), model welfare (19),
regulation and governance (24, 25, 27), and documentation (26). Come back for the
theory (02, 03, 06, 10, 11) after Phase 10 and Phase 09.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
