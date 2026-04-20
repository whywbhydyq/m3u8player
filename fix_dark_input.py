import os

filepath = os.path.join('D:\\桌面\\m3u8player', 'player.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# Fix: convert-url 输入框暗色背景
old = 'class="w-full px-6 py-5 border border-gray-300 dark:border-gray-700 rounded-3xl focus:outline-none focus:border-blue-500 font-mono"'
new = 'class="w-full px-6 py-5 border border-gray-300 dark:border-gray-700 rounded-3xl focus:outline-none focus:border-blue-500 font-mono bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"'
if old in content:
    content = content.replace(old, new)
    changes += 1
    print('1. convert-url 输入框暗色适配')
else:
    print('WARN: 未找到 convert-url 输入框')

# Fix: 转换页整个容器暗色背景
old2 = 'class="max-w-2xl mx-auto bg-white dark:bg-gray-900 rounded-3xl p-10 shadow-xl"'
new2 = 'class="max-w-2xl mx-auto bg-white dark:bg-gray-900 rounded-3xl p-10 shadow-xl text-gray-900 dark:text-gray-100"'
if old2 in content:
    content = content.replace(old2, new2)
    changes += 1
    print('2. 转换页容器文字暗色适配')
else:
    print('WARN: 未找到转换页容器')

# Fix: 转换页 label 文字暗色
old3 = 'class="block text-sm font-medium mb-3"'
new3 = 'class="block text-sm font-medium mb-3 text-gray-700 dark:text-gray-300"'
if old3 in content:
    content = content.replace(old3, new3)
    changes += 1
    print('3. label文字暗色适配')
else:
    print('WARN: 未找到label')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n共修改 {changes} 处')
