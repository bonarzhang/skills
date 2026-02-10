---
name: "qodercli-integration"
description: "通过QoderCLI进行终端编程和代码开发的集成技能。Use when需要进行代码编写、代码审查、项目分析或其他软件开发任务。"
---

# QoderCLI 集成技能

通过QoderCLI进行终端编程和代码开发的集成技能。

## 功能

- 在项目中启动QoderCLI交互模式
- 执行代码分析和审查
- 进行项目级别的开发任务
- 利用Qoder的MCP集成进行浏览器控制等高级功能
- 支持"计划-确认-执行"工作流程的编程任务

## 使用方法

### 基本交互模式

```bash
# 在项目根目录启动QoderCLI交互模式
qodercli

# 在特定工作目录启动
qodercli -w /path/to/project

# 非交互模式执行单个命令
qodercli -p "Explain the use of context in Go"
```

### 计划-确认-执行工作流程（推荐）

这是推荐的编程工作流程，确保在执行前先制定计划并获得确认：

```bash
# 使用工作流脚本（在Pythonprojects/test目录中）
python3 /root/.openclaw/workspace/skills/qodercli-integration/qoder_workflow.py "您的编程需求"

# 示例
python3 /root/.openclaw/workspace/skills/qodercli-integration/qoder_workflow.py "创建一个Python程序来管理任务列表"
```

此工作流程包括：
1. **计划阶段**：分析需求并生成详细的执行计划
2. **确认阶段**：显示计划并等待确认（在完整实现中）
3. **执行阶段**：在指定目录中执行编程任务
4. **记录阶段**：保存任务上下文供后续参考

### 项目开发任务

```bash
# 初始化项目记忆文件
qodercli -p "/init"

# 进行代码审查
qodercli -p "Use code-review subagent to check code issues"

# 分析代码变更
qodercli -p "/review"
```

### 高级功能

```bash
# 使用工作树并行处理
qodercli --worktree "job description"

# 限制工具使用
qodercli --allowed-tools=READ,WRITE

# 限制对话轮数
qodercli --max-turns=10
```

## 权限控制

QoderCLI具有精细的权限控制系统，可在以下文件中配置：
- `~/.qoder/settings.json`
- `${project}/.qoder/settings.json`

## MCP 集成

QoderCLI支持MCP（Model Context Protocol）服务器，可用于：
- 浏览器控制
- 数据库访问
- 文件系统操作
- 其他外部工具集成

## 常用命令

| 命令 | 描述 |
|------|------|
| `/login` | 登录Qoder账户 |
| `/help` | 显示TUI帮助 |
| `/init` | 初始化AGENTS.md记忆文件 |
| `/memory` | 编辑记忆文件 |
| `/quest` | 任务驱动的委托任务 |
| `/review` | 代码审查本地变更 |
| `/resume` | 列出并恢复会话 |
| `/clear` | 清除当前会话上下文历史 |
| `/compact` | 概括当前会话的上下文历史 |
| `/usage` | 显示信用使用情况 |
| `/status` | 显示CLI状态 |
| `/config` | 显示系统配置 |
| `/agents` | 子代理命令：列出、创建、管理子代理 |
| `/quit` | 退出TUI |
| `/logout` | 登出Qoder账户 |

## 适用场景

- 代码理解和分析
- 项目架构设计
- 代码审查和质量检查
- 自动化开发任务
- 文档生成和维护
- 调试和故障排除