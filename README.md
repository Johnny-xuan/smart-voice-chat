# SmartVoice Chat 🗣️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Clawdbot Skill](https://img.shields.io/badge/Clawdbot-Skill-blue.svg)](https://github.com/clawdbot/clawdbot)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/clawdbot/clawdbot)
[![Offline](https://img.shields.io/badge/offline-ready-green.svg)](https://github.com/k2-fsa/sherpa-onnx)

**Intelligent Voice Conversation Skill for Clawdbot**

Offline voice-to-voice interaction powered by Sherpa-ONNX. Automatically detects voice/text input and replies in the same format.

## ✨ Features

- 🎯 **Auto Detection** - Automatically detects voice vs text input
- 🗣️ **Voice-to-Voice** - Replies in same format (voice→voice, text→text)
- 🌏 **Chinese-English** - Native mixed language support
- 🔒 **Fully Offline** - No cloud, privacy-preserving
- 📱 **Telegram Ready** - Outputs OGG format for voice messages

## 📋 System Requirements

### Operating System
- **macOS**: 11.0+ (Big Sur or later)
- **Linux**: Ubuntu 20.04+, Debian 11+, or equivalent
- **Arch**: x86_64 or ARM64 (Apple Silicon supported)

### Dependencies

| Component | Version | Installation |
|-----------|---------|---------------|
| **Clawdbot** | Latest | `npm install -g clawdbot@latest` |
| **Node.js** | 22+ | `brew install node` (macOS) or `nvm install 22` |
| **Python** | 3.8+ | `brew install python3` (macOS) or `apt install python3` |
| **FFmpeg** | 4.0+ | `brew install ffmpeg` (macOS) or `apt install ffmpeg` |
| **pip3** | Latest | Included with Python 3 |

### Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 4 GB | 8 GB+ |
| **Storage** | 2 GB free | 4 GB+ free (for models) |
| **CPU** | Any modern CPU | Apple Silicon M1/M2/M3 or Intel Core i5+ |

### Model Selection by Hardware

**Important**: This skill uses **one STT model** + **one TTS model**. Choose the STT model based on your RAM and language needs.

#### STT Model Options (Speech-to-Text)

| Model | Date | Size | Language | WER | Best For |
|-------|------|------|----------|-----|----------|
| `sherpa-onnx-zipformer-ctc-zh-int8-2025-07-03` | 2025-07 | 350 MB | Chinese | 1.74% | **Latest, balanced** |
| `sherpa-onnx-paraformer-zh-small-2024-03-09` | 2024-03 | 74 MB | Chinese | - | **4GB RAM systems** |
| `sherpa-onnx-streaming-zh-en-2024-03-12` | 2024-03 | 490 MB | Chinese-English | - | **Real-time transcription** |
| `sherpa-onnx-paraformer-zh-2024-03-09` | 2024-03 | 950 MB | Chinese-English | - | **Best accuracy (8GB+)** |
| `sherpa-onnx-paraformer-en-2024-03-09` | 2024-03 | 974 MB | **English** | - | **English speakers** |

#### TTS Model Options (Text-to-Speech)

| Model | Size | Language/Voice | Best For |
|-------|------|----------------|----------|
| `vits-melo-tts-zh_en` | 163 MB | Chinese-English (Female) | **Mixed CEN-EN speech (推荐)** |
| `vits-piper-en_US-lessac-high` | 500 MB | English (Male) | **English-only TTS** |
| `vits-piper-zh_CN-huayan-medium` | 300 MB | Chinese (Female) | **Chinese-only TTS** |

#### Quick Decision Guide

| RAM | STT Model | TTS Model | Total |
|-----|-----------|-----------|-------|
| **4 GB** | `paraformer-zh-small` (74MB) | `vits-melo-tts-zh_en` (163MB) | ~240 MB |
| **4-8 GB (Chinese)** | `zipformer-ctc-zh-int8` (350MB) | `vits-melo-tts-zh_en` (163MB) | ~510 MB |
| **4-8 GB (Mixed)** | `streaming-zh-en` (490MB) | `vits-melo-tts-zh_en` (163MB) | ~650 MB |
| **8 GB+ (Chinese)** | `zipformer-ctc-zh-int8` (350MB) | `vits-melo-tts-zh_en` (163MB) | ~510 MB |
| **8 GB+ (Mixed)** | `paraformer-zh` (950MB) | `vits-melo-tts-zh_en` (163MB) | ~1.1 GB |
| **8 GB+ (English)** | `paraformer-en` (974MB) | `vits-piper-en_US-lessac` (500MB) | ~1.5 GB |

**Recommended Setup** (for most users):
- STT: `sherpa-onnx-zipformer-ctc-zh-int8-2025-07-03` (latest, WER 1.74%)
- TTS: `vits-melo-tts-zh_en` (natural bilingual voice)

**Apple Silicon Tip**: M1/M2/M3 chips handle all models efficiently due to neural engine acceleration.

### Network Requirements
- **Required**: For downloading models and dependencies (initial setup only)
- **Runtime**: Fully offline after installation

## 🔧 Sherpa-ONNX Models

### STT (Speech-to-Text) Options

| Model | Date | Language | Size | WER | Download |
|-------|------|----------|------|-----|----------|
| [zipformer-ctc-zh-int8](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-zipformer-ctc-zh-int8-2025-07-03.tar.bz2) | 2025-07 | Chinese | 350MB | 1.74% | [tar.bz2](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-zipformer-ctc-zh-int8-2025-07-03.tar.bz2) |
| [paraformer-zh-small](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-paraformer-zh-small-2024-03-09.tar.bz2) | 2024-03 | Chinese-English | 74MB | - | [tar.bz2](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-paraformer-zh-small-2024-03-09.tar.bz2) |
| [streaming-zh-en](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-streaming-zh-en-2024-03-12.tar.bz2) | 2024-03 | Chinese-English | 490MB | - | [tar.bz2](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-streaming-zh-en-2024-03-12.tar.bz2) |
| [paraformer-zh](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-paraformer-zh-2024-03-09.tar.bz2) | 2024-03 | Chinese-English | 950MB | - | [tar.bz2](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-paraformer-zh-2024-03-09.tar.bz2) |
| [paraformer-en](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-paraformer-en-2024-03-09.tar.bz2) | 2024-03 | English | 974MB | - | [tar.bz2](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-paraformer-en-2024-03-09.tar.bz2) |

**Recommended**: `zipformer-ctc-zh-int8-2025-07-03` for Chinese users (latest, WER 1.74%)

### TTS (Text-to-Speech) Options

#### Chinese-English (Recommended)

| Model | Voice | Size | Download |
|-------|-------|------|----------|
| **vits-melo-tts-zh_en** | Female | 163MB | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-melo-tts-zh_en.tar.bz2) |
| **vits-piper-zh_CN-huayan** | Female | 300MB | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-zh_CN-huayan-medium.tar.bz2) |

