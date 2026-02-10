#!/usr/bin/env python3
"""
QoderCLI Skill 示例脚本
演示如何在OpenClaw中使用QoderCLI进行编程任务
"""

import subprocess
import sys
import os
from pathlib import Path


def create_sample_project():
    """创建一个示例项目来演示QoderCLI功能"""
    project_dir = Path("/root/.openclaw/workspace/sample-programming-project")
    project_dir.mkdir(exist_ok=True)
    
    # 创建一个简单的Python项目结构
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "tests").mkdir(exist_ok=True)
    
    # 创建一个示例Python文件
    main_py_content = '''"""
示例应用程序 - 演示QoderCLI如何处理编程任务
"""
import json
import logging
from typing import Dict, List, Optional


class TaskManager:
    """简单的任务管理器类"""
    
    def __init__(self):
        self.tasks = []
        self.logger = logging.getLogger(__name__)
    
    def add_task(self, title: str, description: str = "") -> Dict:
        """添加新任务"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False
        }
        self.tasks.append(task)
        self.logger.info(f"Added task: {title}")
        return task
    
    def complete_task(self, task_id: int) -> bool:
        """标记任务为完成"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.logger.info(f"Completed task: {task_id}")
                return True
        return False
    
    def get_tasks(self) -> List[Dict]:
        """获取所有任务"""
        return self.tasks


def main():
    """主函数"""
    tm = TaskManager()
    
    # 添加一些示例任务
    tm.add_task("学习QoderCLI", "掌握QoderCLI的使用方法")
    tm.add_task("创建项目", "创建一个新项目")
    
    # 显示任务
    print("当前任务:")
    for task in tm.get_tasks():
        status = "✓" if task["completed"] else "○"
        print(f"{status} {task['id']}: {task['title']}")


if __name__ == "__main__":
    main()
'''
    
    with open(project_dir / "src" / "main.py", "w", encoding="utf-8") as f:
        f.write(main_py_content)
    
    # 创建requirements.txt
    requirements_content = '''# 示例项目依赖
# 可以通过QoderCLI分析和管理依赖
'''
    
    with open(project_dir / "requirements.txt", "w", encoding="utf-8") as f:
        f.write(requirements_content)
    
    # 创建README.md
    readme_content = '''# 示例编程项目

这是一个演示QoderCLI功能的示例项目。

## 项目结构
- `src/main.py`: 主程序文件
- `tests/`: 测试文件目录
- `requirements.txt`: 项目依赖

## 如何使用QoderCLI

可以使用以下命令来分析和修改此项目：

```bash
# 分析项目结构
qodercli -w /path/to/project -p "分析这个项目的结构和功能"

# 重构代码
qodercli -w /path/to/project -p "优化TaskManager类的性能"

# 添加功能
qodercli -w /path/to/project -p "为TaskManager类添加删除任务的功能"
```
'''
    
    with open(project_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    return project_dir


def demonstrate_qodercli_usage():
    """演示如何使用QoderCLI进行编程任务"""
    print("创建示例项目...")
    project_dir = create_sample_project()
    print(f"示例项目已创建在: {project_dir}")
    
    print("\n使用QoderCLI分析项目...")
    cmd = ["qodercli", "-w", str(project_dir), "-p", "分析这个项目的结构和主要功能"]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("QoderCLI分析结果:")
            print("="*50)
            print(result.stdout)
            print("="*50)
        else:
            print(f"命令执行失败: {result.stderr}")
    except subprocess.TimeoutExpired:
        print("命令执行超时")
    except Exception as e:
        print(f"执行过程中出现错误: {e}")
    
    print(f"\n您现在可以在 {project_dir} 目录中使用QoderCLI进行编程任务")


if __name__ == "__main__":
    demonstrate_qodercli_usage()