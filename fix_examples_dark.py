import os

# ========== 修复 player.html ==========
filepath = os.path.join('D:\\桌面\\m3u8player', 'player.html')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# Fix 1: 替换第一个示例链接（CORS不可用）
old1 = 'https://test-streams.mux.dev/x264_720p_1500kbs_30fps/index.m3u8'
new1 = 'https://devstreaming-cdn.apple.com/videos/streaming/examples/img_bipbop_adv_example_fmp4/master.m3u8'
count = content.count(old1)
if count > 0:
    content = content.replace(old1, new1)
    changes += count
    print(f'1. 替换不可用示例链接 ({count}处)')
else:
    print('WARN: 未找到第一个示例链接')

# Fix 2: 示例数组中第一个改为Apple流，第三个改为x36xhzz
old_urls = '''const urls = [
                "https://devstreaming-cdn.apple.com/videos/streaming/examples/img_bipbop_adv_example_fmp4/master.m3u8",
                "https://devstreaming-cdn.apple.com/videos/streaming/examples/img_bipbop_adv_example_fmp4/master.m3u8",
                "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"
            };'''
new_urls = '''const urls = [
                "https://devstreaming-cdn.apple.com/videos/streaming/examples/img_bipbop_adv_example_fmp4/master.m3u8",
                "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
                "https://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_16x9/bipbop_16x9_variant.m3u8"
            ];'''
if old_urls in content:
    content = content.replace(old_urls, new_urls)
    changes += 1
    print('2. 示例链接数组更新（3个均为可用流）')
else:
    print('WARN: 未找到示例URL数组，尝试单独替换')

# Fix 3: 加载锁防重复点击
old3 = '''        let hls = null;
        let mediaRecorder = null;
        let recordedChunks = [];
        let isRecording = false;
        let recordedBlob = null;
        let currentTab = 0;
        let darkMode = false;'''
new3 = '''        let hls = null;
        let mediaRecorder = null;
        let recordedChunks = [];
        let isRecording = false;
        let recordedBlob = null;
        let currentTab = 0;
        let darkMode = false;
        let isLoading = false;'''
if old3 in content:
    content = content.replace(old3, new3)
    changes += 1
    print('3. 添加 isLoading 锁变量')
else:
    print('WARN: 未找到变量声明区')

# Fix 4: loadAndPlay 加加载锁
old4 = """            log('\u6b63\u5728\u52a0\u8f7d: ' + urlInput.substring(0, 60) + '...');
            
            if (typeof Hls !== 'undefined' && Hls.isSupported()) {"""
new4 = """            if (isLoading) { log('\u6b63\u5728\u52a0\u8f7d\u4e2d\uff0c\u8bf7\u7b49\u5f85...'); return; }
            isLoading = true;
            log('\u6b63\u5728\u52a0\u8f7d: ' + urlInput.substring(0, 60) + '...');
            
            if (typeof Hls !== 'undefined' && Hls.isSupported()) {"""
if old4 in content:
    content = content.replace(old4, new4)
    changes += 1
    print('4. loadAndPlay 添加加载锁入口')
else:
    print('WARN: 未找到加载入口')

# Fix 5: hls.destroy 后释放锁 + play catch 释放锁
old5 = """            if (hls) {
                hls.destroy();
                hls = null;
            }
            
            log('\u6b63\u5728\u52a0\u8f7d"""
new5 = """            if (hls) {
                hls.destroy();
                hls = null;
            }
            
            isLoading = false;
            log('\u6b63\u5728\u52a0\u8f7d"""
if old5 in content:
    content = content.replace(old5, new5)
    changes += 1
    print('5. destroy后释放isLoading锁')
else:
    print('WARN: 未找到destroy区')

# Fix 6: MANIFEST_PARSED 释放锁
old6 = """log('M3U8\u6e05\u5355\u89e3\u6790\u6210\u529f\uff0c\u627e\u5230 ' + data.levels.length + ' \u4e2a\u6e05\u6670\u5ea6', 'success');
                    video.play().catch(e => log('\u81ea\u52a8\u64ad\u653e\u5931\u8d25: ' + e.message, 'error'));"""
new6 = """isLoading = false;
                    log('M3U8\u6e05\u5355\u89e3\u6790\u6210\u529f\uff0c\u627e\u5230 ' + data.levels.length + ' \u4e2a\u6e05\u6670\u5ea6', 'success');
                    video.play().catch(e => log('\u81ea\u52a8\u64ad\u653e\u5931\u8d25: ' + e.message, 'error'));"""
if old6 in content:
    content = content.replace(old6, new6)
    changes += 1
    print('6. MANIFEST_PARSED释放锁')
else:
    print('WARN: 未找到MANIFEST_PARSED')

# Fix 7: 错误时也释放锁
old7 = """                    if (data.fatal) {
                        log('\u81f4\u547d\u9519\u8bef: ' + data.type + ' - ' + data.details, 'error');
                        if (data.type === Hls.ErrorTypes.NETWORK_ERROR) {"""
new7 = """                    if (data.fatal) {
                        isLoading = false;
                        log('\u81f4\u547d\u9519\u8bef: ' + data.type + ' - ' + data.details, 'error');
                        if (data.type === Hls.ErrorTypes.NETWORK_ERROR) {"""
if old7 in content:
    content = content.replace(old7, new7)
    changes += 1
    print('7. 错误时释放锁')
