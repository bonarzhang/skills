# QoderCLI 集成技能使用指南

## 概述

QoderCLI是一个强大的终端AI编程助手，这个技能使OpenClaw能够与其集成，利用其编程能力。

## 推荐工作流程：计划-确认-执行

遵循"计划-确认-执行"的流程来确保编程任务的质量和准确性：

### 1. 计划阶段
在执行任何编程任务之前，先创建详细的计划：

```bash
# 使用工作流脚本创建计划
python3 /root/.openclaw/workspace/skills/qodercli-integration/qoder_workflow.py "您的编程需求"
```

### 2. 确认阶段
在完整实现中，系统会显示计划并等待您的确认。

### 3. 执行阶段
确认计划后，系统会在Pythonprojects/test目录中执行任务。

## 核心功能

### 1. 代码分析和理解
```bash
# 分析代码结构
qodercli -p "分析当前目录下的代码结构"

# 解释特定代码的作用
qodercli -w /path/to/project -p "解释 src/main.py 文件中 TaskManager 类的工作原理"
```

### 2. 代码审查
```bash
# 审查代码质量
qodercli -p "/review"

# 专门针对安全问题的审查
qodercli -p "检查代码中可能存在的安全漏洞"
```

### 3. 代码生成和修改
```bash
# 生成新功能
qodercli -w /path/to/project -p "添加一个删除任务的方法到TaskManager类"

# 重构代码
qodercli -w /path/to/project -p "优化这个函数的性能"
```

### 4. 项目管理
```bash
# 初始化项目记忆文件
qodercli -p "/init"

# 检查项目状态
qodercli -p "列出项目中的所有主要组件"
```

## 在OpenClaw中使用

### 直接使用exec工具
```bash
# 简单询问
exec({"command": "qodercli -p \"解释如何使用Python的asyncio库\""})

# 项目特定任务
exec({"command": "qodercli -w /path/to/project -p \"审查最近的代码更改\""})

# 检查状态
exec({"command": "qodercli status"})
```

### 使用技能包装器
```bash
# 使用Python包装器
exec({"command": "python3 /root/.openclaw/workspace/skills/qodercli-integration/qoder_helper.py non-interactive \"帮我分析这个算法的时间复杂度\""})

# 检查系统状态
exec({"command": "python3 /root/.openclaw/workspace/skills/qodercli-integration/qoder_helper.py status"})
```

## 实际应用场景

### 场景1：代码审查
当需要审查代码质量时：
```bash
qodercli -w /path/to/project -p "审查最近添加的用户认证功能，检查是否存在安全漏洞"
```

### 场景2：项目理解
当加入一个新项目时：
```bash
qodercli -w /path/to/project -p "分析这个项目的架构，解释各个模块之间的关系"
```

### 场景3：功能开发
当需要添加新功能时：
```bash
qodercli -w /path/to/project -p "实现一个缓存机制来提高数据访问速度，使用Redis作为后端"
```

### 场景4：调试问题
当遇到难以解决的bug时：
```bash
qodercli -w /path/to/project -p "分析这个错误日志，找出导致内存泄漏的原因"
```

## 安全注意事项

- QoderCLI具有文件读写和执行shell命令的能力，请在可信的项目目录中使用
- 可以通过配置文件控制权限：
  - `~/.qoder/settings.json`
  - `${project}/.qoder/settings.json`
- 使用 `--allowed-tools` 和 `--disallowed-tools` 参数限制工具访问

## 最佳实践

1. **在特定项目目录中运行**：使用 `-w` 参数指定工作目录
2. **明确任务描述**：提供清晰、具体的指令
3. **分步处理复杂任务**：将大任务分解为多个小任务
4. **定期检查进度**：使用非交互模式监控任务执行

## 故障排除

如果遇到问题：
1. 检查是否已登录：`qodercli status`
2. 检查项目权限：确保有适当的读写权限
3. 检查网络连接：某些功能可能需要网络访问
4. 检查API配额：确认账户有足够的使用额度