---
name: smart-voice-chat
description: "Voice conversation: transcribe voice input, reply in same format (voice-to-voice, text-to-text) by default. User can override with voice or text commands."
metadata: {"clawdbot":{"emoji":"🗣️","os":["darwin","linux"],"requires":{"anyBins":["ffmpeg"],"python":["sherpa-onnx","yaml"]}}}
---

# CRITICAL: VOICE MESSAGE HANDLING PROTOCOL

## WHEN USER SENDS VOICE MESSAGE - YOU MUST:

1. **RUN STT TO TRANSCRIBE**:
   ```bash
   ~/.clawdbot/skills/smart-voice-chat/bin/stt.py <audio_file_path>
   ```

2. **CHECK FOR TEXT-ONLY KEYWORDS** in transcribed text:
   - If contains "用文字回答" or "不用读" or "只显示" → Reply with TEXT ONLY, skip to step 5

3. **PROCESS TRANSCRIBED TEXT** as user's actual message

4. **RUN TTS TO GENERATE VOICE** (MANDATORY for voice input):
   ```bash
   ~/.clawdbot/skills/smart-voice-chat/bin/tts.py "<YOUR_RESPONSE_TEXT>" /tmp/smart-voice-chat/response_$(date +%s)
   ```

5. **SEND REPLY**:
   - If voice input (no text-override): `{"text": "<response>", "mediaUrl": "/tmp/smart-voice-chat/response_<timestamp>.ogg", "audioAsVoice": true}`
   - If text-override or text input: `{"text": "<response>"}`

## WHEN USER SENDS TEXT MESSAGE - YOU MUST:

1. **CHECK FOR VOICE KEYWORDS**:
   - If contains "用语音回答" or "读出来" or "说一下" → Generate voice (go to step 3)

2. **PROCESS AND REPLY** with text only: `{"text": "<response>"}`

3. **GENERATE VOICE** (only if voice keywords detected):
   ```bash
   ~/.clawdbot/skills/smart-voice-chat/bin/tts.py "<YOUR_RESPONSE_TEXT>" /tmp/smart-voice-chat/response_$(date +%s)
   ```
   Reply: `{"mediaUrl": "/tmp/smart-voice-chat/response_<timestamp>.ogg", "audioAsVoice": true}`

---

## Binary Paths (memorize these)

- **STT**: `~/.clawdbot/skills/smart-voice-chat/bin/stt.py <audio_file>`
- **TTS**: `~/.clawdbot/skills/smart-voice-chat/bin/tts.py "<text>" <output_path>`

## Response Format Examples

**IMPORTANT: Parameter Choice for Telegram Voice Messages**

The `audioAsVoice: true` parameter may not work in all Telegram configurations. If you encounter issues with voice messages not being sent/received, use `filePath` instead:

**Method 1 - audioAsVoice (may not work in some environments)**:
```json
{"text": "Your response", "mediaUrl": "/tmp/smart-voice-chat/response_1738212345.ogg", "audioAsVoice": true}
```

**Method 2 - filePath (more reliable)**:
```json
{"text": "Your response", "filePath": "/tmp/smart-voice-chat/response_1738212345.ogg"}
```

**Recommendation**: Test both methods in your environment and use the one that works. The `filePath` parameter is generally more reliable as it directly uploads the local file.

---

**Voice Input → Voice + Text** (default):
```json
{"text": "Your response", "filePath": "/tmp/smart-voice-chat/response_1738212345.ogg"}
```

**Text Input → Text** (default):
```json
{"text": "Your response"}
```

**Voice Override** (text input requesting voice):
```json
{"filePath": "/tmp/smart-voice-chat/response_1738212345.ogg"}
```

---

TL;DR:
- Voice attachment? → STT → TTS → Reply with voice+text
- Text message? → Reply with text only
- User says "用语音回答"? → Generate TTS → Reply with voice
- User says "用文字回答"? → Reply with text only
