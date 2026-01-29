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

### Network Requirements
- **Required**: For downloading models and dependencies (initial setup only)
- **Runtime**: Fully offline after installation

## 🔧 Sherpa-ONNX Models

### STT (Speech-to-Text) Options

| Model | Language | Size | Speed | Accuracy |
|-------|----------|------|-------|----------|
| [sherpa-onnx-paraformer-zh-2024-03-09](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-paraformer-zh-2024-03-09.tar.bz2) | Chinese | 950MB | Fast | High |
| [sherpa-onnx-streaming-zh-en-2024-03-12](https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-streaming-zh-en-2024-03-12.tar.bz2) | Chinese-English | 490MB | Very Fast | Medium |

**Recommended**: `sherpa-onnx-paraformer-zh-2024-03-09` for best accuracy.

### TTS (Text-to-Speech) Options

| Model | Language | Voice | Size |
|-------|----------|-------|------|
| [vits-melo-tts-zh_en](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-melo-tts-zh_en.tar.bz2) | Chinese-English | Female | 163MB |
| [vits-piper-en_US-lessac-high](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-lessac-high.tar.bz2) | English | Male | 500MB |

**Recommended**: `vits-melo-tts-zh_en` for mixed Chinese-English.

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
# STT Model (Chinese)
mkdir -p ~/.clawdbot/sherpa-asr/models
cd ~/.clawdbot/sherpa-asr/models
curl -L https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-paraformer-zh-2024-03-09.tar.bz2 | tar xjf -

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
          "SMART_VOICE_CHAT_STT_MODEL": "~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09",
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
You: [Voice message] "今天天气怎么样"
AI:  [Voice + Text] "今天晴天，气温25度"
```

```
You: "今天天气怎么样"
AI:  "今天晴天，气温25度" [Text only]
```

### Override with Keywords

```
You: "用语音回答：明天会下雨吗"
AI:  [Voice only] "明天可能有小雨"
```

```
You: "用文字回答：现在几点了"
AI:  [Text only] "现在是下午4点"
```

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| STT | Sherpa-ONNX Paraformer (zh-en) |
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
