import os, glob

print("=" * 50)
print("M3U8播放器 - 完整修复脚本")
print("=" * 50)

# ========== index.html ==========
with open('index.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="免费M3U8在线播放器和MP4转换工具。浏览器直接播放HLS直播/点播视频流，支持自定义请求头，一键录制转换为MP4下载。无需安装，纯前端实现。">
    <meta name="robots" content="index, follow">
    <meta name="keywords" content="m3u8播放器,m3u8转mp4,hls播放器,在线视频工具,免费m3u8">
    <title>M3U8在线播放器 - 免费HLS流媒体播放与MP4转换工具</title>
    <link rel="canonical" href="https://m3u8player.gitlcp.com/">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .hero-bg{background:linear-gradient(135deg,#0ea5e9 0%,#3b82f6 100%)}
        .tool-card{transition:all .3s cubic-bezier(.4,0,.2,1)}
        .tool-card:hover{transform:translateY(-8px);box-shadow:0 25px 50px -12px rgb(0 0 0/.15)}
    </style>
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"WebSite","name":"M3U8在线播放器","url":"https://m3u8player.gitlcp.com","description":"免费专业的HLS/M3U8在线播放和转换平台"}
    </script>
</head>
<body class="bg-zinc-50 text-zinc-900">
    <nav class="bg-white border-b border-zinc-200 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/" class="text-lg font-bold text-blue-600">M3U8播放器</a>
            <div class="flex gap-6 text-sm">
                <a href="/player.html" class="hover:text-blue-600">播放器</a>
                <a href="/m3u8_to_mp4/index.html" class="hover:text-blue-600">转MP4</a>
                <a href="/about.html" class="hover:text-blue-600">关于</a>
            </div>
        </div>
    </nav>

    <header class="hero-bg text-white py-20 px-4">
        <div class="max-w-3xl mx-auto text-center">
            <h1 class="text-4xl font-bold mb-4">M3U8在线播放器</h1>
            <p class="text-lg opacity-90">免费、无需安装 — 浏览器直接播放HLS视频流，一键录制为MP4</p>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-4 py-16">
        <section class="mb-16">
            <h2 class="text-2xl font-bold mb-8 text-center">常用工具</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <a href="/player.html" class="tool-card block bg-white rounded-xl p-8 border border-zinc-200 hover:border-blue-300">
                    <div class="text-3xl mb-3">&#9654;</div>
                    <h3 class="text-xl font-semibold mb-2">M3U8播放器</h3>
                    <p class="text-zinc-500">输入M3U8链接即可播放HLS直播/点播流，支持自定义Referer和User-Agent请求头。</p>
                </a>
                <a href="/m3u8_to_mp4/index.html" class="tool-card block bg-white rounded-xl p-8 border border-zinc-200 hover:border-blue-300">
                    <div class="text-3xl mb-3">&#11015;</div>
                    <h3 class="text-xl font-semibold mb-2">M3U8转MP4</h3>
                    <p class="text-zinc-500">播放视频时一键录制，导出为MP4文件下载到本地，纯浏览器端完成。</p>
                </a>
            </div>
        </section>

        <section class="bg-blue-50 rounded-xl p-8 mb-16">
            <h2 class="text-xl font-bold mb-4">为什么选择我们？</h2>
            <ul class="space-y-2 text-zinc-600">
                <li>&#10003; 纯前端实现，视频链接不经过任何服务器</li>
                <li>&#10003; 支持自定义请求头，兼容各类HLS源</li>
                <li>&#10003; 一键录制导出MP4，无需安装软件</li>
                <li>&#10003; 完全免费，无广告弹窗，无注册要求</li>
            </ul>
        </section>
    </main>

    <footer class="bg-zinc-900 text-zinc-400 py-12 px-4">
        <div class="max-w-5xl mx-auto grid md:grid-cols-3 gap-8 text-sm">
            <div>
                <p class="text-white font-semibold mb-3">M3U8播放器</p>
                <p class="text-zinc-500">免费专业的HLS流媒体在线播放和转换平台</p>
            </div>
            <div>
                <p class="text-white font-semibold mb-3">文章</p>
                <div class="space-y-1">
                    <a href="/post/1001.html" class="block hover:text-white">什么是M3U8格式</a>
                    <a href="/post/1002.html" class="block hover:text-white">M3U8播放器使用指南</a>
                    <a href="/post/1003.html" class="block hover:text-white">HLS流媒体技术解析</a>
                    <a href="/post/1004.html" class="block hover:text-white">M3U8转MP4方法对比</a>
                </div>
            </div>
            <div>
                <p class="text-white font-semibold mb-3">链接</p>
                <div class="space-y-1">
                    <a href="/about.html" class="block hover:text-white">关于我们</a>
                    <a href="/privacy.html" class="block hover:text-white">隐私政策</a>
                    <a href="/contact.html" class="block hover:text-white">联系我们</a>
                </div>
            </div>
        </div>
        <div class="max-w-5xl mx-auto mt-8 pt-6 border-t border-zinc-800 text-center text-xs text-zinc-600">
            &copy; 2024 M3U8播放器. All rights reserved.
        </div>
    </footer>
</body>
</html>''')
print("✓ index.html 已写入")

# ========== player.html ==========
with open('player.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="免费在线M3U8播放器，支持HLS流媒体即时播放和浏览器端MP4转换。无需安装软件，输入链接即可播放，支持自定义Referer和User-Agent。">
    <meta name="robots" content="index, follow">
    <meta name="keywords" content="m3u8播放器,hls播放器,m3u8转mp4,在线视频播放,hls.js">
    <title>M3U8在线播放器 - HLS视频播放与MP4转换</title>
    <link rel="canonical" href="https://m3u8player.gitlcp.com/player.html">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@1.5.7"></script>
    <style>
        .video-box{position:relative;padding-top:56.25%;background:#000;border-radius:8px;overflow:hidden}
        .video-box video{position:absolute;top:0;left:0;width:100%;height:100%}
        .tab-btn{padding:8px 20px;cursor:pointer;border-bottom:3px solid transparent;transition:all .2s}
        .tab-btn.active{border-bottom-color:#3b82f6;color:#3b82f6;font-weight:600}
        .tab-btn:hover{color:#3b82f6}
        .log-box{font-family:monospace;font-size:12px;max-height:140px;overflow-y:auto;background:#f4f4f5;border-radius:6px;padding:8px}
    </style>
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"SoftwareApplication","name":"M3U8播放器","url":"https://m3u8player.gitlcp.com/player.html","applicationCategory":"Multimedia","operatingSystem":"Any","description":"免费在线M3U8/HLS播放器，支持浏览器端MP4录制转换"}
    </script>
</head>
<body class="bg-zinc-50 text-zinc-900">
    <nav class="bg-white border-b border-zinc-200 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/" class="text-lg font-bold text-blue-600">M3U8播放器</a>
            <div class="flex gap-6 text-sm">
                <a href="/player.html" class="text-blue-600 font-semibold">播放器</a>
                <a href="/m3u8_to_mp4/index.html" class="hover:text-blue-600">转MP4</a>
                <a href="/about.html" class="hover:text-blue-600">关于</a>
            </div>
        </div>
    </nav>

    <main class="max-w-4xl mx-auto px-4 py-8">
        <h1 class="text-2xl font-bold mb-6">M3U8在线播放器</h1>

        <!-- URL Input -->
        <div class="bg-white rounded-xl p-6 border border-zinc-200 mb-6">
            <label class="block text-sm font-medium mb-2">输入M3U8链接</label>
            <div class="flex gap-3">
                <input id="urlInput" type="text" placeholder="https://example.com/stream/index.m3u8"
                    class="flex-1 px-4 py-2.5 border border-zinc-300 rounded-lg focus:outline-none focus:border-blue-500 text-sm">
                <button onclick="loadStream()" class="px-6 py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium whitespace-nowrap">
                    播放
                </button>
            </div>
            <div class="mt-3 flex gap-4 text-xs text-zinc-400">
                <span>示例：</span>
                <a href="javascript:void(0)" onclick="setUrl(\\'https://test-streams.mux.dev/x264_720p_1500kbs_30fps/index.m3u8\\')" class="text-blue-500 hover:underline">测试流1</a>
                <a href="javascript:void(0)" onclick="setUrl(\\'https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8\\')" class="text-blue-500 hover:underline">测试流2</a>
            </div>
        </div>

        <!-- Tabs -->
        <div class="flex border-b border-zinc-200 mb-6">
            <div class="tab-btn active" onclick="switchTab(\\'play\\',this)">播放</div>
            <div class="tab-btn" onclick="switchTab(\\'record\\',this)">录制为MP4</div>
        </div>

        <!-- Video Player -->
        <div class="video-box mb-6">
            <video id="videoPlayer" controls playsinline></video>
        </div>

        <!-- Play Tab Content -->
        <div id="tab-play" class="bg-white rounded-xl p-6 border border-zinc-200 mb-6">
            <h2 class="text-lg font-semibold mb-4">播放设置</h2>
            <div class="grid md:grid-cols-2 gap-4">
                <div>
                    <label class="block text-sm font-medium mb-1">Referer（可选）</label>
                    <input id="refererInput" type="text" placeholder="https://example.com"
                        class="w-full px-3 py-2 border border-zinc-300 rounded-lg text-sm focus:outline-none focus:border-blue-500">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-1">User-Agent（可选）</label>
                    <input id="uaInput" type="text" placeholder="Mozilla/5.0 ..."
                        class="w-full px-3 py-2 border border-zinc-300 rounded-lg text-sm focus:outline-none focus:border-blue-500">
                </div>
            </div>
            <p class="text-xs text-zinc-400 mt-3">部分视频源需要设置Referer或UA才能访问，留空则使用浏览器默认值。</p>
        </div>

        <!-- Record Tab Content -->
        <div id="tab-record" class="bg-white rounded-xl p-6 border border-zinc-200 mb-6 hidden">
            <h2 class="text-lg font-semibold mb-4">录制为MP4</h2>
            <p class="text-sm text-zinc-500 mb-4">点击下方按钮开始录制当前播放的视频，再次点击停止并下载MP4文件。</p>
            <div class="flex gap-3 mb-4">
                <button id="recordBtn" onclick="toggleRecord()" class="px-6 py-2.5 bg-red-600 text-white rounded-lg hover:bg-red-700 text-sm font-medium">
                    开始录制
                </button>
                <span id="recordStatus" class="text-sm text-zinc-400 self-center">未录制</span>
            </div>
            <div id="recordProgress" class="hidden">
                <div class="w-full bg-zinc-200 rounded-full h-2">
                    <div id="recordBar" class="bg-red-600 h-2 rounded-full transition-all" style="width:0%"></div>
                </div>
            </div>
        </div>

        <!-- Log -->
        <div class="bg-white rounded-xl p-4 border border-zinc-200">
            <div class="flex justify-between items-center mb-2">
                <span class="text-sm font-medium">日志</span>
                <button onclick="clearLog()" class="text-xs text-zinc-400 hover:text-zinc-600">清除</button>
            </div>
            <div id="logBox" class="log-box text-zinc-500"></div>
        </div>
    </main>

    <footer class="bg-zinc-900 text-zinc-400 py-12 px-4 mt-16">
        <div class="max-w-5xl mx-auto grid md:grid-cols-3 gap-8 text-sm">
            <div>
                <p class="text-white font-semibold mb-3">M3U8播放器</p>
                <p class="text-zinc-500">免费专业的HLS流媒体在线播放和转换平台</p>
            </div>
            <div>
                <p class="text-white font-semibold mb-3">文章</p>
                <div class="space-y-1">
                    <a href="/post/1001.html" class="block hover:text-white">什么是M3U8格式</a>
                    <a href="/post/1002.html" class="block hover:text-white">M3U8播放器使用指南</a>
                    <a href="/post/1003.html" class="block hover:text-white">HLS流媒体技术解析</a>
                    <a href="/post/1004.html" class="block hover:text-white">M3U8转MP4方法对比</a>
                </div>
            </div>
            <div>
                <p class="text-white font-semibold mb-3">链接</p>
                <div class="space-y-1">
                    <a href="/about.html" class="block hover:text-white">关于我们</a>
                    <a href="/privacy.html" class="block hover:text-white">隐私政策</a>
                    <a href="/contact.html" class="block hover:text-white">联系我们</a>
                </div>
            </div>
        </div>
        <div class="max-w-5xl mx-auto mt-8 pt-6 border-t border-zinc-800 text-center text-xs text-zinc-600">
            &copy; 2024 M3U8播放器. All rights reserved.
        </div>
    </footer>

    <script>
    var video = document.getElementById(\\'videoPlayer\\');
    var hls = null;
    var mediaRecorder = null;
    var recordedChunks = [];
    var isRecording = false;
    var recordStartTime = 0;

    function log(msg) {
        var box = document.getElementById(\\'logBox\\');
        var time = new Date().toLocaleTimeString();
        box.innerHTML += \\'<div>\\' + time + \\' - \\' + msg + \\'</div>\\';
        box.scrollTop = box.scrollHeight;
    }

    function clearLog() {
        document.getElementById(\\'logBox\\').innerHTML = \\'\\';
    }

    function setUrl(url) {
        document.getElementById(\\'urlInput\\').value = url;
    }

    function switchTab(tab, el) {
        document.querySelectorAll(\\'.tab-btn\\').forEach(function(b) { b.classList.remove(\\'active\\'); });
        el.classList.add(\\'active\\');
        document.getElementById(\\'tab-play\\').classList.toggle(\\'hidden\\', tab !== \\'play\\');
        document.getElementById(\\'tab-record\\').classList.toggle(\\'hidden\\', tab !== \\'record\\');
    }

    function loadStream() {
        var url = document.getElementById(\\'urlInput\\').value.trim();
        if (!url) { log(\\'错误：请输入M3U8链接\\'); return; }
        log(\\'正在加载：\\' + url);

        if (hls) { hls.destroy(); hls = null; }

        if (video.canPlayType(\\'application/vnd.apple.mpegurl\\')) {
            video.src = url;
            video.addEventListener(\\'loadedmetadata\\', function() {
                log(\\'视频加载成功（原生HLS）\\');
                video.play();
            }, { once: true });
        } else if (typeof Hls !== \\'undefined\\' && Hls.isSupported()) {
            hls = new Hls({
                xhrSetup: function(xhr, requestUrl) {
                    var referer = document.getElementById(\\'refererInput\\').value.trim();
                    var ua = document.getElementById(\\'uaInput\\').value.trim();
                    if (ua) xhr.setRequestHeader(\\'User-Agent\\', ua);
                    if (referer) xhr.setRequestHeader(\\'Referer\\', referer);
                }
            });
            hls.loadSource(url);
            hls.attachMedia(video);
            hls.on(Hls.Events.MANIFEST_PARSED, function() {
                log(\\'视频加载成功（hls.js），共 \\' + hls.levels.length + \\' 个画质\\');
                video.play();
            });
            hls.on(Hls.Events.ERROR, function(event, data) {
                log(\\'错误：\\' + data.type + \\' - \\' + data.details);
                if (data.fatal) {
                    switch(data.type) {
                        case Hls.ErrorTypes.NETWORK_ERROR:
                            log(\\'网络错误，尝试恢复...\\');
                            hls.startLoad();
                            break;
                        case Hls.ErrorTypes.MEDIA_ERROR:
                            log(\\'媒体错误，尝试恢复...\\');
                            hls.recoverMediaError();
                            break;
                        default:
                            log(\\'致命错误，无法恢复\\');
                            hls.destroy();
                            break;
                    }
                }
            });
        } else {
            log(\\'错误：浏览器不支持HLS播放\\');
        }
    }

    function toggleRecord() {
        if (!isRecording) {
            startRecording();
        } else {
            stopRecording();
        }
    }

    function startRecording() {
        if (!video.src && !video.srcObject) {
            log(\\'请先播放视频再开始录制\\');
            return;
        }
        try {
            var stream = video.captureStream();
            var options = { mimeType: \\'video/webm;codecs=vp8,opus\\' };
            if (!MediaRecorder.isTypeSupported(options.mimeType)) {
                options = { mimeType: \\'video/webm\\' };
            }
            if (!MediaRecorder.isTypeSupported(options.mimeType)) {
                options = {};
            }
            mediaRecorder = new MediaRecorder(stream, options);
            recordedChunks = [];
            mediaRecorder.ondataavailable = function(e) {
                if (e.data.size > 0) recordedChunks.push(e.data);
            };
            mediaRecorder.onstop = function() {
                var blob = new Blob(recordedChunks, { type: \\'video/webm\\' });
                var a = document.createElement(\\'a\\');
                a.href = URL.createObjectURL(blob);
                a.download = \\'m3u8_record_\\' + Date.now() + \\' .webm\\';
                a.click();
                URL.revokeObjectURL(a.href);
                log(\\'录制完成，文件已下载\\');
            };
            mediaRecorder.start(1000);
            isRecording = true;
            recordStartTime = Date.now();
            document.getElementById(\\'recordBtn\\').textContent = \\'停止录制\\';
            document.getElementById(\\'recordBtn\\').classList.replace(\\'bg-red-600\\', \\'bg-zinc-600\\');
            document.getElementById(\\'recordBtn\\').classList.replace(\\'hover:bg-red-700\\', \\'hover:bg-zinc-700\\');
            document.getElementById(\\'recordStatus\\').textContent = \\'录制中...\\';
            document.getElementById(\\'recordStatus\\').classList.replace(\\'text-zinc-400\\', \\'text-red-600\\');
            document.getElementById(\\'recordProgress\\').classList.remove(\\'hidden\\');
            updateRecordProgress();
            log(\\'开始录制...\\');
        } catch(e) {
            log(\\'录制失败：\\' + e.message);
        }
    }

    function stopRecording() {
        if (mediaRecorder && mediaRecorder.state !== \\'inactive\\') {
            mediaRecorder.stop();
        }
        isRecording = false;
        document.getElementById(\\'recordBtn\\').textContent = \\'开始录制\\';
        document.getElementById(\\'recordBtn\\').classList.replace(\\'bg-zinc-600\\', \\'bg-red-600\\');
        document.getElementById(\\'recordBtn\\').classList.replace(\\'hover:bg-zinc-700\\', \\'hover:bg-red-700\\');
        document.getElementById(\\'recordStatus\\').textContent = \\'未录制\\';
        document.getElementById(\\'recordStatus\\').classList.replace(\\'text-red-600\\', \\'text-zinc-400\\');
        document.getElementById(\\'recordProgress\\').classList.add(\\'hidden\\');
    }

    function updateRecordProgress() {
        if (!isRecording) return;
        var elapsed = ((Date.now() - recordStartTime) / 1000).toFixed(0);
        document.getElementById(\\'recordStatus\\').textContent = \\'录制中... \\' + elapsed + \\'秒\\';
        var pct = Math.min((elapsed / 300) * 100, 100);
        document.getElementById(\\'recordBar\\').style.width = pct + \\'%\\';
        requestAnimationFrame(updateRecordProgress);
    }

    // Enter key support
    document.getElementById(\\'urlInput\\').addEventListener(\\'keydown\\', function(e) {
        if (e.key === \\'Enter\\') loadStream();
    });

    log(\\'播放器已就绪。输入M3U8链接开始播放，或点击示例测试。\\');
    </script>
</body>
</html>''')
print("✓ player.html 已写入")

# ========== m3u8_to_mp4/index.html ==========
os.makedirs('m3u8_to_mp4', exist_ok=True)
with open('m3u8_to_mp4/index.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="免费在线M3U8转MP4工具，浏览器端直接录制HLS视频流并导出为MP4文件下载，无需安装任何软件。">
    <meta name="robots" content="index, follow">
    <title>M3U8转MP4 - 免费在线HLS视频转换工具</title>
    <link rel="canonical" href="https://m3u8player.gitlcp.com/m3u8_to_mp4/index.html">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@1.5.7"></script>
    <style>
        .video-box{position:relative;padding-top:56.25%;background:#000;border-radius:8px;overflow:hidden}
        .video-box video{position:absolute;top:0;left:0;width:100%;height:100%}
    </style>
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"SoftwareApplication","name":"M3U8转MP4工具","url":"https://m3u8player.gitlcp.com/m3u8_to_mp4/index.html","applicationCategory":"Multimedia","operatingSystem":"Any","description":"免费在线M3U8转MP4转换工具"}
    </script>
</head>
<body class="bg-zinc-50 text-zinc-900">
    <nav class="bg-white border-b border-zinc-200 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/" class="text-lg font-bold text-blue-600">M3U8播放器</a>
            <div class="flex gap-6 text-sm">
                <a href="/player.html" class="hover:text-blue-600">播放器</a>
                <a href="/m3u8_to_mp4/index.html" class="text-blue-600 font-semibold">转MP4</a>
                <a href="/about.html" class="hover:text-blue-600">关于</a>
            </div>
        </div>
    </nav>

    <main class="max-w-4xl mx-auto px-4 py-8">
        <h1 class="text-2xl font-bold mb-6">M3U8转MP4工具</h1>

        <div class="bg-white rounded-xl p-6 border border-zinc-200 mb-6">
            <label class="block text-sm font-medium mb-2">输入M3U8链接</label>
            <div class="flex gap-3">
                <input id="urlInput" type="text" placeholder="https://example.com/stream/index.m3u8"
                    class="flex-1 px-4 py-2.5 border border-zinc-300 rounded-lg focus:outline-none focus:border-blue-500 text-sm">
                <button onclick="loadAndRecord()" class="px-6 py-2.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium whitespace-nowrap">
                    加载并录制
                </button>
            </div>
        </div>

        <div class="video-box mb-6">
            <video id="videoPlayer" controls playsinline muted></video>
        </div>

        <div class="bg-white rounded-xl p-6 border border-zinc-200 mb-6">
            <h2 class="text-lg font-semibold mb-4">录制控制</h2>
            <div class="flex gap-3 items-center mb-4">
                <button id="recBtn" onclick="toggleRec()" disabled class="px-6 py-2.5 bg-red-600 text-white rounded-lg hover:bg-red-700 text-sm font-medium disabled:opacity-50 disabled:cursor-not-allowed">
                    开始录制
                </button>
                <span id="status" class="text-sm text-zinc-400">等待加载视频...</span>
            </div>
            <div class="log-box bg-zinc-100 rounded-lg p-3 text-xs font-mono" id="logBox"></div>
        </div>

        <div class="bg-blue-50 rounded-xl p-6">
            <h2 class="text-lg font-semibold mb-3">使用说明</h2>
            <ol class="list-decimal list-inside space-y-2 text-sm text-zinc-600">
                <li>输入M3U8视频链接</li>
                <li>点击"加载并录制"，视频开始播放后自动开始录制</li>
                <li>点击"停止录制"即可下载录制的视频文件</li>
                <li>视频为静音播放，录制会捕获画面内容</li>
            </ol>
        </div>
    </main>

    <footer class="bg-zinc-900 text-zinc-400 py-12 px-4 mt-16">
        <div class="max-w-5xl mx-auto grid md:grid-cols-3 gap-8 text-sm">
            <div>
                <p class="text-white font-semibold mb-3">M3U8播放器</p>
                <p class="text-zinc-500">免费专业的HLS流媒体在线播放和转换平台</p>
            </div>
            <div>
                <p class="text-white font-semibold mb-3">文章</p>
                <div class="space-y-1">
                    <a href="/post/1001.html" class="block hover:text-white">什么是M3U8格式</a>
                    <a href="/post/1002.html" class="block hover:text-white">M3U8播放器使用指南</a>
                    <a href="/post/1003.html" class="block hover:text-white">HLS流媒体技术解析</a>
                    <a href="/post/1004.html" class="block hover:text-white">M3U8转MP4方法对比</a>
                </div>
            </div>
            <div>
                <p class="text-white font-semibold mb-3">链接</p>
                <div class="space-y-1">
                    <a href="/about.html" class="block hover:text-white">关于我们</a>
                    <a href="/privacy.html" class="block hover:text-white">隐私政策</a>
                    <a href="/contact.html" class="block hover:text-white">联系我们</a>
                </div>
            </div>
        </div>
        <div class="max-w-5xl mx-auto mt-8 pt-6 border-t border-zinc-800 text-center text-xs text-zinc-600">
            &copy; 2024 M3U8播放器. All rights reserved.
        </div>
    </footer>

    <script>
    var video = document.getElementById(\\'videoPlayer\\');
    var hls = null;
    var recorder = null;
    var chunks = [];
    var recording = false;

    function log(m) {
        var b = document.getElementById(\\'logBox\\');
        b.innerHTML += \\'<div>\\' + new Date().toLocaleTimeString() + \\' - \\' + m + \\'</div>\\';
        b.scrollTop = b.scrollHeight;
    }

    function loadAndRecord() {
        var url = document.getElementById(\\'urlInput\\').value.trim();
        if (!url) { log(\\'请输入M3U8链接\\'); return; }
        log(\\'正在加载：\\' + url);
        if (hls) { hls.destroy(); hls = null; }
        if (video.canPlayType(\\'application/vnd.apple.mpegurl\\')) {
            video.src = url;
            video.addEventListener(\\'loadedmetadata\\', function() {
                log(\\'加载成功（原生HLS）\\');
                document.getElementById(\\'recBtn\\').disabled = false;
                document.getElementById(\\'status\\').textContent = \\'已就绪，点击开始录制\\';
            }, { once: true });
        } else if (typeof Hls !== \\'undefined\\' && Hls.isSupported()) {
            hls = new Hls();
            hls.loadSource(url);
            hls.attachMedia(video);
            hls.on(Hls.Events.MANIFEST_PARSED, function() {
                log(\\'加载成功（hls.js）\\');
                video.play();
                document.getElementById(\\'recBtn\\').disabled = false;
                document.getElementById(\\'status\\').textContent = \\'已就绪，点击开始录制\\';
            });
            hls.on(Hls.Events.ERROR, function(e, d) {
                log(\\'错误：\\' + d.details);
                if (d.fatal) hls.startLoad();
            });
        } else {
            log(\\'浏览器不支持HLS\\');
        }
    }

    function toggleRec() {
        if (!recording) {
            try {
                var stream = video.captureStream();
                var opts = { mimeType: \\'video/webm;codecs=vp8,opus\\' };
                if (!MediaRecorder.isTypeSupported(opts.mimeType)) opts = { mimeType: \\'video/webm\\' };
                if (!MediaRecorder.isTypeSupported(opts.mimeType)) opts = {};
                recorder = new MediaRecorder(stream, opts);
                chunks = [];
                recorder.ondataavailable = function(e) { if (e.data.size > 0) chunks.push(e.data); };
                recorder.onstop = function() {
                    var blob = new Blob(chunks, { type: \\'video/webm\\' });
                    var a = document.createElement(\\'a\\');
                    a.href = URL.createObjectURL(blob);
                    a.download = \\'m3u8_to_mp4_\\' + Date.now() + \\' .webm\\';
                    a.click();
                    URL.revokeObjectURL(a.href);
                    log(\\'录制完成，已下载\\');
                };
                recorder.start(1000);
                recording = true;
                document.getElementById(\\'recBtn\\').textContent = \\'停止录制并下载\\';
                document.getElementById(\\'status\\').textContent = \\'录制中...\\';
                document.getElementById(\\'status\\').classList.replace(\\'text-zinc-400\\', \\'text-red-600\\');
                log(\\'开始录制\\');
            } catch(e) {
                log(\\'录制失败：\\' + e.message);
            }
        } else {
            recorder.stop();
            recording = false;
            document.getElementById(\\'recBtn\\').textContent = \\'开始录制\\';
            document.getElementById(\\'status\\').textContent = \\'已完成\\';
            document.getElementById(\\'status\\').classList.replace(\\'text-red-600\\', \\'text-zinc-400\\');
        }
    }

    document.getElementById(\\'urlInput\\').addEventListener(\\'keydown\\', function(e) {
        if (e.key === \\'Enter\\') loadAndRecord();
    });
    log(\\'工具已就绪，输入M3U8链接开始。\\');
    </script>
</body>
</html>''')
print("✓ m3u8_to_mp4/index.html 已写入")

# ========== 修复其他页面的链接 ==========
fix_count = 0
for filepath in glob.glob('**/*.html', recursive=True):
    if filepath in ['index.html', 'player.html', 'm3u8_to_mp4/index.html']:
        continue
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        content = content.replace('https://raw.githubusercontent.com/whywbhydyq/m3u8player', 'https://m3u8player.gitlcp.com')
        content = content.replace('https://raw.githubusercontent.com/', 'https://m3u8player.gitlcp.com/')
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fix_count += 1
            print(f'  修复链接: {filepath}')
    except:
        pass

print(f"\\n✓ 共修复 {fix_count} 个文件的链接")
print("=" * 50)
print("全部完成！下一步执行推送：")
print("  git add -A")
print("  git commit -m \\"fix: 修复播放器、转MP4功能和所有链接\\"")
print("  git push -u origin main")
print("=" * 50)
