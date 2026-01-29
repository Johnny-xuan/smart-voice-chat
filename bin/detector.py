#!/usr/bin/env python3
"""
SmartVoice Chat - Input Type Detector
检测输入是语音还是文字
"""

import os
import sys
from pathlib import Path

# Add lib directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))


class InputDetector:
    """检测输入类型"""
    
    # 支持的音频格式
    AUDIO_EXTENSIONS = {
        '.wav', '.mp3', '.m4a', '.ogg', '.opus', 
        '.flac', '.aac', '.wma'
    }
    
    @classmethod
    def detect(cls, input_data):
        """
        检测输入类型
        
        Args:
            input_data: 输入数据（文件路径或文字内容）
            
        Returns:
            str: 'voice', 'text', 或 'unknown'
        """
        # 检查是否是文件路径
        if cls._is_file_path(input_data):
            return cls._detect_file_type(input_data)
        
        # 检查是否是纯文字
        if cls._is_text(input_data):
            return 'text'
        
        return 'unknown'
    
    @classmethod
    def _is_file_path(cls, data):
        """检查是否是文件路径"""
        if not isinstance(data, str):
            return False
        
        # 检查是否是绝对路径或相对路径
        stripped = data.strip()
        if not stripped:
            return False
            
        # 检查是否包含路径分隔符或文件扩展名
        return ('/' in stripped or 
                '\\' in stripped or 
                '.' in stripped and 
                os.path.exists(stripped))
    
    @classmethod
    def _detect_file_type(cls, file_path):
        """检测文件类型"""
        if not os.path.exists(file_path):
            return 'unknown'
        
        # 检查文件扩展名
        ext = Path(file_path).suffix.lower()
        
        if ext in cls.AUDIO_EXTENSIONS:
            return 'voice'
        
        # 检查是否是文本文件
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                f.read(1024)  # 尝试读取一小部分
            return 'text'
        except:
            return 'unknown'
    
    @classmethod
    def _is_text(cls, data):
        """检查是否是文字内容"""
        if not isinstance(data, str):
            return False
        
        stripped = data.strip()
        
        # 空字符串
        if not stripped:
            return False
        
        # 文件路径（已处理）
        if os.path.exists(stripped):
            return False
        
        # 纯文字内容
        return True


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: detector.py <input_data>")
        print("  input_data: 文件路径或文字内容")
        sys.exit(1)
    
    input_data = sys.argv[1]
    result = InputDetector.detect(input_data)
    print(result)


if __name__ == "__main__":
    main()
