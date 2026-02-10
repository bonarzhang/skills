#!/bin/bash
# QoderCLI Integration Script
# 用于在OpenClaw中集成QoderCLI功能

set -e

# 检查qodercli是否已安装
if ! command -v qodercli &> /dev/null; then
    echo "错误: qodercli 未安装或不在PATH中"
    exit 1
fi

# 检查是否已登录
if ! qodercli status &> /dev/null; then
    echo "错误: 请先登录QoderCLI账户"
    exit 1
fi

# 获取第一个参数作为命令类型
COMMAND_TYPE="${1:-interactive}"

case $COMMAND_TYPE in
    "interactive")
        # 交互模式 - 启动TUI
        echo "启动QoderCLI交互模式..."
        shift
        qodercli "$@"
        ;;
    "non-interactive")
        # 非交互模式 - 执行单个命令
        shift
        if [ $# -eq 0 ]; then
            echo "用法: $0 non-interactive \"prompt message\""
            exit 1
        fi
        qodercli -p "$*"
        ;;
    "project")
        # 项目模式 - 在指定目录中运行
        PROJECT_DIR="${2:-.}"
        shift 2
        if [ ! -d "$PROJECT_DIR" ]; then
            echo "错误: 目录 $PROJECT_DIR 不存在"
            exit 1
        fi
        cd "$PROJECT_DIR"
        qodercli -p "$*"
        ;;
    "status")
        # 检查状态
        qodercli status
        ;;
    "review")
        # 代码审查
        qodercli -p "/review"
        ;;
    "init")
        # 初始化项目记忆文件
        qodercli -p "/init"
        ;;
    *)
        echo "用法:"
        echo "  $0 interactive [args...]     - 启动交互模式"
        echo "  $0 non-interactive \"prompt\"  - 执行非交互命令"
        echo "  $0 project DIR \"prompt\"      - 在指定目录执行命令"
        echo "  $0 status                    - 检查QoderCLI状态"
        echo "  $0 review                    - 执行代码审查"
        echo "  $0 init                      - 初始化项目记忆文件"
        exit 1
        ;;
esac