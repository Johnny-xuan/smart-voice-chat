#!/bin/bash
#
# SmartVoice Chat - 测试脚本
#

set -e

# 颜色
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# 测试计数
TESTS_PASSED=0
TESTS_FAILED=0

# 测试函数
test_case() {
    local name="$1"
    local command="$2"
    
    echo -n "测试: $name ... "
    
    if eval "$command" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ PASS${NC}"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}✗ FAIL${NC}"
        ((TESTS_FAILED++))
    fi
}

echo -e "${YELLOW}SmartVoice Chat - 测试套件${NC}"
echo "======================================"
echo ""

# 项目结构测试
echo "项目结构检查:"
test_case "配置文件存在" "[ -f $PROJECT_DIR/config/config.yaml ]"
test_case "主脚本存在" "[ -f $PROJECT_DIR/bin/smart-voice.sh ]"
test_case "detector.py 存在" "[ -f $PROJECT_DIR/bin/detector.py ]"
test_case "parser.py 存在" "[ -f $PROJECT_DIR/bin/parser.py ]"
test_case "stt.py 存在" "[ -f $PROJECT_DIR/bin/stt.py ]"
test_case "tts.py 存在" "[ -f $PROJECT_DIR/bin/tts.py ]"
test_case "player.py 存在" "[ -f $PROJECT_DIR/bin/player.py ]"
test_case "orchestrator.py 存在" "[ -f $PROJECT_DIR/lib/orchestrator.py ]"

echo ""
echo "Python 模块测试:"
cd "$PROJECT_DIR"
test_case "detector.py 可执行" "python3 bin/detector.py 'hello'"
test_case "parser.py 可执行" "python3 bin/parser.py 'hello'"
test_case "导入 yaml" "python3 -c 'import yaml'"

echo ""
echo "依赖检查:"
test_case "STT CLI 存在" "[ -f ~/.clawdbot/tools/sherpa-stt/sherpa-stcli.py ]"
test_case "STT 模型存在" "[ -d ~/.clawdbot/sherpa-asr/models/sherpa-onnx-paraformer-zh-2024-03-09 ]"
test_case "TTS 模型存在" "[ -d ~/.clawdbot/tools/sherpa-onnx-tts/models/vits-melo-tts-zh_en ]"

# 功能测试
echo ""
echo "功能测试:"

# 测试输入检测
echo -n "测试: 输入类型检测 (文字) ... "
INPUT_TYPE=$(python3 -c "import sys; sys.path.insert(0, 'bin'); from detector import InputDetector; print(InputDetector.detect('hello world'))")
if [ "$INPUT_TYPE" = "text" ]; then
    echo -e "${GREEN}✓ PASS${NC}"
    ((TESTS_PASSED++))
else
    echo -e "${RED}✗ FAIL${NC} (got: $INPUT_TYPE)"
    ((TESTS_FAILED++))
fi

# 测试意图解析
echo -n "测试: 意图解析 (语音关键词) ... "
INTENT=$(python3 -c "import sys; sys.path.insert(0, 'bin'); from parser import IntentParser; p = IntentParser(); print(p.parse('用语音回答：今天天气怎么样')['mode'])")
if [ "$INTENT" = "voice_only" ]; then
    echo -e "${GREEN}✓ PASS${NC}"
    ((TESTS_PASSED++))
else
    echo -e "${RED}✗ FAIL${NC} (got: $INTENT)"
    ((TESTS_FAILED++))
fi

echo ""
echo "======================================"
echo -e "测试结果: ${GREEN}$TESTS_PASSED${NC} 通过, ${RED}$TESTS_FAILED${NC} 失败"
echo "======================================"

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}所有测试通过！${NC}"
    exit 0
else
    echo -e "${RED}部分测试失败${NC}"
    exit 1
fi
