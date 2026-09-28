Set-Location -Path $PSScriptRoot
& "$PSScriptRoot\.venv\Scripts\python.exe" -m streamlit run "$PSScriptRoot\app.py" --server.address 127.0.0.1 --server.port 8509 --server.headless true
