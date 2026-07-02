# Phase 12: Multimodal AI

> Models that see, hear, read, and reason across modalities.

## Why this phase exists

Up to now, most of what you've built lives in one modality at a time: text in,
text out. But the world isn't text-only. A useful model has to look at a photo,
read a receipt, watch a video, listen to a voice, and tie all of it back to
language it can reason about. That's what "multimodal" means — one model that
handles pictures, sound, and words together instead of a separate tool for each.

This phase traces how that capability was actually built, in the order the field
figured it out. You start with the single primitive that makes it all possible —
turning an image into tokens a transformer can eat — and end with agents that read
a screenshot and click the right button. Every step in between is a real system
(CLIP, BLIP-2, LLaVA, Qwen-VL, Whisper, and their descendants) that a 2026 frontier
model still carries inside it. Learn the lineage and the modern models stop looking
like magic.

## What you need first

This is a phase where the prerequisites genuinely matter — multimodal AI is where
several earlier tracks meet:

- **Phase 4 (Computer Vision)** — how images become features in the first place.
- **Phase 5 (NLP)** — the language side that every one of these models reasons in.
- **Phase 7 (Transformers)** — the architecture underneath *all* of it. If you're
  shaky on attention and tokens, review Phase 7 before starting here.

A few later lessons also lean on Phase 6 (Speech and Audio), Phase 8 (Generative
AI), and Phase 11 (LLM Engineering) — but each lesson names exactly what it needs at
the top, so you can pull those in as you go. You don't have to hold the whole map in
your head. If a term is new, the lesson that introduces it explains it from the
problem up.

## What you'll be able to do after this phase

- Explain how an image, a video, or an audio clip gets turned into tokens a
  transformer can process — and build that pipeline yourself
- Read a modern vision-language model's architecture and name each part (encoder,
  connector, language backbone) and why it's there
- Build the core pieces of the models everyone actually uses — a contrastive
  trainer, a Q-Former bridge, a LLaVA-style projector
- Reason about the real design trade-offs: discrete vs. continuous image tokens,
  one encoder vs. two, post-hoc vision vs. native multimodal pretraining
- Handle any-resolution images, long videos, audio, and documents — not just tidy
  224x224 squares
- Assemble a multimodal agent that perceives a screen, reasons, and acts

## The lessons

