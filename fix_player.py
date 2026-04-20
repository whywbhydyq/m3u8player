import os

filepath = os.path.join('D:\\桌面\\m3u8player', 'player.html')

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# Fix 1: MediaRecorder mimeType 回退链（Firefox不支持vp9，导致录制崩溃）
old1 = """                mediaRecorder = new MediaRecorder(video.captureStream(), {
                    mimeType: 'video/webm;codecs=vp9'  // webm is widely supported, we can convert name to mp4 or use webm
                });"""
new1 = """                let mimeType = 'video/webm;codecs=vp9';
                if (!MediaRecorder.isTypeSupported(mimeType)) mimeType = 'video/webm;codecs=vp8';
                if (!MediaRecorder.isTypeSupported(mimeType)) mimeType = 'video/webm';
                if (!MediaRecorder.isTypeSupported(mimeType)) mimeType = '';
                mediaRecorder = new MediaRecorder(video.captureStream(), mimeType ? { mimeType: mimeType } : {});"""
if old1 in content:
    content = content.replace(old1, new1)
    changes += 1
    print('1. MediaRecorder mimeType 回退链')
else:
    print('WARN: 未找到 MediaRecorder 代码块')

# Fix 2: Hls 类型检查（CDN加载失败时不崩溃）
old2 = """            log('正在加载: ' + urlInput.substring(0, 60) + '...');
            
            if (Hls.isSupported()) {"""
new2 = """            log('正在加载: ' + urlInput.substring(0, 60) + '...');
            
            if (typeof Hls !== 'undefined' && Hls.isSupported()) {"""
if old2 in content:
    content = content.replace(old2, new2)
    changes += 1
    print('2. Hls 类型检查防崩溃')
else:
    print('WARN: 未找到 Hls.isSupported()')

# Fix 3: 页脚 MP4转换 链接指向正确页面
old3 = '<a href="https://m3u8player.gitlcp.com/player.html#tab1" class="block hover:text-blue-600">MP4转换</a>'
new3 = '<a href="https://m3u8player.gitlcp.com/m3u8_to_mp4/index.html" class="block hover:text-blue-600">M3U8转MP4</a>'
if old3 in content:
    content = content.replace(old3, new3)
    changes += 1
    print('3. 页脚MP4转换链接')
else:
    print('WARN: 未找到页脚MP4转换链接')

# Fix 4: 第三个示例链接（earthcam CORS不可用）
old4 = 'https://videos-3.earthcam.com/fecnetwork/13306.flv/playlist.m3u8'
new4 = 'https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8'
if old4 in content:
    content = content.replace(old4, new4)
    changes += 1
    print('4. 第三个示例链接')
else:
    print('WARN: 未找到第三个示例链接')

# Fix 5: 第三个示例 Referer 清空
old5 = 'const referers = ["", "", "https://www.earthcam.com"];'
new5 = 'const referers = ["", "", ""];'
if old5 in content:
    content = content.replace(old5, new5)
    changes += 1
    print('5. 第三个示例Referer')
else:
    print('WARN: 未找到Referer数组')

# Fix 6: 暗黑模式持久化 localStorage
old6 = """            darkMode = !darkMode;
            if (darkMode) {
                document.documentElement.classList.add('dark');
                document.getElementById('theme-icon').textContent = '\u2600\ufe0f';
            } else {
                document.documentElement.classList.remove('dark');
                document.getElementById('theme-icon').textContent = '\ud83c\udf19';
            }"""
new6 = """            darkMode = !darkMode;
            if (darkMode) {
                document.documentElement.classList.add('dark');
                localStorage.theme = 'dark';
                document.getElementById('theme-icon').textContent = '\u2600\ufe0f';
            } else {
                document.documentElement.classList.remove('dark');
                localStorage.theme = 'light';
                document.getElementById('theme-icon').textContent = '\ud83c\udf19';
            }"""
if old6 in content:
    content = content.replace(old6, new6)
    changes += 1
    print('6. 暗黑模式localStorage持久化')
else:
    print('WARN: 未找到暗黑模式切换')

# Fix 7: 自动暗黑模式检查 localStorage
old7 = """            if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                darkMode = true;
                document.documentElement.classList.add('dark');
                document.getElementById('theme-icon').textContent = '\u2600\ufe0f';
            }"""
