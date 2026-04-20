import os

filepath = os.path.join('D:\\桌面\\m3u8player', 'm3u8_to_mp4', 'index.html')
os.makedirs(os.path.dirname(filepath), exist_ok=True)

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# Fix 1: 添加 hls.js CDN（页面完全没有引入）
old1 = '  <!-- Preconnect -->\n  <link rel="preconnect" href="https://cdn.jsdelivr.net">'
new1 = '  <!-- Preconnect -->\n  <link rel="preconnect" href="https://cdn.jsdelivr.net">\n  <script src="https://cdn.jsdelivr.net/npm/hls.js@1.5.7"></script>'
if old1 in content:
    content = content.replace(old1, new1)
    changes += 1
    print('1. 添加 hls.js CDN')
else:
    print('WARN: 未找到 Preconnect 标记')

# Fix 2: 删除 Cloudflare email-decode 脚本（Vercel上404）
old2 = '  <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script>'
new2 = '  <script>'
if old2 in content:
    content = content.replace(old2, new2)
    changes += 1
    print('2. 删除 Cloudflare email-decode 脚本')
else:
    print('WARN: 未找到 Cloudflare 脚本')

# Fix 3: 修复邮箱混淆为明文
old3 = '<p>&copy; 2019-2025 M3U8在线播放器 | 联系邮箱: <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="aa989398989a989d999399eadbdb84c9c5c7">[email&#160;protected]</a></p>'
new3 = '<p>&copy; 2019-2025 M3U8在线播放器 | 联系邮箱: <a href="mailto:2922027393@qq.com">2922027393@qq.com</a></p>'
if old3 in content:
    content = content.replace(old3, new3)
    changes += 1
    print('3. 邮箱混淆 -> 明文')
else:
    print('WARN: 未找到邮箱混淆')

# Fix 4: 添加隐藏 video 元素（录制需要）
old4 = '      <div class="progress-container" id="progressContainer">'
new4 = '      <video id="hiddenVideo" style="display:none" muted playsinline></video>\n      <div class="progress-container" id="progressContainer">'
if old4 in content:
    content = content.replace(old4, new4, 1)
    changes += 1
    print('4. 添加隐藏 video 元素')
else:
    print('WARN: 未找到 progressContainer')

# Fix 5: 重写整个 script 部分（核心修复：假的转真正的录制转换）
script_marker = "    function showStatus(message, type) {"
script_start = content.find(script_marker)
# 找到 </script> 结尾
script_end_marker = "    }\n  </script>"
script_end = content.find(script_end_marker)

