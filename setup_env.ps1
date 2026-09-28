# Creates .venv (Python 3.12) next to this script and installs the pinned dependencies.
# Run once on a new machine; never copy an old .venv over (it contains absolute paths).
$ErrorActionPreference = "Stop"
$venv = Join-Path $PSScriptRoot ".venv"
if (-not (Test-Path $venv)) {
    if (Get-Command py -ErrorAction SilentlyContinue) { py -3.12 -m venv $venv } else { python -m venv $venv }
}
$py = Join-Path $venv "Scripts\python.exe"
& $py -m pip install --upgrade pip
& $py -m pip install -r (Join-Path $PSScriptRoot "requirements.txt")
& $py -c "import streamlit; print('streamlit', streamlit.__version__, 'ready')"
