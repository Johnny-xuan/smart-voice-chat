# SmartVoice Chat 🗣️

**一个为 Clawdbot 设计的智能语音对话 Skill**

基于 Sherpa-ONNX 全栈的离线语音交互解决方案，让 Fox（或其他 AI Agent）能够与你进行自然的语音对话。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Clawdbot Skill](https://img.shields.io/badge/Clawdbot-Skill-blue.svg)](https://github.com/clawd-bot)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## ✨ 特性

- 🎯 **自动输入检测** - 智能识别语音/文字输入
- 🎛️ **灵活输出模式** - 关键词控制语音/文字/双模式输出
- 🌏 **中英混合支持** - 原生支持中文+英文混合识别与合成
- 🔒 **完全离线** - 无需网络连接，保护隐私
- 🤖 **Fox 集成** - 作为 Clawdbot Skill 无缝集成
- ⚙️ **高度可配置** - YAML 配置文件，自定义行为

## 📦 这是一个 Clawdbot Skill

SmartVoice Chat 是为 [Clawdbot](https://github.com/clawd-bot) 设计的 **Skill**，安装后 Fox 将获得智能语音对话能力：

```
┌─────────────────────────────────────────────────┐
│              Clawdbot (Fox)                     │
│                                                 │
│  你说话 → SmartVoice Chat Skill → Fox 理解     │
│           自动检测、解析、处理                  │
│                                                 │
│  Fox 回复 → SmartVoice Chat Skill → 语音播报   │
│            智能选择输出方式                     │
└─────────────────────────────────────────────────┘
```

### 安装为 Clawdbot Skill

```bash
# 1. 克隆到 clawdbot skills 目录
git clone https://github.com/Johnny-xuan/smart-voice-chat.git \
  ~/.clawdbot/skills/smart-voice-chat

# 2. 运行安装脚本
cd ~/.clawdbot/skills/smart-voice-chat
./install.sh

# 3. 验证安装
clawdbot skills list | grep smart-voice
```

### 在 Fox 中使用

```
你: "用 smart-voice 和我对话"

Fox: 好的！现在可以语音对话了。
     你可以说话或打字，我会智能识别并回复。
     
你: [说话] 今天天气怎么样
Fox: [文字] 今天晴天，气温25度
    [语音] 今天晴天，气温25度
```

## 🚀 快速开始

### 方式一：作为 Clawdbot Skill 使用（推荐）

```bash
# 安装到 clawdbot
git clone https://github.com/Johnny-xuan/smart-voice-chat.git \
  ~/.clawdbot/skills/smart-voice-chat

cd ~/.clawdbot/skills/smart-voice-chat
./install.sh

# 在 Fox 中使用
"用 smart-voice 处理这段语音"
```

### 方式二：独立使用

```bash
# 克隆仓库
git clone https://github.com/Johnny-xuan/smart-voice-chat.git
cd smart-voice-chat

# 安装依赖
pip3 install -r requirements.txt

# 运行
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
AI: [仅语音播报] 明天可能有小雨

你: 用文字回答：现在几点了
AI: [仅文字显示] 现在是下午4点
```

### 中英混合

```
你: yesterday was 星期一 today is tuesday
AI: [识别正确] 昨天是星期一，今天是星期二
```

## 🏗️ 项目结构

```
smart-voice-chat/
├── SKILL.md              # Clawdbot Skill 定义 ⭐
├── README.md             # 项目文档
├── install.sh            # 安装脚本
├── config/
│   └── config.yaml       # 配置文件
├── bin/                  # 核心模块
│   ├── smart-voice.sh    # 主入口（Fox 调用这个）
│   ├── detector.py       # 输入类型检测
│   ├── parser.py         # 意图解析
│   ├── stt.py            # STT 封装
│   ├── tts.py            # TTS 封装
│   └── player.py         # 音频播放
├── lib/
│   └── orchestrator.py   # 流程编排
└── tests/
    └── test.sh           # 测试脚本
```

## ⚙️ 配置

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

## 🔧 技术栈

| 组件 | 技术 |
|------|------|
| Skill 类型 | Clawdbot Skill |
| STT | Sherpa-ONNX Paraformer |
| TTS | Sherpa-ONNX VITS-Melo |
| 语言 | Python 3 + Bash |
| 配置 | YAML |

## 📊 与旧版 voice-chat 对比

| 特性 | SmartVoice Chat | voice-chat (旧) |
|------|----------------|----------------|
| 自动输入检测 | ✅ 智能识别 | ❌ 需手动录音 |
| 灵活输出控制 | ✅ 关键词+配置 | ❌ 固定模式 |
| 中英混合 | ✅ 原生支持 | ⚠️ 需切换 |
| 配置化 | ✅ YAML 文件 | ❌ 硬编码 |
| Skill 封装 | ✅ 完整 SKILL.md | ⚠️ 简单 |

## 🔌 Skill 依赖

```yaml
metadata: {
  "clawdbot": {
    "requires": {
      "bins": ["smart-voice.sh"],
      "python": ["sherpa-onnx", "yaml"]
    }
  }
}
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 🙏 致谢

- [Clawdbot](https://github.com/clawd-bot) - AI Agent 框架
- [Sherpa-ONNX](https://github.com/k2-fsa/sherpa-onnx) - 离线语音处理
- [Paraformer](https://github.com/alibaba-damo-academy/FunASR) - 阿里语音识别
- [VITS-Melo](https://github.com/myshell-ai/MeloTTS) - MyShell 语音合成

---

**作者**: Johnny  
**Clawdbot Skill**: [smart-voice-chat](https://github.com/Johnny-xuan/smart-voice-chat)  
**用途**: 让 Fox 具备智能语音对话能力
