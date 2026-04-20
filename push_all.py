#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
M3U8播放器 - 完整推送脚本
将生成的文件推送到GitHub仓库
"""

import os
import subprocess
import sys

def run_command(cmd, cwd=None):
    """执行命令并返回结果"""
    print(f">>> 执行: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"错误: {result.stderr}")
        return False, result.stderr
    print(result.stdout)
    return True, result.stdout

def main():
    # 配置
    repo_url = "https://github.com/whywbhydyq/m3u8player.git"
    local_path = r"D:\桌面\m3u8player"  # 用户本地路径
    
    print("=" * 60)
    print("M3U8播放器 - Git推送脚本")
    print("=" * 60)
    
    # 检查本地目录
    if not os.path.exists(local_path):
        print(f"创建目录: {local_path}")
        os.makedirs(local_path, exist_ok=True)
    
    # 进入项目目录
    os.chdir(local_path)
    print(f"当前目录: {os.getcwd()}")
    
    # 检查是否是git仓库
    if not os.path.exists(os.path.join(local_path, ".git")):
        print("初始化Git仓库...")
        success, _ = run_command("git init")
        if not success:
            print("Git初始化失败")
            return
        
        # 添加远程仓库
        run_command(f"git remote add origin {repo_url}")
    
    # 获取当前远程仓库
    print("\n当前远程仓库:")
    run_command("git remote -v")
    
    # 拉取最新代码（避免冲突）
    print("\n拉取远程代码...")
    run_command("git pull origin main --allow-unrelated-histories || git pull origin master --allow-unrelated-histories")
    
    # 添加所有文件
    print("\n添加文件到暂存区...")
    files_to_add = [
        "robots.txt",
        "ads.txt", 
        "vercel.json",
        "sitemap.xml",
        "404.html",
        "contact.html",
        "index.html",
        "player.html",
        "about.html",
        "privacy.html",
        "post/1001.html",
        "post/1002.html",
        "post/1003.html",
        "post/1004.html",
        "m3u8_to_mp4/index.html"
    ]
    
    for file in files_to_add:
        run_command(f"git add {file}")
    
    # 检查状态
    print("\nGit状态:")
    run_command("git status")
    
    # 提交
    print("\n提交更改...")
    commit_msg = "feat: 重构站点 - 完善SEO、添加必需文件、优化结构"
    success, _ = run_command(f'git commit -m "{commit_msg}"')
    if not success:
        print("没有需要提交的更改，或提交失败")
        return
    
    # 推送到远程
    print("\n推送到GitHub...")
    success, output = run_command("git push origin main || git push origin master")
    if success:
        print("\n" + "=" * 60)
        print("✅ 推送成功!")
        print("=" * 60)
        print(f"仓库地址: {repo_url}")
        print(f"线上预览: https://m3u8player.gitlcp.com/")
        print("\n下一步:")
        print("1. 登录 Vercel 导入此仓库部署")
        print("2. 添加自定义域名 m3u8player.gitlcp.com")
        print("3. 在 Cloudflare 添加 CNAME 指向 cname.vercel-dns.com")
    else:
        print("\n❌ 推送失败，请检查错误信息")

if __name__ == "__main__":
    main()