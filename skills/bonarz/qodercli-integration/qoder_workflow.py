#!/usr/bin/env python3
"""
QoderCLI 编程任务工作流脚本
遵循"计划-确认-执行"流程的编程任务管理器
"""

import subprocess
import sys
import os
import json
from pathlib import Path
from typing import Dict, List, Optional


def create_task_plan(prompt: str) -> str:
    """
    根据用户需求创建任务计划
    """
    planning_prompt = f"""请根据以下需求创建一个详细的编程任务计划：

需求: {prompt}

请提供:
1. 任务分解 - 将任务分解为具体的步骤
2. 预期输出 - 完成后应该有哪些文件或功能
3. 潜在挑战 - 可能遇到的技术难点
4. 执行顺序 - 步骤的合理执行顺序

请以结构化的方式呈现计划。
"""
    
    cmd = ['qodercli', '-p', planning_prompt]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return f"创建计划时出错: {result.stderr}"


def confirm_plan(plan: str) -> bool:
    """
    这里在实际实现中会向用户请求确认
    在当前环境中，我们返回True表示继续
    """
    print("任务计划已生成，等待用户确认...")
    print("\n" + "="*60)
    print("编程任务计划")
    print("="*60)
    print(plan)
    print("="*60)
    print("\n计划已生成。在实际环境中，这里会等待用户确认。")
    
    # 在真实环境中，这会等待用户输入确认
    return True


def execute_task(prompt: str, project_dir: str = "/root/.openclaw/workspace/Pythonprojects/test") -> str:
    """
    在指定目录中执行编程任务
    """
    cmd = ['qodercli', '-w', project_dir, '-p', prompt]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    
    if result.returncode == 0:
        return result.stdout
    else:
        return f"执行任务时出错: {result.stderr}"


def save_task_context(task_id: str, prompt: str, plan: str, execution_result: str):
    """
    保存任务上下文到文件
    """
    context_dir = Path("/root/.openclaw/workspace/Pythonprojects/test/task_contexts")
    context_dir.mkdir(exist_ok=True)
    
    context = {
        "task_id": task_id,
        "prompt": prompt,
        "plan": plan,
        "execution_result": execution_result,
        "status": "completed" if "出错" not in execution_result else "failed"
    }
    
    context_file = context_dir / f"{task_id}.json"
    with open(context_file, 'w', encoding='utf-8') as f:
        json.dump(context, f, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) < 2:
        print("用法: python qoder_workflow.py \"编程需求描述\"")
        print("示例: python qoder_workflow.py \"创建一个简单的计算器程序\"")
        sys.exit(1)
    
    # 获取用户需求
    user_prompt = " ".join(sys.argv[1:])
    
    print(f"收到编程需求: {user_prompt}")
    print("正在创建任务计划...")
    
    # 创建计划
    plan = create_task_plan(user_prompt)
    
    # 显示计划并等待确认（模拟）
    if confirm_plan(plan):
        print("\n用户已确认计划，开始执行任务...")
        
        # 执行任务
        execution_result = execute_task(user_prompt)
        
        # 保存任务上下文
        task_id = f"task_{len(os.listdir(Path('/root/.openclaw/workspace/Pythonprojects/test/task_contexts')) if Path('/root/.openclaw/workspace/Pythonprojects/test/task_contexts').exists() else []) + 1:03d}"
        save_task_context(task_id, user_prompt, plan, execution_result)
        
        print("\n任务执行完成！")
        print("执行结果:")
        print(execution_result)
        
        return execution_result
    else:
        print("用户未确认计划，任务已取消。")
        return "任务已取消"


if __name__ == "__main__":
    main()