#!/bin/bash
#
# SmartVoice Chat - 主入口脚本
# 智能语音对话系统
#

set -e

# 获取脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Python 路径
export PYTHONPATH="$PROJECT_DIR/lib:$PROJECT_DIR/bin:$PYTHONPATH"

# 配置文件
CONFIG_FILE="$PROJECT_DIR/config/config.yaml"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 显示帮助
show_help() {
    cat << HELP
SmartVoice Chat - 智能语音对话系统

用法:
  smart-voice.sh [选项] [输入]

选项:
  -h, --help          显示此帮助信息
  -m, --mode MODE     输出模式: dual, voice_only, text_only
  -i, --interactive   交互模式（循环对话）
  -v, --version       显示版本信息

输入:
  音频文件路径        自动识别语音并转文字
  文字内容            直接处理文字
  (无输入)            交互模式

示例:
  # 处理音频文件
  smart-voice.sh /path/to/audio.wav

  # 处理文字输入
  smart-voice.sh "今天天气怎么样"

  # 交互模式
  smart-voice.sh -i

  # 指定输出模式
  smart-voice.sh -m voice_only "读一下这段话"

输出模式控制（在对话中）:
  "用语音回答"        强制语音输出
  "用文字回答"        强制文字输出
  默认行为            双模式输出（文字+语音）

HELP
}

# 显示版本
show_version() {
    echo "SmartVoice Chat v1.0.0"
    echo "Sherpa-ONNX 全栈语音对话系统"
}

# 处理输入
process_input() {
    local input="$1"
    local mode="$2"
    
    # 调用 Python 编排器
    python3 - << PYTHON
import sys
sys.path.insert(0, '$PROJECT_DIR/lib')
sys.path.insert(0, '$PROJECT_DIR/bin')

from orchestrator import VoiceOrchestrator

orchestrator = VoiceOrchestrator('$CONFIG_FILE')

try:
    result = orchestrator.process('$input')
    orchestrator.print_result(result)
except Exception as e:
    print(f"${RED}Error: {e}${NC}", file=sys.stderr)
    sys.exit(1)
PYTHON
}

# 交互模式
interactive_mode() {
    echo -e "${GREEN}SmartVoice Chat - 交互模式${NC}"
    echo "输入 'quit' 或 'exit' 退出"
    echo ""
    
    while true; do
        echo -n "${YELLOW}你:${NC} "
        read -e input
        
        # 检查退出命令
        if [[ "$input" == "quit" ]] || [[ "$input" == "exit" ]]; then
            echo "再见！"
            break
        fi
        
        # 处理输入
        process_input "$input"
    done
}

# 主函数
main() {
    local mode=""
    local interactive=false
    local input=""
    
    # 解析参数
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_help
                exit 0
                ;;
            -v|--version)
                show_version
                exit 0
                ;;
            -m|--mode)
                mode="$2"
                shift 2
                ;;
            -i|--interactive)
                interactive=true
                shift
                ;;
            -*)
                echo -e "${RED}未知选项: $1${NC}" >&2
                show_help
                exit 1
                ;;
            *)
                input="$1"
                shift
                ;;
        esac
    done
    
    # 执行相应模式
    if $interactive || [[ -z "$input" ]]; then
        interactive_mode
    else
        process_input "$input" "$mode"
    fi
}

# 运行主函数
main "$@"