new7 = """            if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                darkMode = true;
                document.documentElement.classList.add('dark');
                document.getElementById('theme-icon').textContent = '\u2600\ufe0f';
            }"""
if old7 in content:
    content = content.replace(old7, new7)
    changes += 1
    print('7. 自动暗黑模式localStorage检查')
else:
    print('WARN: 未找到自动暗黑模式')

# Fix 8: 重写 startConversion + downloadConvertedFile（核心修复）
start_marker = '        // Converter functions (uses the same player logic internally)\n        let convertedBlob = null;'
end_marker = "            log('MP4 (WebM) \u6587\u4ef6\u5df2\u4e0b\u8f7d', 'success');\n        }"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    end_idx += len(end_marker)
    new_converter = """        // Converter functions
        let convertedBlob = null;
        let conversionRecorder = null;
        let conversionChunks = [];
        let conversionInterval = null;

        function startConversion() {
            const url = document.getElementById('convert-url').value.trim();
            if (!url) { alert('\u8bf7\u8f93\u5165M3U8\u5730\u5740'); return; }

            const progressContainer = document.getElementById('conversion-progress');
            const progressBar = document.getElementById('progress-bar');
            const progressText = document.getElementById('progress-text');
            const resultContainer = document.getElementById('conversion-result');
            const duration = parseInt(document.getElementById('duration').value) * 1000;

            progressContainer.classList.remove('hidden');
            resultContainer.classList.add('hidden');
            progressBar.style.width = '5%';
            progressText.textContent = '\u6b63\u5728\u52a0\u8f7d\u89c6\u9891\u6d41...';

            if (conversionInterval) { clearInterval(conversionInterval); conversionInterval = null; }
            if (conversionRecorder && conversionRecorder.state !== 'inactive') { conversionRecorder.stop(); }
            conversionChunks = [];

            switchTab(0);
            document.getElementById('m3u8-url').value = url;
            if (hls) { hls.destroy(); hls = null; }

            const video = document.getElementById('video');
            let started = false;

            function beginRec() {
                if (started) return;
                started = true;
                try {
                    let mime = 'video/webm;codecs=vp9';
                    if (!MediaRecorder.isTypeSupported(mime)) mime = 'video/webm;codecs=vp8';
                    if (!MediaRecorder.isTypeSupported(mime)) mime = 'video/webm';
                    if (!MediaRecorder.isTypeSupported(mime)) mime = '';
                    const stream = video.captureStream ? video.captureStream() : (video.mozCaptureStream ? video.mozCaptureStream() : null);
                    if (!stream) { progressText.textContent = '\u6d4f\u89c8\u5668\u4e0d\u652f\u6301\u6d41\u6355\u83b7'; return; }
                    conversionRecorder = new MediaRecorder(stream, mime ? { mimeType: mime } : {});
                    conversionRecorder.ondataavailable = function(e) { if (e.data.size > 0) conversionChunks.push(e.data); };
                    conversionRecorder.onstop = function() {
                        if (conversionInterval) { clearInterval(conversionInterval); conversionInterval = null; }
                        convertedBlob = new Blob(conversionChunks, { type: 'video/webm' });
                        progressBar.style.width = '100%';
                        progressText.textContent = '\u8f6c\u6362\u5b8c\u6210\uff01\u6587\u4ef6: ' + (convertedBlob.size / (1024*1024)).toFixed(2) + ' MB';
                        setTimeout(function() {
                            progressContainer.classList.add('hidden');
                            resultContainer.classList.remove('hidden');
                        }, 800);
                        log('MP4\u8f6c\u6362\u5b8c\u6210, ' + (convertedBlob.size / (1024*1024)).toFixed(2) + ' MB', 'success');
                    };
                    conversionRecorder.start(1000);
                    progressBar.style.width = '15%';
                    progressText.textContent = '\u6b63\u5728\u5f55\u5236...';
                    log('\u5f00\u59cb\u5f55\u5236\u8f6c\u6362...', 'success');
                    var startTime = Date.now();
                    conversionInterval = setInterval(function() {
                        var elapsed = Date.now() - startTime;
                        if (duration > 0) {
                            var pct = Math.min(15 + (elapsed / duration) * 80, 95);
                            progressBar.style.width = pct + '%';
                            progressText.textContent = '\u5f55\u5236\u4e2d... ' + (elapsed/1000).toFixed(0) + '\u79d2 / ' + (duration/1000) + '\u79d2';
                            if (elapsed >= duration) {
                                clearInterval(conversionInterval); conversionInterval = null;
                                if (conversionRecorder.state !== 'inactive') conversionRecorder.stop();
                            }
                        } else {
                            progressBar.style.width = Math.min(15 + (elapsed / 300000) * 80, 95) + '%';
                            progressText.textContent = '\u5f55\u5236\u4e2d... ' + (elapsed/1000).toFixed(0) + '\u79d2\uff08\u5207\u6362\u5230\u64ad\u653e\u6807\u7b7e\u505c\u6b62\uff09';
                        }
                    }, 500);
                } catch(e) {
                    progressText.textContent = '\u5f55\u5236\u5931\u8d25: ' + e.message;
                    log('\u8f6c\u6362\u5f55\u5236\u5931\u8d25: ' + e.message, 'error');
                }
            }

            if (typeof Hls !== 'undefined' && Hls.isSupported()) {
                hls = new Hls({
                    xhrSetup: function(xhr, reqUrl) {
                        var ref = document.getElementById('referer').value.trim();
                        var ua = document.getElementById('user-agent').value.trim();
                        if (ref) xhr.setRequestHeader('Referer', ref);
                        if (ua) xhr.setRequestHeader('User-Agent', ua);
                    }
                });
                hls.loadSource(url);
                hls.attachMedia(video);
                hls.on(Hls.Events.MANIFEST_PARSED, function() {
                    progressBar.style.width = '10%';
                    progressText.textContent = '\u6d41\u5df2\u52a0\u8f7d\uff0c\u51c6\u5907\u5f55\u5236...';
                    video.play().then(function() { setTimeout(beginRec, 1500); }).catch(function(e) {
                        progressText.textContent = '\u64ad\u653e\u5931\u8d25: ' + e.message;
                    });
                });
                hls.on(Hls.Events.ERROR, function(event, data) {
                    if (data.fatal) { progressText.textContent = '\u52a0\u8f7d\u5931\u8d25: ' + data.details; log('\u8f6c\u6362\u52a0\u8f7d\u5931\u8d25: ' + data.details, 'error'); }
                });
            } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
                video.src = url;
                video.addEventListener('loadedmetadata', function() {
                    progressBar.style.width = '10%';
                    progressText.textContent = '\u6d41\u5df2\u52a0\u8f7d...';
                    video.play().then(function() { setTimeout(beginRec, 1500); });
                }, { once: true });
            } else {
                progressText.textContent = '\u6d4f\u89c8\u5668\u4e0d\u652f\u6301HLS';
                log('\u6d4f\u89c8\u5668\u4e0d\u652f\u6301HLS', 'error');
            }
        }

        function downloadConvertedFile() {
            if (!convertedBlob) { alert('\u6ca1\u6709\u53ef\u4e0b\u8f7d\u7684\u6587\u4ef6\u3002\u8bf7\u5148\u5b8c\u6210\u4e00\u6b21\u8f6c\u6362\u3002'); return; }
            var a = document.createElement('a');
            a.href = URL.createObjectURL(convertedBlob);
            a.download = 'converted-m3u8-' + Date.now() + '.webm';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(a.href);
            log('\u8f6c\u6362\u6587\u4ef6\u5df2\u4e0b\u8f7d', 'success');
        }"""
    content = content[:start_idx] + new_converter + content[end_idx:]
    changes += 1
    print('8. startConversion+downloadConvertedFile 重写')
else:
    print('WARN: 未找到转换函数代码块')

# Fix 9: 转换页输入框 Enter 键
old9 = "            console.log('%cM3U8 Player v2.1 - \u529f\u80fd\u5df2\u5b8c\u5168\u4fee\u590d', 'color:#3b82f6; font-size:13px; font-family:monospace');"
new9 = """            document.getElementById('convert-url').addEventListener('keydown', function(e) {
                if (e.key === 'Enter') startConversion();
            });
            console.log('%cM3U8 Player v2.1 - \u529f\u80fd\u5df2\u4fee\u590d', 'color:#3b82f6; font-size:13px; font-family:monospace');"""
if old9 in content:
    content = content.replace(old9, new9)
    changes += 1
    print('9. 转换页Enter键支持')
else:
    print('WARN: 未找到console.log标记')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n共修改 {changes} 处 -> {filepath}')
