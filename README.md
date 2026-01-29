# SmartVoice Chat 🗣️

智能语音对话系统 - 基于 Sherpa-ONNX 全栈的离线语音交互解决方案

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## ✨ 特性

- 🎯 **自动检测输入** - 智能识别语音/文字输入
- 🎛️ **灵活输出模式** - 支持语音/文字/双模式输出
- 🌏 **中英混合** - 原生支持中文+英文混合识别与合成
- 🔒 **完全离线** - 无需网络连接，保护隐私
- 🧠 **智能解析** - 自动理解用户想要的输出方式

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/johnny/smart-voice-chat.git
cd smart-voice-chat

# 确保 Sherpa-ONNX 组件已安装
# STT: ~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09/
# TTS: ~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en/

# 安装 Python 依赖
pip3 install -r requirements.txt
```

### 使用

```bash
# 处理音频文件
./bin/smart-voice.sh /path/to/audio.wav

# 处理文字输入
./bin/smart-voice.sh "今天天气怎么样"

# 交互模式
./bin/smart-voice.sh -i
```

## 💡 使用示例

### 基础对话

```
你: 今天天气怎么样
AI: [文字] 今天晴天，气温25度
    [语音] 今天晴天，气温25度
```

### 控制输出模式

```
你: 用语音回答：明天会下雨吗
AI: [语音播报] 明天可能有小雨

你: 用文字回答：现在几点了
AI: [文字显示] 现在是下午4点
```

## 🏗️ 项目结构

```
smart-voice-chat/
├── README.md              # 项目文档
├── SKILL.md               # Clawdbot skill 定义
├── requirements.txt       # Python 依赖
├── config/
│   └── config.yaml        # 配置文件
├── bin/
│   ├── smart-voice.sh     # 主入口脚本
│   ├── detector.py        # 输入类型检测
│   ├── parser.py          # 意图解析
│   ├── stt.py             # STT 封装
│   ├── tts.py             # TTS 封装
│   └── player.py          # 音频播放
├── lib/
│   └── orchestrator.py    # 流程编排
└── tests/
    └── test.sh            # 测试脚本
```

## ⚙️ 配置

编辑 `config/config.yaml` 自定义行为：

```yaml
voice:
  input_mode: auto          # 输入模式
  output_mode: dual         # 输出模式 (dual/voice_only/text_only)
  auto_play: true           # 自动播放

stt:
  language: zh-en           # 中英混合

tts:
  sample_rate: 22050        # 采样率
```

## 🔧 技术栈

| 组件 | 技术 |
|------|------|
| STT | Sherpa-ONNX Paraformer |
| TTS | Sherpa-ONNX VITS-Melo |
| 语言 | Python 3 + Bash |
| 配置 | YAML |

## 📊 与传统方案对比

| 特性 | SmartVoice Chat | voice-chat (旧) |
|------|----------------|----------------|
| 自动输入检测 | ✅ | ❌ |
| 灵活输出控制 | ✅ | ❌ |
| 中英混合 | ✅ | ⚠️ |
| 配置化 | ✅ | ❌ |

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 🙏 致谢

- [Sherpa-ONNX](https://github.com/k2-fsa/sherpa-onnx) - 离线语音处理工具链
- [Paraformer](https://github.com/alibaba-damo-academy/FunASR) - 阿里达摩院语音识别模型
- [VITS-Melo](https://github.com/myshell-ai/MeloTTS) - MyShell 语音合成模型

---

**作者**: Johnny  
**项目主页**: [smart-voice-chat](https://github.com/johnny/smart-voice-chat)
