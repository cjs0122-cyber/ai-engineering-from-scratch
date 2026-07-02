# Phase 6: Speech & Audio

> The other half of human communication. Hear, understand, speak.

## Why this phase exists

So far you've taught machines to read and write. But most human communication
isn't typed — it's spoken, heard, and sung. This phase is the other half:
teaching machines to *hear* (turn sound into something a model understands),
*understand* (recognize words, speakers, and meaning), and *speak* (turn text
back into a voice).

Audio feels intimidating because it starts as a wall of numbers — a waveform. The
whole trick of the field is turning that wall into pictures (spectrograms) and
then into tokens a transformer can chew on, the same way you already handle text.
Once you see that ladder, every ASR, TTS, voice-cloning, and music-generation
system in 2026 is a variation on the same few ideas. This phase walks you up that
ladder from raw sound to a full voice assistant that listens, thinks, and talks
back.

## What you need first

This is not a beginner phase. It leans on earlier work:

- **Phase 3 (Deep Learning)** — you'll use CNNs, RNNs, and the training loop
  constantly. Spectrograms are images; audio models are the networks you already
  built, pointed at sound.
- **Phase 1 (Math Foundations)** — vectors and matrices throughout, plus
  probability. The Fourier transform (turning a signal into its frequencies) shows
  up on day one, but the first lesson teaches it from the ground up.
- **Phase 5 (NLP)** — attention, seq2seq, and embeddings reappear the moment we
  hit speech recognition and text-to-speech.

If any of that feels rusty, that's fine — each lesson lists its exact
prerequisites, and the early lessons rebuild the audio-specific pieces from
scratch. You don't need perfect recall of every earlier phase, just the habits.

## What you'll be able to do after this phase

- Turn raw audio into spectrograms and mel features, the input every audio model
  expects
- Build and evaluate audio classifiers, speech recognizers (ASR), and
  text-to-speech (TTS) systems
- Fine-tune Whisper and reason about the modern transformer-based audio stack
- Recognize and verify speakers, clone voices, and defend against spoofed audio
- Run audio in real time — voice activity detection, turn-taking, and full-duplex
  speech-to-speech
- Stitch it all together into a working voice assistant, and measure any audio
  system with the right 2026 metric

## The lessons

Do them in order — the phase is built as a ladder, and later lessons assume the
earlier ones.

| # | Lesson | Why it matters | Time |
|---|--------|----------------|------|
| 01 | **Audio Fundamentals — Waveforms, Sampling, Fourier Transform** | The first rung: how sound becomes numbers, and how sampling and Fourier turn a waveform into something a model can use. | ~45 min |
| 02 | **Spectrograms, Mel Scale & Audio Features** | Neural nets don't eat raw waveforms — they eat mel spectrograms. This one preprocessing choice underpins every later lesson. | ~45 min |
| 03 | **Audio Classification — From k-NN on MFCCs to AST and BEATs** | "Dog bark vs siren," language ID, and more — the entry-point task that teaches audio features and evaluation. | ~75 min |
| 04 | **Speech Recognition (ASR) — CTC, RNN-T, Attention** | Turning speech into text, via the three sequence models (CTC, RNN-T, attention) that make it possible. | ~45 min |
| 05 | **Whisper — Architecture & Fine-Tuning** | The 2026 reference ASR: one encoder-decoder transformer, 99 languages, and how to fine-tune it for your own data. | ~75 min |
| 06 | **Speaker Recognition & Verification** | Not "what did they say?" but "who said it?" — embeddings, cosine similarity, and the EER number production hinges on. | ~45 min |
| 07 | **Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro** | The inverse of ASR: text → tokens → mel → waveform, with a default model at each step that runs on a laptop. | ~75 min |
| 08 | **Voice Cloning & Voice Conversion** | Speak in someone else's voice, or rewrite a voice while keeping the words — both built on separating speaker identity from content. | ~75 min |
| 09 | **Music Generation — MusicGen, Stable Audio, Suno, and the Licensing Earthquake** | Generating music with open and commercial models, plus the 2025-2026 legal upheaval that reshaped the field. | ~75 min |
| 10 | **Audio-Language Models — Qwen2.5-Omni, Audio Flamingo, GPT-4o Audio** | Models that reason over speech, sound, and music together — where open models have essentially caught closed ones. | ~45 min |
| 11 | **Real-Time Audio Processing** | Processing the next 20 milliseconds before the next 20 arrive — the latency budget every conversational AI lives by. | ~75 min |
| 12 | **Build a Voice Assistant Pipeline — The Phase 6 Capstone** | Lessons 01-11 stitched into an assistant that listens, reasons, and talks back — an integration problem, not a research one. | ~120 min |
| 13 | **Neural Audio Codecs — EnCodec, SNAC, Mimi, DAC and the Semantic-Acoustic Split** | Turning waveforms into discrete tokens a transformer can predict — the biggest architectural shift in audio since the Transformer. | ~60 min |
| 14 | **Voice Activity Detection & Turn-Taking — Silero, Cobra, and the Flush Trick** | Is the user speaking, and are they done? Get either wrong and your assistant cuts people off or never shuts up. | ~45 min |
| 15 | **Streaming Speech-to-Speech — Moshi, Hibiki, and Full-Duplex Dialogue** | A single model that listens and speaks at once — the new reference design that abandons the ASR → LLM → TTS pipeline. | ~75 min |
| 16 | **Voice Anti-Spoofing & Audio Watermarking — ASVspoof 5, AudioSeal, WaveVerify** | Voice cloning outran its defenses; this is how you detect fake speech and watermark real speech before you ship. | ~75 min |
| 17 | **Audio Evaluation — WER, MOS, UTMOS, MMAU, FAD, and the Open Leaderboards** | You can't ship what you can't measure — the right 2026 metric and leaderboard for every audio task. | ~60 min |

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

Go straight down 01 → 17. The phase is deliberately ordered as a ladder: 01-02
give you the audio-to-features foundation everything else needs, 03-10 cover the
core tasks (classification, ASR, TTS, cloning, music, audio-language models), and
11-12 bring it into real time and the capstone voice assistant.

Lessons 13-17 are the production layer — codecs, turn-taking, full-duplex speech,
anti-spoofing, and evaluation. If you're short on time, you can treat 13, 15, and
17 (the **Learn** lessons) as reading and focus your hands-on energy on the
**Build** lessons. But the capstone in lesson 12 pays off most if you've done
everything before it.

See [ROADMAP.md](../../ROADMAP.md) for the full lesson plan across all 20 phases.
