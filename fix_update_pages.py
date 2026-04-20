#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新现有页面，添加完整的SEO元素和统一风格
"""

import os
import re

def fix_about_html():
    """更新 about.html 添加完整SEO"""
    filepath = 'about.html'
    if not os.path.exists(filepath):
        print(f"⚠️  {filepath} 不存在，跳过")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有完整SEO
    if '<meta name="robots"' in content and '<link rel="canonical"' in content:
        print(f"✅ {filepath} 已有完整SEO，跳过")
        return
    
    # 添加基础SEO（如果缺失）
    seo_meta = '''<meta name="robots" content="index, follow">
    <link rel="canonical" href="https://m3u8player.gitlcp.com/about.html">
    <meta property="og:title" content="关于我们 - M3U8在线播放器">
    <meta property="og:description" content="了解M3U8在线播放器团队，专业的流媒体播放解决方案提供商。">
    <meta property="og:url" content="https://m3u8player.gitlcp.com/about.html">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="M3U8在线播放器">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="关于我们 - M3U8在线播放器">
    <meta name="twitter:description" content="了解M3U8在线播放器团队。">'''
    
    # 在 </head> 前插入
    if '<meta name="robots"' not in content:
        content = content.replace('</head>', f'{seo_meta}\n    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1653188471819736" crossorigin="anonymous"></script>\n</head>')
    
    # 更新联系邮箱
    content = content.replace('kefu888@gmail.com', '2922027393@qq.com')
    content = content.replace('kefu888#gmail.com', '2922027393@qq.com')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已更新 {filepath}")

def fix_privacy_html():
    """更新 privacy.html 确保AdSense合规"""
    filepath = 'privacy.html'
    if not os.path.exists(filepath):
        print(f"⚠️  {filepath} 不存在，跳过")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新联系邮箱
    content = content.replace('kefu888@gmail.com', '2922027393@qq.com')
    
    # 确保有完整的robots和canonical
    if '<meta name="robots"' not in content:
        content = content.replace('<head>', '''<head>
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://m3u8player.gitlcp.com/privacy.html">''')
    
    # 确保有AdSense脚本
    if 'adsbygoogle' not in content:
        content = content.replace('</head>', '''    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1653188471819736" crossorigin="anonymous"></script>\n</head>''')
    
    # 确保隐私政策包含Google退出链接
    if 'optout' not in content.lower() and '退出' not in content:
        # 在Cookie部分后添加退出说明
        optout_text = '''\n\n### 如何退出个性化广告\n\n您可以访问 [Google 广告设置](https://adssettings.google.com/) 关闭个性化广告，或使用 [Network Advertising Initiative 退出页面](https://optout.networkadvertising.org/) 选择退出。'''
        content = content.replace('## 五、隐私政策更新', optout_text + '\n\n## 五、隐私政策更新')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已更新 {filepath}")

def fix_player_html():
    """更新 player.html 添加SEO"""
    filepath = 'player.html'
    if not os.path.exists(filepath):
        print(f"⚠️  {filepath} 不存在，跳过")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否已有完整SEO
    if '<meta name="robots"' in content:
        print(f"✅ {filepath} 已有SEO，仅更新邮箱")
        content = content.replace('kefu888@gmail.com', '2922027393@qq.com')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return
    
    # 添加SEO和AdSense
    seo_tags = '''<meta name="robots" content="index, follow">
    <link rel="canonical" href="https://m3u8player.gitlcp.com/player.html">
    <meta property="og:title" content="M3U8播放器 - 在线HLS视频播放">
    <meta property="og:description" content="免费在线M3U8播放器，输入链接即可播放HLS流媒体视频。">
    <meta property="og:url" content="https://m3u8player.gitlcp.com/player.html">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1653188471819736" crossorigin="anonymous"></script>'''
    
    if '<meta name="robots"' not in content:
        content = content.replace('</head>', f'{seo_tags}\n</head>')
    
    content = content.replace('kefu888@gmail.com', '2922027393@qq.com')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ 已更新 {filepath}")

def fix_article_pages():
    """更新文章页面"""
    articles = ['post/1001.html', 'post/1002.html', 'post/index.html']
    
    for filepath in articles:
        if not os.path.exists(filepath):
            print(f"⚠️  {filepath} 不存在，跳过")
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 更新邮箱
        content = content.replace('kefu888@gmail.com', '2922027393@qq.com')
        
        # 确保有基础SEO
        if '<meta name="robots"' not in content:
            seo = '''<meta name="robots" content="index, follow">
    <link rel="canonical" href="https://m3u8player.gitlcp.com/''' + filepath + '''">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1653188471819736" crossorigin="anonymous"></script>'''
            content = content.replace('</head>', f'{seo}\n</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 已更新 {filepath}")

if __name__ == '__main__':
    print("开始更新页面...\n")
    fix_about_html()
    fix_privacy_html()
    fix_player_html()
    fix_article_pages()
    print("\n✅ 所有页面更新完成！")
