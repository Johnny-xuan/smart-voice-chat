#!/usr/bin/env python3
"""
SmartVoice Chat - Audio Player
音频播放模块
"""

import os
import sys
import subprocess
from pathlib import Path
import yaml

# Add lib directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))


class AudioPlayer:
    """音频播放器"""
    
    def __init__(self, config_path=None):
        """初始化播放器"""
        self.config = self._load_config(config_path)
        
        # 获取播放器配置
        self.player = self.config.get('voice', {}).get('audio_player', 'afplay')
        
        # 验证播放器是否可用
        self._validate_player()
    
    def _load_config(self, config_path):
        """加载配置文件"""
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config" / "config.yaml"
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except:
            return {}
    
    def _validate_player(self):
        """验证播放器是否可用"""
        try:
            subprocess.run(['which', self.player], 
                         capture_output=True, check=True)
        except subprocess.CalledProcessError:
            # 尝试使用默认播放器
            self.player = 'afplay'
    
    def play(self, audio_file):
        """
        播放音频文件
        
        Args:
            audio_file: 音频文件路径
        """
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"音频文件不存在: {audio_file}")
        
        try:
            subprocess.run([self.player, audio_file], check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"播放失败: {e}")
        except FileNotFoundError:
            raise Exception(f"播放器未找到: {self.player}")
    
    def play_async(self, audio_file):
        """
        异步播放音频文件
        
        Args:
            audio_file: 音频文件路径
        """
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"音频文件不存在: {audio_file}")
        
        try:
            subprocess.Popen([self.player, audio_file],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        except Exception as e:
            raise Exception(f"异步播放失败: {e}")


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("Usage: player.py <audio_file>")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    
    try:
        player = AudioPlayer()
        player.play(audio_file)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
