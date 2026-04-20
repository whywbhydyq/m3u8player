import os

filepath = os.path.join('D:\\桌面\\m3u8player', 'sitemap.xml')
with open(filepath, 'rb') as f:
    raw = f.read()

if raw[:3] == b'\xef\xbb\xbf':
    with open(filepath, 'wb') as f:
        f.write(raw[3:])
    print('已移除 BOM')
else:
    print('无 BOM，文件正常')

# 同时确认编码正确
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
print('sitemap.xml 前80字符:', repr(content[:80]))
