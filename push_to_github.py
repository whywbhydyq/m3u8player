#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 推送脚本
用法: python push_to_github.py "提交说明"
"""

import os
import sys
import subprocess
import datetime

def run_command(cmd, description):
    """执行命令并输出结果"""
    print(f"\n▶️ {description}...")
    print(f"   命令: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(f"   输出: {result.stdout.strip()}")
    if result.stderr and "warning" not in result.stderr.lower():
        print(f"   错误: {result.stderr.strip()}")
    return result.returncode == 0

def main():
    # 获取提交信息
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        message = f"更新站点内容 - {now}"
    
    print("="*50)
    print("M3U8播放器站点 - GitHub 推送工具")
    print("="*50)
    print(f"\n提交信息: {message}")
    
    # 检查是否在git仓库中
    if not os.path.exists('.git'):
        print("\n⚠️ 当前目录不是Git仓库，请确认位置正确")
        print(f"   当前目录: {os.getcwd()}")
        return 1
    
    # 检查远程仓库
    result = subprocess.run('git remote -v', shell=True, capture_output=True, text=True)
    if 'github.com' not in result.stdout:
        print("\n⚠️ 未配置GitHub远程仓库")
        print("   请确认已设置远程仓库: git remote add origin https://github.com/whywbhydyq/m3u8player.git")
        return 1
    
    print(f"\n远程仓库:\n{result.stdout}")
    
    # 步骤1: 检查状态
    print("\n" + "="*50)
    print("步骤 1/4: 检查Git状态")
    print("="*50)
    run_command('git status', "检查当前状态")
    
    # 步骤2: 添加所有文件
    print("\n" + "="*50)
    print("步骤 2/4: 添加文件到暂存区")
    print("="*50)
    if not run_command('git add -A', "添加所有更改"):
        print("❌ 添加文件失败")
        return 1
    
    # 步骤3: 提交更改
    print("\n" + "="*50)
    print("步骤 3/4: 提交更改")
    print("="*50)
    if not run_command(f'git commit -m "{message}"', f"提交: {message}"):
        print("⚠️ 可能没有需要提交的更改，或提交失败")
        # 检查是否有更改要提交
        status = subprocess.run('git status --porcelain', shell=True, capture_output=True, text=True)
        if not status.stdout.strip():
            print("   没有需要提交的更改")
            return 0
    
    # 步骤4: 推送到远程
    print("\n" + "="*50)
    print("步骤 4/4: 推送到GitHub")
    print("="*50)
    
    # 获取当前分支
    branch_result = subprocess.run('git branch --show-current', shell=True, capture_output=True, text=True)
    branch = branch_result.stdout.strip() or 'main'
    
    if not run_command(f'git push origin {branch}', f"推送到 {branch} 分支"):
        print("❌ 推送失败")
        print("\n可能的解决方案:")
        print("1. 检查网络连接")
        print("2. 确认有推送权限")
        print("3. 如果需要，先执行: git pull origin main")
        return 1
    
    # 完成
    print("\n" + "="*50)
    print("✅ 推送成功！")
    print("="*50)
    print(f"\n站点地址:")
    print(f"   GitHub:   https://github.com/whywbhydyq/m3u8player")
    print(f"   线上预览: https://m3u8player.gitlcp.com/")
    print("\n提示:")
    print("   - Vercel 会自动部署最新代码")
    print("   - 更新可能有1-2分钟延迟")
    print("   - 可通过 Vercel Dashboard 查看部署状态")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
