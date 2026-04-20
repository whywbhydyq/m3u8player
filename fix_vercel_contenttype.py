import os, json

filepath = os.path.join('D:\\桌面\\m3u8player', 'vercel.json')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 确保有 sitemap.xml 的正确 headers
if 'sitemap.xml' not in content:
    config = json.loads(content)
    if 'headers' not in config:
        config['headers'] = []
    config['headers'].append({
        "source": "sitemap.xml",
        "headers": [{"key": "Content-Type", "value": "application/xml"}]
    })
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print('vercel.json 已添加 sitemap Content-Type')
else:
    print('vercel.json 已包含 sitemap 配置')
