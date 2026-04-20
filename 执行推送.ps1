# M3U8播放器 - 执行推送
# 在PowerShell中运行此脚本

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  M3U8播放器 - GitHub推送脚本" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# 检查Python
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command python3 -ErrorAction SilentlyContinue
}

if (-not $python) {
    Write-Host "错误: 未找到Python，请先安装Python" -ForegroundColor Red
    exit 1
}

Write-Host "Python路径: $($python.Source)" -ForegroundColor Green
Write-Host ""

# 执行Python脚本
& $python.Source "push_all.py"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "脚本执行完成" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan