#!/bin/bash
#
# SmartVoice Chat - 安装脚本
#

set -e

# 颜色
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}SmartVoice Chat 安装向导${NC}"
echo "======================================"
echo ""

# 检查 Python 3
echo -n "检查 Python 3..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | awk '{print $2}')
    echo -e " ${GREEN}✓${NC} (版本: $PYTHON_VERSION)"
else
    echo -e " ${RED}✗${NC} 未安装"
    echo "请先安装 Python 3.8+"
    exit 1
fi

# 检查 pip3
echo -n "检查 pip3..."
if command -v pip3 &> /dev/null; then
    echo -e " ${GREEN}✓${NC}"
else
    echo -e " ${RED}✗${NC} 未安装"
    exit 1
fi

# 检查 Sherpa-ONNX STT
echo -n "检查 STT 模型..."
if [ -d ~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09 ]; then
    echo -e " ${GREEN}✓${NC}"
else
    echo -e " ${YELLOW}⚠${NC} 未找到"
    echo "请先安装 Sherpa-ONNX STT 模型"
fi

# 检查 Sherpa-ONNX TTS
echo -n "检查 TTS 模型..."
if [ -d ~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en ]; then
    echo -e " ${GREEN}✓${NC}"
else
    echo -e " ${YELLOW}⚠${NC} 未找到"
    echo "请先安装 Sherpa-ONNX TTS 模型"
fi

# 安装 Python 依赖
echo ""
echo -n "安装 Python 依赖..."
pip3 install -q -r requirements.txt
echo -e " ${GREEN}✓${NC}"

# 创建临时目录
echo -n "创建临时目录..."
mkdir -p /tmp/smart-voice-chat
echo -e " ${GREEN}✓${NC}"

# 设置权限
echo -n "设置脚本权限..."
chmod +x bin/*.py
chmod +x bin/*.sh
chmod +x lib/*.py
echo -e " ${GREEN}✓${NC}"

# 创建符号链接（可选）
echo ""
read -p "创建全局命令链接？(y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -n "创建 smart-voice 命令..."
    mkdir -p ~/.local/bin
    ln -sf "$(pwd)/bin/smart-voice.sh" ~/.local/bin/smart-voice
    echo -e " ${GREEN}✓${NC}"
    
    # 检查 PATH
    if [[ :$PATH: != *:$HOME/.local/bin:* ]]; then
        echo -e "${YELLOW}注意: ~/.local/bin 不在 PATH 中${NC}"
        echo "请添加到 ~/.zshrc 或 ~/.bashrc:"
        echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    fi
fi

echo ""
echo -e "${GREEN}======================================"
echo "安装完成！"
echo "======================================${NC}"
echo ""
echo "开始使用:"
echo "  ./bin/smart-voice.sh -i"
echo ""
echo "或查看帮助:"
echo "  ./bin/smart-voice.sh --help"
echo ""
