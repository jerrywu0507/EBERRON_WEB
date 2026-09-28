# Restart the Eberron guide: stop whatever listens on 8509, then start start_streamlit.ps1 hidden.
$pids = Get-NetTCPConnection -State Listen -LocalPort 8509 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess -Unique
foreach ($p in $pids) { try { Stop-Process -Id $p -Force -ErrorAction Stop } catch {} }
Start-Sleep -Milliseconds 800
Start-Process powershell -WindowStyle Hidden -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSScriptRoot\start_streamlit.ps1`""
