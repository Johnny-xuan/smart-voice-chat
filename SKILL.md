---
name: smart-voice-chat
description: Voice conversation: transcribe voice input, reply in same format (voice→voice, text→text) by default. User can override with "用语音回答" or "用文字回答".
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

Intelligent voice conversation system with automatic format detection and mirrored response mode.

## 🎯 How It Works

**Core Principle**: Reply in the same format as the input (voice → voice, text → text)

```
Voice Input → STT → AI Process → TTS → Voice Reply
Text Input  → AI Process → Text Reply
```

## 📋 Workflow for AI Agents

### Step 1: Detect Input Format

When receiving a message from the user:

**Check if message contains:**
- Voice attachment (audio/* mime type)
- Audio file path (.wav, .ogg, .mp3, .m4a)

**If voice detected:**
```bash
~/.clawdbot/skills/smart-voice-chat/bin/stt.py <audio_file>
```

**If text:**
- Use the text directly

### Step 2: Parse Intent

Check the transcribed text for keywords:
- "用语音回答", "读出来", "说一下" → Voice-only output
- "用文字回答", "不用读", "只显示" → Text-only output
- **Default** → Use same format as input (voice → voice, text → text)

### Step 3: Process with AI

Use the transcribed/cleaned text as the user's actual message for AI processing.

### Step 4: Generate Response

**For voice output or dual mode:**
```bash
~/.clawdbot/skills/smart-voice-chat/bin/tts.py \
  "<AI_RESPONSE_TEXT>" \
  /tmp/smart-voice-chat/response_<timestamp>
```
**Note**: TTS will automatically output .ogg format (Telegram voice message compatible)

**Then attach the audio file to the reply:**
- For Telegram: Use audioAsVoice: true with mediaUrl (.ogg file)
- For iMessage: Attach the .ogg file (Telegram compatible format)
- For other channels: Attach based on channel capabilities

**For text-only mode:**
- Send text only, no audio attachment

## 💡 Usage Examples

### Example 1: Voice Input → Voice Reply (Default)

```
You: [Send voice message] "今天天气怎么样"

AI: 
  1. Detects voice attachment
  2. Runs STT → "今天天气怎么样"
  3. Processes AI → "今天晴天，气温25度"
  4. Runs TTS → generates .wav file
  5. Sends: "今天晴天，气温25度" + voice attachment
```

### Example 2: Text Input → Text Reply (Default)

```
You: "今天天气怎么样"

AI:
  1. Detects text input
  2. Processes AI → "今天晴天，气温25度"
  3. Sends: "今天晴天，气温25度" (text only)
```

### Example 3: Voice Input → Text Reply (Special Request)

```
You: [Send voice] "用文字回答：今天几点了"

AI:
  1. Detects voice attachment
  2. Runs STT → "用文字回答：今天几点了"
  3. Parses intent → Text-only mode
  4. Cleans text → "今天几点了"
  5. Processes AI → "现在是下午4点"
  6. Sends: "现在是下午4点" (text only, no voice)
```

### Example 4: Text Input → Voice Reply (Special Request)

```
You: "用语音回答：明天会下雨吗"

AI:
  1. Detects text input
  2. Parses intent → Voice-only mode
  3. Cleans text → "明天会下雨吗"
  4. Processes AI → "明天可能有小雨"
  5. Runs TTS → generates .wav file
  6. Sends: voice attachment
```

## 🔧 Configuration

Edit ~/.clawdbot/skills/smart-voice-chat/config/config.yaml:

```yaml
# Default behavior
voice:
  input_mode: auto          # Auto-detect input type
  output_mode: mirror       # mirror = same format as input
  auto_play: false          # Let Moltbot handle playback

# STT settings
stt:
  model_path: ~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09
  language: zh-en

# TTS settings
tts:
  model_path: ~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en
  output_dir: /tmp/smart-voice-chat
```

## 🎨 Reply Format

### For Telegram

```json
{
  "text": "AI response text",
  "mediaUrl": "/tmp/smart-voice-chat/response_xxx.ogg",
  "audioAsVoice": true
}
```

### For iMessage

```json
{
  "text": "AI response text",
  "attachments": [
    {
      "original_path": "/tmp/smart-voice-chat/response_xxx.ogg"
    }
  ]
}
```

## ⚠️ Important Notes

1. **Default mode is "mirror"**: Reply in same format as input
2. **Always transcribe voice first**: Don't process raw audio files
3. **Clean intent keywords**: Remove "用语音回答" etc. before AI processing
4. **Generate unique filenames**: Use timestamp or random ID for TTS output
5. **Handle STT failures**: If transcription fails, ask user to repeat

## 📊 Supported Audio Formats

**Input**: .wav, .mp3, .m4a, .ogg, .opus, .flac
**Output**: .ogg (OPUS encoded, Telegram voice message compatible)

---

**TL;DR**: Auto-detect input format → Process with AI → Reply in same format (unless user requests otherwise)
