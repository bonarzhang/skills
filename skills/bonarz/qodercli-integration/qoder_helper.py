#!/usr/bin/env python3
"""
QoderCLI Integration for OpenClaw
提供一个Python接口来调用QoderCLI的各种功能
"""

import subprocess
import sys
import json
import os
from typing import Optional, Dict, Any


def run_qoder_command(mode: str, *args, **kwargs) -> Dict[str, Any]:
    """
    运行QoderCLI命令
    
    Args:
        mode: 运行模式 ('interactive', 'non-interactive', 'project', 'status', 'review', 'init')
        *args: 附加参数
        **kwargs: 附加关键字参数
    
    Returns:
        包含命令执行结果的字典
    """
    try:
        # 检查qodercli是否已安装
        result = subprocess.run(['which', 'qodercli'], 
                              capture_output=True, text=True, check=False)
        if result.returncode != 0:
            return {
                'success': False,
                'error': 'qodercli 未安装或不在PATH中',
                'output': '',
                'return_code': result.returncode
            }
        
        # 检查是否已登录
        status_result = subprocess.run(['qodercli', 'status'], 
                                    capture_output=True, text=True, check=False)
        if status_result.returncode != 0:
            return {
                'success': False,
                'error': '请先登录QoderCLI账户',
                'output': status_result.stderr,
                'return_code': status_result.returncode
            }
        
        # 根据模式构建命令
        if mode == 'non-interactive':
            if not args:
                return {
                    'success': False,
                    'error': '非交互模式需要提供提示消息',
                    'output': '',
                    'return_code': 1
                }
            cmd = ['qodercli', '-p', args[0]]
        elif mode == 'project':
            if len(args) < 2:
                return {
                    'success': False,
                    'error': '项目模式需要提供目录和提示消息',
                    'output': '',
                    'return_code': 1
                }
            project_dir = args[0]
            prompt = args[1]
            if not os.path.isdir(project_dir):
                return {
                    'success': False,
                    'error': f'目录 {project_dir} 不存在',
                    'output': '',
                    'return_code': 1
                }
            cmd = ['qodercli', '-w', project_dir, '-p', prompt]
        elif mode == 'status':
            cmd = ['qodercli', 'status']
        elif mode == 'review':
            cmd = ['qodercli', '-p', '/review']
        elif mode == 'init':
            cmd = ['qodercli', '-p', '/init']
        elif mode == 'interactive':
            # 交互模式通常不应该在自动化脚本中使用
            return {
                'success': False,
                'error': '交互模式不适合自动化使用',
                'output': '',
                'return_code': 1
            }
        else:
            return {
                'success': False,
                'error': f'未知模式: {mode}',
                'output': '',
                'return_code': 1
            }
        
        # 添加额外参数（如果有）
        if 'extra_args' in kwargs:
            cmd.extend(kwargs['extra_args'])
        
        # 执行命令
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        return {
            'success': result.returncode == 0,
            'output': result.stdout,
            'error': result.stderr,
            'return_code': result.returncode,
            'command': ' '.join(cmd)
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'output': '',
            'return_code': -1
        }


def main():
    """主函数，允许从命令行调用"""
    if len(sys.argv) < 2:
        print("用法: python qoder_helper.py <mode> [args...]")
        print("模式: non-interactive, project, status, review, init")
        sys.exit(1)
    
    mode = sys.argv[1]
    args = sys.argv[2:]
    
    result = run_qoder_command(mode, *args)
    
    if result['success']:
        print(result['output'])
        sys.exit(0)
    else:
        print(f"错误: {result['error']}", file=sys.stderr)
        if result['output']:
            print(result['output'])
        sys.exit(result['return_code'])


if __name__ == '__main__':
    main()