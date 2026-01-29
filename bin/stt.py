#!/usr/bin/env python3
"""
SmartVoice Chat - STT (Speech-to-Text) Module
语音转文字封装
"""

import os
import sys
import subprocess
from pathlib import Path
import yaml

# Add lib directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))


class STTModule:
    """语音转文字模块"""
    
    def __init__(self, config_path=None):
        """初始化 STT 模块"""
        self.config = self._load_config(config_path)
        
        # 获取 STT 配置
        stt_config = self.config.get('stt', {})
        self.model_dir = os.path.expanduser(stt_config.get('model_path', 
            '~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09'))
        self.model_file = stt_config.get('model_file', 'model.onnx')
        self.tokens_file = stt_config.get('tokens_file', 'tokens.txt')
        self.num_threads = stt_config.get('num_threads', 4)
        
        # 现有的 STT CLI 路径
        self.stt_cli = os.path.expanduser('~/.clawdbot/tools/sherpa-stt/sherpa-stcli.py')
        
        # 支持的音频格式
        self.supported_formats = self.config.get('supported_formats', 
            ['wav', 'mp3', 'm4a', 'ogg', 'opus'])
    
    def _load_config(self, config_path):
        """加载配置文件"""
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config" / "config.yaml"
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except:
            return {}
    
    def _convert_to_wav(self, input_file):
        """
        转换音频文件为 WAV 格式（16kHz, mono）
        
        Args:
            input_file: 输入音频文件路径
            
        Returns:
            str: WAV 文件路径，如果不需要转换则返回原路径
        """
        # 检查扩展名
        ext = Path(input_file).suffix.lower()
        
        if ext == '.wav':
            # 检查是否已经是正确格式
            # 这里简化处理，假设已经是正确格式
            return input_file
        
        # 需要转换
        output_file = input_file.rsplit('.', 1)[0] + '.wav'
        
        try:
            subprocess.run([
                'ffmpeg', '-y', '-i', input_file,
                '-ar', '16000', '-ac', '1',
                output_file
            ], capture_output=True, check=True)
            return output_file
        except subprocess.CalledProcessError as e:
            raise Exception(f"音频转换失败: {e.stderr.decode()}")
    
    def transcribe(self, audio_file):
        """
        转写音频文件为文字
        
        Args:
            audio_file: 音频文件路径
            
        Returns:
            str: 识别的文字
        """
        # 检查文件是否存在
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"音频文件不存在: {audio_file}")
        
        # 转换为 WAV 格式
        wav_file = self._convert_to_wav(audio_file)
        
        # 调用 STT CLI
        try:
            result = subprocess.run([
                self.stt_cli, wav_file
            ], capture_output=True, text=True, check=True)
            
            return result.stdout.strip()
        
        except subprocess.CalledProcessError as e:
            raise Exception(f"STT 识别失败: {e.stderr}")


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: stt.py <audio_file>")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    
    try:
        stt = STTModule()
        text = stt.transcribe(audio_file)
        print(text)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
