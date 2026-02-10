# QoderCLI 集成技能

这个技能允许OpenClaw与QoderCLI集成，利用其强大的终端编程能力。

## 功能

- 执行代码分析和审查
- 进行项目级别的开发任务
- 利用Qoder的MCP集成进行高级功能
- 非交互式代码生成和修改

## 使用方法

### 通过exec工具直接使用

```bash
# 检查QoderCLI状态
qodercli status

# 执行非交互式命令
qodercli -p "帮我分析这个项目的架构"

# 在特定项目目录中执行命令
qodercli -w /path/to/project -p "审查最近的代码更改"
```

### 通过技能脚本使用

```bash
# 使用非交互模式执行命令
python3 /root/.openclaw/workspace/skills/qodercli-integration/qoder_helper.py non-interactive "帮我重构这段代码以提高性能"

# 检查状态
python3 /root/.openclaw/workspace/skills/qodercli-integration/qoder_helper.py status

# 执行代码审查
python3 /root/.openclaw/workspace/skills/qodercli-integration/qoder_helper.py review

# 初始化项目记忆文件
python3 /root/.openclaw/workspace/skills/qodercli-integration/qoder_helper.py init
```

### 使用bash脚本

```bash
# 非交互模式
/root/.openclaw/workspace/skills/qodercli-integration/qoder_helper.sh non-interactive "帮我写一个Python函数来计算斐波那契数列"

# 在项目目录中执行
/root/.openclaw/workspace/skills/qodercli-integration/qoder_helper.sh project /path/to/project "分析这个项目的依赖关系"
```

## 适用场景

1. **代码理解**：分析现有代码库的结构和逻辑
2. **代码审查**：检查代码质量和安全性
3. **项目分析**：理解项目架构和依赖关系
4. **自动化开发**：执行重复性的开发任务
5. **文档生成**：为代码生成注释和文档

## 注意事项

- 确保QoderCLI已正确安装并登录
- 某些操作可能需要适当的项目目录权限
- 对于敏感项目，请检查权限配置以确保安全

## 配置

QoderCLI具有精细的权限控制系统，可在以下文件中配置：
- `~/.qoder/settings.json`
- `${project}/.qoder/settings.json`