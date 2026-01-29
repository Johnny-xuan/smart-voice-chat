# SmartVoice Chat 🗣️

**Intelligent Voice Conversation Skill for Clawdbot**

Offline voice-to-voice interaction powered by Sherpa-ONNX. Auto-detects voice/text input and replies in the same format.

## ✨ Features

- 🎯 **Auto Detection** - Automatically detects voice vs text input
- 🗣️ **Voice-to-Voice** - Replies in the same format (voice→voice, text→text)
- 🌏 **Chinese-English** - Native mixed language support
- 🔒 **Fully Offline** - No cloud, privacy-preserving
- 📱 **Telegram Ready** - Outputs OGG format for voice messages

## 📦 Installation

### 1. Clone to Clawdbot Skills

```bash
# Copy to Clawdbot bundled skills directory
CLAWDBOT_SKILLS="/Users/johnny/Library/pnpm/global/5/.pnpm/clawdbot@*/node_modules/clawdbot/skills/"
cp -r ~/smart-voice-chat "$CLAWDBOT_SKILLS/"
```

### 2. Configure Sherpa-ONNX Models

Make sure you have these models installed:

- **STT**: `~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09`
- **TTS**: `~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en`

### 3. Restart Clawdbot

```bash
pkill -9 clawdbot
clawdbot-gateway &
```

### 4. Verify

```bash
clawdbot skills list | grep smart-voice
```

Should show: `│ ✓ ready │ 🗣️ smart-voice- │ ...`

## 💡 Usage

### Default Mode (Mirror)

```
You: [Voice] "今天天气怎么样"
AI:  [Voice + Text] "今天晴天，气温25度"
```

```
You: "今天天气怎么样"
AI:  "今天晴天，气温25度" [Text only]
```

### Override Mode

```
You: "用语音回答：明天会下雨吗"
AI:  [Voice only] "明天可能有小雨"
```

```
You: "用文字回答：现在几点了"
AI:  [Text only] "现在是下午4点"
```

## ⚙️ Configuration

### SKILL.md

```yaml
---
name: smart-voice-chat
description: "Voice conversation: transcribe voice input, reply in same format (voice-to-voice, text-to-text)"
metadata: {"clawdbot":{"emoji":"🗣️","os":["darwin","linux"],"requires":{"anyBins":["ffmpeg"]}}}
---
```

**Important**:
- Use quotes for `description`
- Avoid special characters like `→` (use `to` instead)
- `requires` only supports: `bins`, `anyBins`, `env`, `config`

### clawdbot.json

```json
{
  "skills": {
    "entries": {
      "smart-voice-chat": {
        "env": {
          "SMART_VOICE_CHAT_STT_MODEL": "/path/to/stt/model",
          "SMART_VOICE_CHAT_TTS_MODEL": "/path/to/tts/model"
        }
      }
    }
  }
}
```

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| STT | Sherpa-ONNX Paraformer (zh-en) |
| TTS | Sherpa-ONNX VITS-Melo (zh-en) |
| Audio | FFmpeg (WAV → OGG/OPUS) |
| Language | Python 3 + Bash |

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
