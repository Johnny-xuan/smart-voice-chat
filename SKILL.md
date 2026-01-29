---
name: smart-voice-chat
description: 智能语音对话系统 - 自动检测语音/文字输入，灵活选择输出格式，支持中英混合
homepage: https://github.com/johnny/smart-voice-chat
metadata: {
  "clawdbot": {
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

智能语音对话系统 - 基于 Sherpa-ONNX 全栈的离线语音交互解决方案。

## 特性

- ✅ **自动检测输入类型**: 智能识别语音/文字输入
- ✅ **灵活输出模式**: 支持语音/文字/双模式输出
- ✅ **中英混合支持**: 原生支持中文+英文混合识别与合成
- ✅ **完全离线运行**: 无需网络连接，保护隐私
- ✅ **智能意图解析**: 自动理解用户想要的输出方式

## 如何工作

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  你说话     │ →  │  自动检测   │ →  │  AI 处理    │ →  │  灵活输出   │
│  或打字     │    │  (STT/文字) │    │             │    │ (语音/文字) │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                        ↓                                  ↓
                  Sherpa-ONNX                        Sherpa-ONNX
                  Paraformer STT                      VITS-Melo TTS
```

## 快速开始

### 1. 安装依赖

确保已安装 Sherpa-ONNX 组件：

```bash
# STT 模型 (Paraformer)
~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09/

# TTS 模型 (VITS-Melo)
~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en/

# Python 依赖
pip3 install sherpa-onnx pyyaml
```

### 2. 使用

```bash
# 处理音频文件
smart-voice.sh /path/to/audio.wav

# 处理文字输入
smart-voice.sh "今天天气怎么样"

# 交互模式
smart-voice.sh -i
```

## 输出模式控制

### 关键词控制

在对话中使用关键词控制输出模式：

| 关键词 | 效果 |
|--------|------|
| "用语音回答" | 仅语音输出 |
| "读出来" | 仅语音输出 |
| "用文字回答" | 仅文字输出 |
| "不用读" | 仅文字输出 |
| (默认) | 双模式（文字+语音） |

### 示例对话

```
你: 今天天气怎么样
AI: [文字显示] 今天晴天，气温25度
   [语音播报] 今天晴天，气温25度

你: 用语音回答：明天会下雨吗
AI: [语音播报] 明天可能有小雨

你: 用文字回答：现在几点了
AI: [文字显示] 现在是下午4点
```

## 技术栈

- **STT**: Sherpa-ONNX Paraformer (中文+英文混合识别)
- **TTS**: Sherpa-ONNX VITS-Melo (中文+英文混合合成)
- **语言**: Python 3 + Bash
- **配置**: YAML

## 模块架构

```
smart-voice-chat/
├── bin/
│   ├── detector.py        # 输入类型检测
│   ├── parser.py          # 意图解析
│   ├── stt.py             # STT 封装
│   ├── tts.py             # TTS 封装
│   ├── player.py          # 音频播放
│   └── smart-voice.sh     # 主入口
└── lib/
    └── orchestrator.py    # 流程编排
```

## 配置文件

编辑 `config/config.yaml` 自定义行为：

```yaml
voice:
  input_mode: auto          # auto | voice_only | text_only
  output_mode: dual         # dual | voice_only | text_only
  auto_play: true           # 自动播放 TTS

stt:
  model_path: ~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09
  language: zh-en           # 中英混合

tts:
  model_path: ~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en
```

## 与传统方案对比

| 特性 | SmartVoice Chat | 传统 voice-chat |
|------|----------------|----------------|
| 输入检测 | ✅ 自动识别 | ❌ 需手动指定 |
| 输出控制 | ✅ 关键词+配置 | ❌ 固定模式 |
| 中英混合 | ✅ 原生支持 | ⚠️ 需切换模型 |
| 灵活性 | ✅ 高度可配置 | ❌ 硬编码 |

## 故障排除

### STT 不工作
```bash
# 检查模型是否存在
ls ~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09/

# 测试 STT CLI
~/.clawdbot/tools/sherpa-stt/sherpa-stcli.py test.wav
```

### TTS 不工作
```bash
# 检查模型是否存在
ls ~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en/

# 测试 TTS
sherpa-onnx-offline-tts --help
```

### 音频格式问题
```bash
# 转换音频为 WAV 格式
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

---

**TL;DR**: 自动检测输入类型，灵活选择输出方式，完全离线的中英混合语音对话系统。
