#!/usr/bin/env python3
"""
SmartVoice Chat - Intent Parser
解析用户意图，决定输出模式
"""

import re
import sys
from pathlib import Path
import yaml

# Add lib directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))


class IntentParser:
    """意图解析器"""
    
    def __init__(self, config_path=None):
        """
        初始化解析器
        
        Args:
            config_path: 配置文件路径
        """
        self.config = self._load_config(config_path)
        self.voice_keywords = self.config.get(
            'intent_keywords', {}).get('voice_only', []
        )
        self.text_keywords = self.config.get(
            'intent_keywords', {}).get('text_only', []
        )
    
    def _load_config(self, config_path):
        """加载配置文件"""
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config" / "config.yaml"
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except:
            # 返回默认配置
            return {
                'intent_keywords': {
                    'voice_only': ['用语音回答', '读出来', '说一下'],
                    'text_only': ['用文字回答', '不用读', '只显示']
                }
            }
    
    def parse(self, text, default_mode='dual'):
        """
        解析意图，决定输出模式
        
        Args:
            text: 用户输入的文字
            default_mode: 默认模式 ('dual', 'voice_only', 'text_only')
            
        Returns:
            dict: {
                'mode': 'dual' | 'voice_only' | 'text_only',
                'cleaned_text': '去除关键词后的文字',
                'detected_keyword': '检测到的关键词（如果有）'
            }
        """
        # 检查语音关键词
        for keyword in self.voice_keywords:
            if keyword in text:
                return {
                    'mode': 'voice_only',
                    'cleaned_text': text.replace(keyword, '').strip(),
                    'detected_keyword': keyword
                }
        
        # 检查文字关键词
        for keyword in self.text_keywords:
            if keyword in text:
                return {
                    'mode': 'text_only',
                    'cleaned_text': text.replace(keyword, '').strip(),
                    'detected_keyword': keyword
                }
        
        # 默认模式
        return {
            'mode': default_mode,
            'cleaned_text': text,
            'detected_keyword': None
        }
    
    def should_use_voice(self, text, default=True):
        """
        简化版判断：是否应该用语音输出
        
        Args:
            text: 用户输入
            default: 默认值
            
        Returns:
            bool: 是否用语音输出
        """
        result = self.parse(text, default_mode='dual' if default else 'text_only')
        return result['mode'] in ['dual', 'voice_only']
    
    def should_use_text(self, text, default=True):
        """
        简化版判断：是否应该用文字输出
        
        Args:
            text: 用户输入
            default: 默认值
            
        Returns:
            bool: 是否用文字输出
        """
        result = self.parse(text, default_mode='dual' if default else 'voice_only')
        return result['mode'] in ['dual', 'text_only']


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: parser.py <text>")
        sys.exit(1)
    
    text = ' '.join(sys.argv[1:])
    parser = IntentParser()
    result = parser.parse(text)
    
    print(f"Mode: {result['mode']}")
    print(f"Cleaned: {result['cleaned_text']}")
    if result['detected_keyword']:
        print(f"Keyword: {result['detected_keyword']}")


if __name__ == "__main__":
    main()