Do them in order — this phase is a chronology, and each lesson assumes the one
before it. The early lessons build the primitives; the middle explores the design
space; the later ones specialize into video, audio, documents, and agents.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Vision Transformers and the Patch-Token Primitive** | The single idea every multimodal model starts from: an image becomes a sequence of patch tokens a transformer can process. | ~2 hr |
| 02 | **CLIP and Contrastive Vision-Language Pretraining** | Aligns images and text in one shared space using only web image-caption pairs — the vision tower inside nearly every modern VLM. | ~3 hr |
| 03 | **From CLIP to BLIP-2 — Q-Former as Modality Bridge** | A small trainable bridge that lets a frozen vision encoder talk to a frozen LLM — the ancestor of every adapter-based VLM. | ~3 hr |
| 04 | **Flamingo and Gated Cross-Attention for Few-Shot VLMs** | Interleaves images, video, and text in one sequence and learns in-context — the pattern behind Gemini's interleaved inputs. | ~2 hr |
| 05 | **LLaVA and Visual Instruction Tuning** | The most-copied multimodal recipe on the planet: swap the fancy bridge for a simple MLP and just concatenate tokens. Simpler won. | ~3 hr |
| 06 | **Any-Resolution Vision: Patch-n'-Pack and NaFlex** | Real images aren't squares — this is how VLMs handle receipts, charts, and screenshots without throwing away the signal. | ~2 hr |
| 07 | **Open-Weight VLM Recipes: What Actually Matters** | Distills a forest of ablation tables into the few results that hold: encoder and data matter more than connector architecture. | ~3 hr |
| 08 | **LLaVA-OneVision: Single-Image, Multi-Image, Video in One Model** | One curriculum that trains a single model to handle images, multiple images, and video — and shows skills transfer between them. | ~3 hr |
| 09 | **Qwen-VL Family and Dynamic-FPS Video** | The most influential open VLM lineage — each generation made one architectural bet the whole ecosystem then copied. | ~2 hr |
| 10 | **InternVL3: Native Multimodal Pretraining** | Trains text and images together from step one instead of bolting vision onto a finished LLM — and matches frontier models doing it. | ~2 hr |
| 11 | **Chameleon and Early-Fusion Token-Only Multimodal Models** | Puts images and text in one shared vocabulary and one loss — so the model can generate mixed image-and-text output. | ~3 hr |
| 12 | **Emu3: Next-Token Prediction for Image and Video Generation** | One decoder-only transformer, next-token prediction only, beats specialized image and video generators. Better tokenizer plus scale. | ~2 hr |
| 13 | **Transfusion: Autoregressive Text + Diffusion Image in One Transformer** | Keeps images continuous and trains one transformer with two losses — the design cousin of Stable Diffusion 3's backbone. | ~3 hr |
| 14 | **Show-o and Discrete-Diffusion Unified Models** | Text via next-token prediction, images via masked discrete diffusion, both in one transformer — a parallel, few-step image generator. | ~2 hr |
| 15 | **Janus-Pro: Decoupled Encoders for Unified Multimodal Models** | Understanding and generation want different image features, so use two encoders and share the body — beating DALL-E 3 at 7B. | ~2 hr |
| 16 | **MIO and Any-to-Any Streaming Multimodal Models** | Four tokenizers (text, image, speech, music), one transformer, any modality in to any modality out — the open answer to GPT-4o. | ~2 hr |
| 17 | **Video-Language Models: Temporal Tokens and Grounding** | Video has ordering and timing a stack of photos can't capture — this is how models represent when things happen. | ~3 hr |
| 18 | **Long-Video Understanding at Million-Token Context** | An hour of video is tens of millions of tokens — compares the strategies (long context, ring attention, agentic retrieval) that make it tractable. | ~3 hr |
| 19 | **Audio-Language Models: the Whisper to Audio Flamingo 3 Arc** | Moves from transcribing speech to reasoning about sound — instruments, emotion, events — by bolting audio encoders onto LLMs. | ~3 hr |
| 20 | **Omni Models: Qwen2.5-Omni and the Thinker-Talker Split** | The architecture and latency budget behind real-time voice-and-video dialogue — a Thinker that reasons and a Talker that speaks. | ~3 hr |
| 21 | **Embodied VLAs: RT-2, OpenVLA, π0, GR00T** | Vision-language-action: a single model that sees, reads, and acts — web-scale knowledge transferred to robot control. | ~3 hr |
| 22 | **Document and Diagram Understanding** | Documents have layout, tables, and structure plain image models miss — the arc from OCR pipelines to OCR-free VLMs. | ~3 hr |
| 23 | **ColPali and Vision-Native Document RAG** | Skip OCR entirely: embed the page image directly and retrieve on it, keeping the figures, fonts, and layout text-RAG throws away. | ~3 hr |
| 24 | **Multimodal RAG and Cross-Modal Retrieval** | Production retrieval across text, images, audio, and video — cross-modal search, fusion, grounding, and evaluation for real workflows. | ~3 hr |
| 25 | **Multimodal Agents and Computer-Use (Capstone)** | Pulls every thread together: an agent that reads a screen, reasons with tools, grounds coordinates, and completes a workflow. | ~4 hr |

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

**Go in order.** Unlike Phase 0, this phase is a story told in sequence — lesson 05
assumes 02, lesson 08 assumes 06, and so on. The chronology *is* the lesson.

**If you're short on time,** the spine of the phase is **01 → 02 → 03 → 05** (the
primitives and the recipe everyone copies), then **06, 09, and 10** for how modern
VLMs actually work. Come back for the generation lessons (11–16) and the
specialization tracks — video (17–18), audio (20), documents (22–24) — when you need
them.

**Whatever order you take,** finish with **25 (the capstone)**. It ties perception,
reasoning, grounding, and evaluation into one working multimodal agent, and it's the
clearest proof to yourself that the phase stuck.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