else:
    print('WARN: 未找到错误处理')

# Fix 8: Safari分支释放锁
old8 = """                log('\u4f7f\u7528Safari\u539f\u751fHLS\u652f\u6301', 'success');
                video.play();"""
new8 = """                isLoading = false;
                log('\u4f7f\u7528Safari\u539f\u751fHLS\u652f\u6301', 'success');
                video.play();"""
if old8 in content:
    content = content.replace(old8, new8)
    changes += 1
    print('8. Safari分支释放锁')
else:
    print('WARN: 未找到Safari分支')

# Fix 9: 转MP4标签页 - 输入框暗色模式
old9 = '''class="w-full px-6 py-5 border border-gray-300 dark:border-gray-700 rounded-3xl focus:outline-none focus:border-blue-500 font-mono"
                               placeholder="https://example.com/playlist.m3u8" value="https://test-streams.mux.dev/x264_720p_1500kbs_30fps/index.m3u8"'''
new9 = '''class="w-full px-6 py-5 border border-gray-300 dark:border-gray-700 rounded-3xl focus:outline-none focus:border-blue-500 font-mono bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100"
                               placeholder="https://example.com/playlist.m3u8" value="https://devstreaming-cdn.apple.com/videos/streaming/examples/img_bipbop_adv_example_fmp4/master.m3u8"'''
if old9 in content:
    content = content.replace(old9, new9)
    changes += 1
    print('9. 转换页输入框暗色适配 + 默认URL修复')
else:
    print('WARN: 未找到转换页输入框')

# Fix 10: 转换页 select 暗色模式
old10 = '''<select id="quality" class="w-full px-6 py-5 border border-gray-300 dark:border-gray-700 rounded-3xl">
                                <option value="high">\u6700\u9ad8\u753b\u8d28</option>'''
new10 = '''<select id="quality" class="w-full px-6 py-5 border border-gray-300 dark:border-gray-700 rounded-3xl bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">
                                <option value="high">\u6700\u9ad8\u753b\u8d28</option>'''
if old10 in content:
    content = content.replace(old10, new10)
    changes += 1
    print('10. 画质select暗色适配')
else:
    print('WARN: 未找到画质select')

# Fix 11: 时长select暗色模式
old11 = '''<select id="duration" class="w-full px-6 py-5 border border-gray-300 dark:border-gray-700 rounded-3xl">
                                <option value="60">60\u79d2</option>'''
new11 = '''<select id="duration" class="w-full px-6 py-5 border border-gray-300 dark:border-gray-700 rounded-3xl bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100">
                                <option value="60">60\u79d2</option>'''
if old11 in content:
    content = content.replace(old11, new11)
    changes += 1
    print('11. 时长select暗色适配')
else:
    print('WARN: 未找到时长select')

# Fix 12: 转换页底部文字暗色
old12 = '''<div class="text-center mt-10 text-xs text-gray-500 max-w-md mx-auto">'''
new12 = '''<div class="text-center mt-10 text-xs text-gray-500 dark:text-gray-400 max-w-md mx-auto">'''
if old12 in content:
    content = content.replace(old12, new12)
    changes += 1
    print('12. 转换页底部文字暗色适配')
else:
    print('WARN: 未找到底部文字')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'\nplayer.html 共修改 {changes} 处')

# ========== 修复 m3u8_to_mp4/index.html 暗色模式 ==========
filepath2 = os.path.join('D:\\桌面\\m3u8player', 'm3u8_to_mp4', 'index.html')
with open(filepath2, 'r', encoding='utf-8') as f:
    c2 = f.read()

c2_changes = 0

# 给 input 加暗色
old_inp = 'class="flex: 1; padding: 14px 18px;'
# Actually the input uses inline style in CSS, let me check
# The .input-group input style is in CSS section
old_css_input = '''.input-group input { 
      flex: 1; 
      padding: 14px 18px; 
      border: 2px solid #e2e8f0; 
      border-radius: 8px; 
      font-size: 16px; 
      transition: border-color 0.2s; 
    }'''
new_css_input = '''.input-group input { 
      flex: 1; 
      padding: 14px 18px; 
      border: 2px solid #e2e8f0; 
      border-radius: 8px; 
      font-size: 16px; 
      transition: border-color 0.2s; 
      background: #fff; 
      color: #2d3748; 
    }
    @media (prefers-color-scheme: dark) {
      .input-group input { background: #1a202c; color: #e2e8f0; border-color: #4a5568; }
      .option input, .option select { background: #1a202c; color: #e2e8f0; border-color: #4a5568; }
      .converter { background: #1a202c; }
      .feature { background: #1a202c; }
      .steps { background: #1a202c; }
      body { background: #0d1117; color: #e2e8f0; }
      .status.info { background: #1a365d; color: #90cdf4; }
      .status.error { background: #742a2a; color: #feb2b2; }
      .status.success { background: #22543d; color: #9ae6b4; }
    }'''
if old_css_input in c2:
    c2 = c2.replace(old_css_input, new_css_input)
    c2_changes += 1
    print('13. m3u8_to_mp4 暗色模式CSS')
else:
    print('WARN: 未找到input CSS')

with open(filepath2, 'w', encoding='utf-8') as f:
    f.write(c2)
print(f'm3u8_to_mp4/index.html 共修改 {c2_changes} 处')

print(f'\n总计修改 {changes + c2_changes} 处')