#### English Voices

| Model | Accent | Voice | Size | Download |
|-------|--------|-------|------|----------|
| **vits-piper-en_US-lessac-high** | American | Male | 500MB | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-lessac-high.tar.bz2) |
| **vits-piper-en_US-glados** | American | Female | 300MB | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-glados-medium.tar.bz2) |
| **vits-piper-en_GB-semaine** | British | Female | 300MB | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_GB-semaine-medium.tar.bz2) |
| **vits-piper-en_GB-lessac** | British | Male | 500MB | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_GB-lessac-medium.tar.bz2) |

#### Japanese

| Model | Voice | Size | Download |
|-------|-------|------|----------|
| **vits-vctk** | Multi-speaker | 500MB+ | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-vctk.tar.bz2) |

#### Spanish

| Model | Voice | Size | Download |
|-------|-------|------|----------|
| **vits-piper-es_ES-vox** | Female | 300MB | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-es_ES-vox-medium.tar.bz2) |

#### French

| Model | Voice | Size | Download |
|-------|-------|------|----------|
| **vits-piper-fr_FR-siwis** | Female | 300MB | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-fr_FR-siwis-medium.tar.bz2) |

#### German

| Model | Voice | Size | Download |
|-------|-------|------|----------|
| **vits-piper-de_DE-thorsten-medium** | Male | 300MB | [Download](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-de_DE-thorsten-medium.tar.bz2) |

#### Kokoro Multi-Language (103+ Speakers)

