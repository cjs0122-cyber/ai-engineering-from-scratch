# Phase 8: Generative AI

> Create images, video, audio, 3D, and more.

## Why this phase exists

Most of the AI you've built so far *reads* the world: it classifies an image,
predicts a number, answers a question. This phase is about the other direction —
teaching a model to *make* things. Give it noise and a prompt, and it produces a
photo that never existed, a five-second video clip, a piece of music, or a 3D
object.

That's what "generative AI" means: models that create images, video, audio, 3D
shapes, and more. The images you see from Stable Diffusion, Flux, and Midjourney,
the video from Sora and Veo, the voice clones and music tools — all of it comes
from a handful of ideas you'll build here, one at a time, from the ground up. By
the end you'll know not just how to *use* these tools, but why they work and where
they break.

## What you need first

This is a phase that builds on real foundations. Before you start, you should have:

- **Phase 3 (Deep Learning Core)** — you'll lean on backprop, CNNs, optimizers, and
  normalization constantly. Generative models *are* neural networks trained with a
  clever loss.
- **Phase 7 (Transformers)** — the attention and Vision Transformer ideas show up in
  modern diffusion and video models.
- **Phase 1 (Math Foundations)** — probability, distributions, and a little calculus.
  Sampling from a distribution is the whole game here.

If some of that feels rusty, that's fine — the lessons re-introduce each idea as it
comes up, and every lesson lists exactly which earlier ones it depends on. You don't
need a fancy GPU either: the demos are small and run on a normal laptop. You're
learning the mechanisms, not training a production model.

## What you'll be able to do after this phase

- Explain the five families of generative models and pick the right one for a task
- Build a VAE, a GAN, and a diffusion model from scratch and understand each trade-off
- Understand how Stable Diffusion actually works — latent space, VAE, and denoising
- Steer image generation with ControlNet, LoRA, and inpainting instead of just text
- Reason about how video, audio, and 3D generation extend the same core ideas
- Evaluate generative models honestly with FID, CLIP score, and human preference — and
  spot the ways each metric can be gamed

## The lessons

Do them in order. This phase tells a story: each generation of models fixes a
weakness in the one before it, so the sequence matters more than usual.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Generative Models — Taxonomy & History** | The map of the whole field — every model fits in one of five families, and picking the right one saves weeks. | ~45 min |
| 02 | **Autoencoders & Variational Autoencoders (VAE)** | One trick turns a compressor into a sampler — and that trick is the input layer of every modern image model. | ~75 min |
| 03 | **GANs — Generator vs Discriminator** | Two networks fighting until the fakes fool a critic — still the sharpest samples in narrow domains. | ~75 min |
| 04 | **Conditional GANs & Pix2Pix** | How you control what a GAN makes by attaching a label, an image, or a sentence. | ~75 min |
| 05 | **StyleGAN** | The architecture that made photorealistic faces a solved problem by untangling the latent space. | ~45 min |
| 06 | **Diffusion Models — DDPM from Scratch** | Add noise, then learn to remove it — the loop that powers nearly every mainstream image, video, and audio model today. | ~75 min |
| 07 | **Latent Diffusion & Stable Diffusion** | Run diffusion inside a VAE's compact latent space instead of raw pixels — the single idea behind Stable Diffusion. | ~75 min |
| 08 | **ControlNet, LoRA & Conditioning** | Steer a frozen model with depth maps and poses, and fine-tune billions of parameters by training millions. | ~75 min |
| 09 | **Inpainting, Outpainting & Image Editing** | Fixing and extending existing images — where most real, billable image work actually happens. | ~75 min |
| 10 | **Video Generation** | The same diffusion theory in one more dimension, at 10-100x the compute — from Sora to the open-weights stack. | ~45 min |
| 11 | **Audio Generation** | Compress audio to discrete tokens with a neural codec, then generate the tokens — the recipe every 2026 audio model shares. | ~45 min |
| 12 | **3D Generation** | Turning a single prompt or photo into a 3D object with multi-view diffusion and Gaussian splatting. | ~45 min |
| 13 | **Flow Matching & Rectified Flows** | Train straight paths from noise to data so you need fewer steps — why SD3 and Flux got faster. | ~45 min |
| 14 | **Evaluation — FID, CLIP Score, Human Preference** | The three numbers every leaderboard cites, and the failure mode hiding inside each one. | ~45 min |
| 19 | **Visual Autoregressive Modeling (VAR): Next-Scale Prediction** | Predict an image scale by scale instead of denoising step by step — GPT-style scaling laws for image generation. | ~90 min |

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

Go straight down the list. The order isn't arbitrary — VAEs (02) feed latent
diffusion (07), GANs (03) lead into conditioning (04) and StyleGAN (05), and
diffusion (06) is the trunk that video (10), audio (11), 3D (12), and flow matching
(13) all branch off of.

**If you're short on time,** the spine of the phase is **01 → 02 → 03 → 06 → 07 →
08**. Those six give you the mental model behind almost every image tool shipping
today. Come back for the modality-specific lessons (10-12), the speed tricks (13),
evaluation (14), and VAR (19) when you need them.

**Don't skip the "Build It" steps.** Generative models feel like magic until you've
written the sampling loop yourself once — then they're just code.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
