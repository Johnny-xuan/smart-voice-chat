#!/usr/bin/env python3
"""
SmartVoice Chat - TTS (Text-to-Speech) Module
文字转语音封装
"""

import os
import sys
import subprocess
from pathlib import Path
import yaml
import tempfile

# Add lib directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))


class TTSModule:
    """文字转语音模块"""
    
    def __init__(self, config_path=None):
        """初始化 TTS 模块"""
        self.config = self._load_config(config_path)
        
        # 获取 TTS 配置
        tts_config = self.config.get('tts', {})
        self.model_dir = os.path.expanduser(tts_config.get('model_path',
            '~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en'))
        self.model_file = tts_config.get('model_file', 'model.onnx')
        self.tokens_file = tts_config.get('tokens_file', 'tokens.txt')
        self.lexicon_file = tts_config.get('lexicon_file', 'lexicon.txt')
        rule_fsts = tts_config.get('rule_fsts', 'date.fst,number.fst')
        self.rule_fsts = [f.strip() for f in rule_fsts.split(',')]
        self.num_threads = tts_config.get('num_threads', 4)
        
        # TTS 二进制路径
        self.tts_bin = os.path.expanduser('~/.local/bin/sherpa-onnx-offline-tts')
        
        # 临时目录
        self.temp_dir = Path(self.config.get('temp_dir', '/tmp/smart-voice-chat'))
        self.temp_dir.mkdir(parents=True, exist_ok=True)
    
    def _load_config(self, config_path):
        """加载配置文件"""
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config" / "config.yaml"
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except:
            return {}
    
    def _convert_to_ogg(self, wav_file, ogg_file):
        """
        将 WAV 转换为 OGG (OPUS 编码) 用于 Telegram 语音消息

        Args:
            wav_file: WAV 文件路径
            ogg_file: 输出 OGG 文件路径

        Returns:
            str: OGG 文件路径
        """
        cmd = [
            'ffmpeg',
            '-i', str(wav_file),
            '-c:a', 'libopus',
            '-ac', '1',  # 单声道
            '-b:a', '24k',  # 比特率
            '-application', 'voip',  # 语音优化
            str(ogg_file),
            '-y'  # 覆盖已存在文件
        ]

        try:
            subprocess.run(cmd, capture_output=True, check=True)
            return str(ogg_file)
        except subprocess.CalledProcessError as e:
            raise Exception(f"OGG 转换失败: {e.stderr.decode()}")

    def synthesize(self, text, output_file=None, format='ogg'):
        """
        合成语音

        Args:
            text: 要合成的文字
            output_file: 输出文件路径（可选，默认使用临时文件）
            format: 输出格式，'ogg' (Telegram 语音消息) 或 'wav' (原始音频)

        Returns:
            str: 输出文件路径
        """
        if not text or not text.strip():
            raise ValueError("文字内容为空")

        # 确定输出文件路径
        if output_file is None:
            output_file = self.temp_dir / f"tts_{id(text)}"
        else:
            output_file = Path(output_file)

        # 先生成临时 WAV 文件
        wav_file = self.temp_dir / f"temp_{id(text)}.wav"

        # 构建 TTS 命令
        cmd = [
            self.tts_bin,
            f'--vits-model={self.model_dir}/{self.model_file}',
            f'--vits-lexicon={self.model_dir}/{self.lexicon_file}',
            f'--vits-tokens={self.model_dir}/{self.tokens_file}',
            f'--tts-rule-fsts={self.model_dir}/{self.rule_fsts[0]},{self.model_dir}/{self.rule_fsts[1]}',
            f'--output-filename={wav_file}',
            text
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            # 根据格式要求返回文件
            if format == 'ogg':
                ogg_file = str(output_file) + '.ogg' if not str(output_file).endswith('.ogg') else str(output_file)
                final_file = self._convert_to_ogg(wav_file, ogg_file)
                # 删除临时 WAV 文件
                wav_file.unlink(missing_ok=True)
                return final_file
            else:
                # 返回 WAV 文件（重命名为目标文件名）
                if wav_file != output_file:
                    wav_file.rename(output_file)
                return str(output_file)

        except subprocess.CalledProcessError as e:
            raise Exception(f"TTS 合成失败: {e.stderr}")


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: tts.py <text> [output_file]")
        sys.exit(1)
    
    text = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        tts = TTSModule()
        audio_file = tts.synthesize(text, output_file)
        print(audio_file)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