| Model | Languages | Speakers | Size |
|-------|-----------|----------|------|
| [kokoro-multi-lang-v1_0](https://huggingface.co/csukuangfj/kokoro-multi-lang-v1_0.onnx) | Multi | 103+ | Large |

**Recommended**: `vits-melo-tts-zh_en` for mixed Chinese-English.

### 🎧 Try Before You Download

Listen to samples at the [Sherpa-ONNX Text-to-Speech Space](https://huggingface.co/spaces/k2-fsa/text-to-speech) on HuggingFace.

### 📚 More Languages and Models

Sherpa-ONNX supports **40+ languages** and **100+ pre-trained models**:

- **Full Model List**: [https://k2-fsa.github.io/sherpa/onnx/tts/all/](https://k2-fsa.github.io/sherpa/onnx/tts/all/)
- **VITS Models**: [https://k2-fsa.github.io/sherpa/onnx/tts/pretrained_models/vits.html](https://k2-fsa.github.io/sherpa/onnx/tts/pretrained_models/vits.html)
- **GitHub Releases**: [https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models](https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models)

Supported languages include: Arabic, Bulgarian, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hindi, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Romanian, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian, Vietnamese, and more.

## 📦 Installation

### Quick Install (Recommended)

1. **Clone this repository**
```bash
git clone https://github.com/Johnny-xuan/smart-voice-chat.git ~/smart-voice-chat
```

2. **Download Sherpa-ONNX runtime**
```bash
# macOS
curl -L https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.23/sherpa-onnx-v1.12.23-osx-universal2-shared.tar.bz2 | tar xjf -
mkdir -p ~/.clawdbot/sherpa-asr/runtime
mv sherpa-onnx*/* ~/.clawdbot/sherpa-asr/runtime/
```

3. **Download models**
```bash
# STT Model (Chinese - Latest 2025)
mkdir -p ~/.clawdbot/sherpa-asr/models
cd ~/.clawdbot/sherpa-asr/models
curl -L https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-zipformer-ctc-zh-int8-2025-07-03.tar.bz2 | tar xjf -

# TTS Model (Chinese-English)
mkdir -p ~/.clawdbot/tools/sherpa-onnx-tts/models
cd ~/.clawdbot/tools/sherpa-onnx-tts/models
curl -L https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-melo-tts-zh_en.tar.bz2 | tar xjf -
```

4. **Install to Clawdbot skills**
```bash
# Find Clawdbot skills directory
CLAWDBOT_SKILLS=$(npm root -g)/clawdbot@*/node_modules/clawdbot/skills

# Copy skill
cp -r ~/smart-voice-chat "$CLAWDBOT_SKILLS/"

# Verify
clawdbot skills list | grep smart-voice
```

Expected output: `│ ✓ ready │ 🗣️ smart-voice- │ ...`

5. **Restart Clawdbot**
```bash
pkill -9 clawdbot
clawdbot-gateway &
```

## ⚙️ Configuration

### Environment Variables (Optional)

Add to `~/.clawdbot/clawdbot.json`:

```json
{
  "skills": {
    "entries": {
      "smart-voice-chat": {
        "env": {
          "SMART_VOICE_CHAT_STT_MODEL": "~/.clawdbot/sherpa-asr/models/sherpa-onnx-zipformer-ctc-zh-int8-2025-07-03",
          "SMART_VOICE_CHAT_TTS_MODEL": "~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en",
          "SMART_VOICE_CHAT_OUTPUT_DIR": "/tmp/smart-voice-chat"
        }
      }
    }
  }
}
```

### SKILL.md Format

The `SKILL.md` frontmatter must use valid JSON:

```yaml
---
name: smart-voice-chat
description: "Voice conversation with auto-detection (voice-to-voice, text-to-text)"
metadata: {"clawdbot":{"emoji":"🗣️","os":["darwin","linux"],"requires":{"anyBins":["ffmpeg"]}}}
---
```

**Important**:
- Always wrap `description` in quotes
- Avoid special characters (use `to` instead of `→`)
- `requires` only supports: `bins`, `anyBins`, `env`, `config`
- Does NOT support: `python` field (ignored by Clawdbot)

## 💡 Usage

### Default Mirror Mode

```
You: [Voice message] "What's the weather like today?"
AI:  [Voice + Text] "It's sunny today, 25°C"
```

```
You: "What's the weather like today?"
AI:  "It's sunny today, 25°C" [Text only]
```

### Override with Keywords

```
You: "Reply with voice: Will it rain tomorrow?"
AI:  [Voice only] "It might rain lightly tomorrow"
```

```
You: "Reply with text: What time is it now?"
AI:  [Text only] "It's 4 PM now"
```

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| STT | Sherpa-ONNX Zipformer CTC (zh, int8, WER 1.74%) |
| TTS | Sherpa-ONNX VITS-Melo (zh-en) |
| Audio | FFmpeg (WAV → OGG/OPUS) |
| Language | Python 3 + Bash |

## 🐛 Troubleshooting

### Skill not showing in `clawdbot skills list`

1. Check SKILL.md syntax:
```bash
head -5 ~/.clawdbot/skills/smart-voice-chat/SKILL.md
```

2. Verify FFmpeg is installed:
```bash
which ffmpeg
```

3. Check logs:
```bash
tail -50 ~/.clawdbot/logs/gateway.err.log
```

### OGG conversion fails

Install FFmpeg:
```bash
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Ubuntu/Debian
```

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 🙏 Acknowledgments

- [Clawdbot](https://github.com/clawdbot/clawdbot) - AI Agent Framework
- [Sherpa-ONNX](https://github.com/k2-fsa/sherpa-onnx) - Offline speech processing
- [Paraformer](https://github.com/alibaba-damo-academy/FunASR) - Alibaba's ASR model
- [VITS-Melo](https://github.com/myshell-ai/MeloTTS) - MyShell's TTS model

---

**Author**: Johnny
**GitHub**: [smart-voice-chat](https://github.com/Johnny-xuan/smart-voice-chat)
