#!/usr/bin/env python3
"""
SmartVoice Chat - Orchestrator
流程编排器：整合所有模块
"""

import sys
import os
from pathlib import Path

# Add bin directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "bin"))

from detector import InputDetector
from parser import IntentParser
from stt import STTModule
from tts import TTSModule
from player import AudioPlayer


class VoiceOrchestrator:
    """语音对话编排器"""
    
    def __init__(self, config_path=None):
        """
        初始化编排器
        
        Args:
            config_path: 配置文件路径
        """
        # 获取配置文件路径
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config" / "config.yaml"
        
        self.config_path = str(config_path)
        
        # 初始化所有模块
        self.detector = InputDetector()
        self.parser = IntentParser(config_path)
        self.stt = STTModule(config_path)
        self.tts = TTSModule(config_path)
        self.player = AudioPlayer(config_path)
        
        # 获取默认配置
        import yaml
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.default_output_mode = self.config.get(
            'voice', {}).get('output_mode', 'dual'
        )
        self.auto_play = self.config.get(
            'voice', {}).get('auto_play', True
        )
    
    def process(self, input_data, agent_handler=None):
        """
        处理用户输入
        
        Args:
            input_data: 用户输入（文件路径或文字）
            agent_handler: AI 处理函数，接收文字，返回文字
            
        Returns:
            dict: {
                'input_type': 'voice' | 'text',
                'input_text': '用户输入的文字',
                'response': 'AI 回复',
                'output_mode': 'dual' | 'voice_only' | 'text_only',
                'audio_file': '生成的音频文件路径（如果有）'
            }
        """
        result = {
            'input_type': None,
            'input_text': None,
            'response': None,
            'output_mode': None,
            'audio_file': None
        }
        
        # 1. 检测输入类型
        input_type = self.detector.detect(input_data)
        result['input_type'] = input_type
        
        if input_type == 'unknown':
            raise ValueError("无法识别输入类型")
        
        # 2. 转换为文字（如果是语音）
        if input_type == 'voice':
            input_text = self.stt.transcribe(input_data)
        else:
            input_text = input_data
        
        result['input_text'] = input_text
        
        # 3. 解析意图
        intent = self.parser.parse(input_text, self.default_output_mode)
        result['output_mode'] = intent['mode']
        
        # 4. AI 处理
        if agent_handler:
            response = agent_handler(intent['cleaned_text'])
        else:
            # 默认：简单回显
            response = f"你说：{intent['cleaned_text']}"
        
        result['response'] = response
        
        # 5. 生成输出
        if intent['mode'] in ['voice_only', 'dual']:
            # TTS 合成
            audio_file = self.tts.synthesize(response)
            result['audio_file'] = audio_file
            
            # 自动播放
            if self.auto_play:
                self.player.play(audio_file)
        
        return result
    
    def print_result(self, result):
        """打印处理结果"""
        print(f"\n{'='*60}")
        print(f"输入类型: {result['input_type']}")
        print(f"输入内容: {result['input_text']}")
        print(f"输出模式: {result['output_mode']}")
        print(f"AI 回复: {result['response']}")
        if result['audio_file']:
            print(f"音频文件: {result['audio_file']}")
        print(f"{'='*60}\n")


def main():
    """命令行入口（测试用）"""
    if len(sys.argv) < 2:
        print("Usage: orchestrator.py <input_data>")
        print("  input_data: 音频文件路径或文字内容")
        sys.exit(1)
    
    input_data = sys.argv[1]
    
    try:
        orchestrator = VoiceOrchestrator()
        result = orchestrator.process(input_data)
        orchestrator.print_result(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
