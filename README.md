# SmartVoice Chat 🗣️

**An Intelligent Voice Conversation Skill for Moltbot**

Offline voice interaction solution powered by Sherpa-ONNX, enabling natural voice conversations with AI agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Moltbot Skill](https://img.shields.io/badge/Moltbot-Skill-blue.svg)](https://github.com/moltbot)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## ✨ Features

- 🎯 **Auto Input Detection** - Intelligently detects voice/text input
- 🎛️ **Flexible Output Modes** - Keyword-controlled voice/text/dual output
- 🌏 **Chinese-English Mixed** - Native support for mixed Chinese and English
- 🔒 **Fully Offline** - No network connection required, privacy-preserving
- 🤖 **Moltbot Integration** - Seamless integration as a Moltbot Skill
- ⚙️ **Highly Configurable** - YAML configuration for customization

## 📦 This is a Moltbot Skill

SmartVoice Chat is a **Skill** designed for [Moltbot](https://github.com/moltbot), enabling AI agents to have natural voice conversations:

```
┌─────────────────────────────────────────────────┐
│              Moltbot (AI Agent)                 │
│                                                 │
│  You speak → SmartVoice Chat → Agent understands│
│              Auto-detect, parse, process        │
│                                                 │
│  Agent replies → SmartVoice Chat → Voice output │
│                   Smart output selection        │
└─────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Method 1: As Moltbot Skill (Recommended)

```bash
# Install to Moltbot skills directory
git clone https://github.com/Johnny-xuan/smart-voice-chat.git \
  ~/.moltbot/skills/smart-voice-chat

cd ~/.moltbot/skills/smart-voice-chat
./install.sh

# Verify installation
moltbot skills list | grep smart-voice
```

### Method 2: Standalone Usage

```bash
# Clone repository
git clone https://github.com/Johnny-xuan/smart-voice-chat.git
cd smart-voice-chat

# Install dependencies
pip3 install -r requirements.txt

# Run
./bin/smart-voice.sh -i
```

## 💡 Usage Examples

### Basic Conversation

```
You: 今天天气怎么样
AI: [Text] 今天晴天，气温25度
    [Voice] 今天晴天，气温25度
```

### Output Mode Control

```
You: 用语音回答：明天会下雨吗
AI: [Voice only] 明天可能有小雨

You: 用文字回答：现在几点了
AI: [Text only] 现在是下午4点
```

### Chinese-English Mixed

```
You: yesterday was 星期一 today is tuesday
AI: [Recognized] 昨天是星期一，今天是星期二
```

## 🏗️ Project Structure

```
smart-voice-chat/
├── SKILL.md              # Moltbot Skill definition ⭐
├── README.md             # Project documentation
├── install.sh            # Installation script
├── config/
│   └── config.yaml       # Configuration file
├── bin/                  # Core modules
│   ├── smart-voice.sh    # Main entry point
│   ├── detector.py       # Input type detection
│   ├── parser.py         # Intent parsing
│   ├── stt.py            # STT wrapper
│   ├── tts.py            # TTS wrapper
│   └── player.py         # Audio playback
├── lib/
│   └── orchestrator.py   # Flow orchestration
└── tests/
    └── test.sh           # Test suite
```

## ⚙️ Configuration

Edit `config/config.yaml` to customize behavior:

```yaml
voice:
  input_mode: auto          # auto | voice_only | text_only
  output_mode: dual         # dual | voice_only | text_only
  auto_play: true           # Auto-play TTS output

stt:
  model_path: ~/.moltbot/tools/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09
  language: zh-en           # Chinese-English mixed

tts:
  model_path: ~/.moltbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en
```

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| Skill Type | Moltbot Skill |
| STT | Sherpa-ONNX Paraformer |
| TTS | Sherpa-ONNX VITS-Melo |
| Language | Python 3 + Bash |
| Config | YAML |

## 📊 Comparison with Old voice-chat

| Feature | SmartVoice Chat | voice-chat (old) |
|---------|----------------|-----------------|
| Auto input detection | ✅ Smart recognition | ❌ Manual recording |
| Flexible output control | ✅ Keywords + config | ❌ Fixed mode |
| Chinese-English mixed | ✅ Native support | ⚠️ Requires switching |
| Configurable | ✅ YAML file | ❌ Hardcoded |
| Skill packaging | ✅ Complete SKILL.md | ⚠️ Basic |

## 🔌 Skill Dependencies

```yaml
metadata: {
  "moltbot": {
    "emoji": "🗣️",
    "requires": {
      "bins": ["smart-voice.sh"],
      "python": ["sherpa-onnx", "yaml"]
    }
  }
}
```

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 🙏 Acknowledgments

- [Moltbot](https://github.com/moltbot) - AI Agent Framework
- [Sherpa-ONNX](https://github.com/k2-fsa/sherpa-onnx) - Offline speech processing
- [Paraformer](https://github.com/alibaba-damo-academy/FunASR) - Alibaba's ASR model
- [VITS-Melo](https://github.com/myshell-ai/MeloTTS) - MyShell's TTS model

---

**Author**: Johnny  
**Moltbot Skill**: [smart-voice-chat](https://github.com/Johnny-xuan/smart-voice-chat)  
**Purpose**: Enable intelligent voice conversation capabilities for AI agents
