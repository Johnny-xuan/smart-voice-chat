---
name: smart-voice-chat
description: Intelligent voice conversation system - Auto-detect voice/text input, flexible output formats, Chinese-English mixed support
homepage: https://github.com/Johnny-xuan/smart-voice-chat
metadata: {
  "moltbot": {
    "emoji": "🗣️",
    "requires": {
      "bins": ["smart-voice.sh"],
      "python": ["sherpa-onnx", "yaml"]
    },
    "skills": []
  }
}
---

# SmartVoice Chat 🗣️

Intelligent voice conversation system powered by Sherpa-ONNX offline speech processing stack.

## Features

- ✅ **Auto Input Detection**: Intelligently recognizes voice/text input
- ✅ **Flexible Output Modes**: Supports voice/text/dual output modes
- ✅ **Chinese-English Mixed**: Native support for Chinese + English mixed recognition and synthesis
- ✅ **Fully Offline**: No network connection required, privacy-preserving
- ✅ **Smart Intent Parsing**: Automatically understands desired output mode

## How It Works

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  You Speak  │ →  │  Auto Detect│ →  │  AI Process │ →  │ Flexible    │
│  or Type    │    │  (STT/Text) │    │             │    │ Output      │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                        ↓                                  ↓
                  Sherpa-ONNX                        Sherpa-ONNX
                  Paraformer STT                      VITS-Melo TTS
```

## Quick Start

### 1. Install Dependencies

Ensure Sherpa-ONNX components are installed:

```bash
# STT Model (Paraformer)
~/.moltbot/tools/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09/

# TTS Model (VITS-Melo)
~/.moltbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en/

# Python dependencies
pip3 install sherpa-onnx pyyaml
```

### 2. Usage

```bash
# Process audio file
smart-voice.sh /path/to/audio.wav

# Process text input
smart-voice.sh "今天天气怎么样"

# Interactive mode
smart-voice.sh -i
```

## Output Mode Control

### Keyword Control

Use keywords in conversation to control output mode:

| Keyword | Effect |
|---------|--------|
| "用语音回答" or "读出来" | Voice output only |
| "用文字回答" or "不用读" | Text output only |
| (default) | Dual mode (text + voice) |

### Example Conversation

```
You: 今天天气怎么样
AI: [Text display] 今天晴天，气温25度
   [Voice playback] 今天晴天，气温25度

You: 用语音回答：明天会下雨吗
AI: [Voice playback] 明天可能有小雨

You: 用文字回答：现在几点了
AI: [Text display] 现在是下午4点
```

## Tech Stack

- **STT**: Sherpa-ONNX Paraformer (Chinese + English mixed recognition)
- **TTS**: Sherpa-ONNX VITS-Melo (Chinese + English mixed synthesis)
- **Language**: Python 3 + Bash
- **Config**: YAML

## Module Architecture

```
smart-voice-chat/
├── bin/
│   ├── detector.py        # Input type detection
│   ├── parser.py          # Intent parsing
│   ├── stt.py             # STT wrapper
│   ├── tts.py             # TTS wrapper
│   ├── player.py          # Audio playback
│   └── smart-voice.sh     # Main entry point
└── lib/
    └── orchestrator.py    # Flow orchestration
```

## Configuration

Edit `config/config.yaml` to customize behavior:

```yaml
voice:
  input_mode: auto          # auto | voice_only | text_only
  output_mode: dual         # dual | voice_only | text_only
  auto_play: true           # Auto-play TTS

stt:
  model_path: ~/.moltbot/tools/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09
  language: zh-en           # Chinese-English mixed

tts:
  model_path: ~/.moltbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en
```

## Comparison with Traditional Solutions

| Feature | SmartVoice Chat | Traditional voice-chat |
|---------|----------------|----------------------|
| Input detection | ✅ Auto recognize | ❌ Manual specification |
| Output control | ✅ Keywords + config | ❌ Fixed mode |
| Chinese-English mixed | ✅ Native support | ⚠️ Model switching |
| Flexibility | ✅ Highly configurable | ❌ Hardcoded |

## Troubleshooting

### STT Not Working
```bash
# Check if model exists
ls ~/.moltbot/tools/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09/

# Test STT CLI
~/.moltbot/tools/sherpa-stt/sherpa-stcli.py test.wav
```

### TTS Not Working
```bash
# Check if model exists
ls ~/.moltbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en/

# Test TTS
sherpa-onnx-offline-tts --help
```

### Audio Format Issues
```bash
# Convert audio to WAV format
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

---

**TL;DR**: Auto-detect input type, flexible output selection, fully offline Chinese-English mixed voice conversation system.