if script_start != -1 and script_end != -1:
    script_end += len(script_end_marker)
    new_script = """    var convHls = null;
    var convRecorder = null;
    var convChunks = [];
    var convInterval = null;

    function showStatus(message, type) {
      var status = document.getElementById('status');
      status.textContent = message;
      status.className = 'status ' + type;
    }

    function updateProgress(percent, text) {
      var container = document.getElementById('progressContainer');
      var fill = document.getElementById('progressFill');
      var textEl = document.getElementById('progressText');
      container.classList.add('active');
      fill.style.width = percent + '%';
      textEl.textContent = text;
    }

    function startConversion() {
      var url = document.getElementById('urlInput').value.trim();
      var btn = document.getElementById('convertBtn');
      if (!url) { showStatus('\u8bf7\u8f93\u5165M3U8\u89c6\u9891\u94fe\u63a5', 'error'); return; }

      btn.disabled = true;
      showStatus('\u6b63\u5728\u521d\u59cb\u5316...', 'info');
      updateProgress(5, '\u6b63\u5728\u52a0\u8f7d\u89c6\u9891\u6d41...');

      if (convInterval) { clearInterval(convInterval); convInterval = null; }
      if (convRecorder && convRecorder.state !== 'inactive') { convRecorder.stop(); }
      if (convHls) { convHls.destroy(); convHls = null; }
      convChunks = [];

      var video = document.getElementById('hiddenVideo');
      var started = false;

      function beginRec() {
        if (started) return;
        started = true;
        try {
          var mime = 'video/webm;codecs=vp9';
          if (!MediaRecorder.isTypeSupported(mime)) mime = 'video/webm;codecs=vp8';
          if (!MediaRecorder.isTypeSupported(mime)) mime = 'video/webm';
          if (!MediaRecorder.isTypeSupported(mime)) mime = '';
          var stream = video.captureStream ? video.captureStream() : (video.mozCaptureStream ? video.mozCaptureStream() : null);
          if (!stream) { showStatus('\u6d4f\u89c8\u5668\u4e0d\u652f\u6301\u6d41\u6355\u83b7', 'error'); btn.disabled = false; return; }
          convRecorder = new MediaRecorder(stream, mime ? { mimeType: mime } : {});
          convRecorder.ondataavailable = function(e) { if (e.data.size > 0) convChunks.push(e.data); };
          convRecorder.onstop = function() {
            if (convInterval) { clearInterval(convInterval); convInterval = null; }
            var blob = new Blob(convChunks, { type: 'video/webm' });
            updateProgress(100, '\u8f6c\u6362\u5b8c\u6210\uff01');
            showStatus('\u8f6c\u6362\u5b8c\u6210\uff01\u6587\u4ef6\u5927\u5c0f: ' + (blob.size / (1024*1024)).toFixed(2) + ' MB', 'success');
            var fname = document.getElementById('filename').value.trim() || ('converted-' + Date.now() + '.webm');
            var a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = fname;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(a.href);
            btn.disabled = false;
          };
          convRecorder.start(1000);
          updateProgress(15, '\u6b63\u5728\u5f55\u5236\u89c6\u9891...');
          showStatus('\u6b63\u5728\u5f55\u5236\uff0c\u8bf7\u7b49\u5f85\u540e\u70b9\u51fb\u201c\u505c\u6b62\u5e76\u4e0b\u8f7d\u201d', 'info');
          btn.textContent = '\u505c\u6b62\u5e76\u4e0b\u8f7d';
          btn.disabled = false;
          btn.onclick = function() { stopConversion(); };
          var startTime = Date.now();
          convInterval = setInterval(function() {
            var elapsed = ((Date.now() - startTime) / 1000).toFixed(0);
            var pct = Math.min(15 + (elapsed / 300) * 80, 95);
            updateProgress(pct, '\u5f55\u5236\u4e2d... ' + elapsed + '\u79d2');
          }, 500);
        } catch(e) {
          showStatus('\u5f55\u5236\u5931\u8d25: ' + e.message, 'error');
          btn.disabled = false;
        }
      }

      if (typeof Hls !== 'undefined' && Hls.isSupported()) {
        convHls = new Hls();
        convHls.loadSource(url);
        convHls.attachMedia(video);
        convHls.on(Hls.Events.MANIFEST_PARSED, function() {
          updateProgress(10, '\u6d41\u5df2\u52a0\u8f7d\uff0c\u51c6\u5907\u5f55\u5236...');
          video.play().then(function() { setTimeout(beginRec, 1500); }).catch(function(e) {
            showStatus('\u64ad\u653e\u5931\u8d25: ' + e.message, 'error');
            btn.disabled = false;
          });
        });
        convHls.on(Hls.Events.ERROR, function(event, data) {
          if (data.fatal) {
            showStatus('\u52a0\u8f7d\u5931\u8d25: ' + data.details, 'error');
            btn.disabled = false;
          }
        });
      } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
        video.src = url;
        video.addEventListener('loadedmetadata', function() {
          updateProgress(10, '\u6d41\u5df2\u52a0\u8f7d...');
          video.play().then(function() { setTimeout(beginRec, 1500); });
        }, { once: true });
      } else {
        showStatus('\u6d4f\u89c8\u5668\u4e0d\u652f\u6301HLS\u64ad\u653e', 'error');
        btn.disabled = false;
      }
    }

    function stopConversion() {
      if (convRecorder && convRecorder.state !== 'inactive') { convRecorder.stop(); }
      if (convInterval) { clearInterval(convInterval); convInterval = null; }
      var btn = document.getElementById('convertBtn');
      btn.textContent = '\u5f00\u59cb\u8f6c\u6362';
      btn.onclick = function() { startConversion(); };
      showStatus('\u6b63\u5728\u751f\u6210\u6587\u4ef6...', 'info');
    }

    document.getElementById('urlInput').addEventListener('keydown', function(e) {
      if (e.key === 'Enter') startConversion();
    });
  </script>"""
    content = content[:script_start] + new_script + content[script_end:]
    changes += 1
    print('5. 重写 startConversion 为真正的 hls.js + MediaRecorder 录制')
else:
    print('WARN: 未找到 script 区域')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n共修改 {changes} 处 -> {filepath}')
