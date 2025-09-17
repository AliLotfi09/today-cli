# Today CLI 📅⏰

<div align="center">

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

**A beautiful command-line tool to display current time and date in both Persian (Jalali) and Gregorian calendars**

</div>

---

## Features ✨

- Beautiful time display with colored tables
- Persian (Jalali) calendar support
- Gregorian calendar display  
- Rich colors and formatting
- Fast and lightweight

---

## Quick Start 🚀

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/today-cli.git
cd today-cli
```

### 2. Install dependencies
```bash
pip install rich jdatetime

```

### 3. Run directly
```bash
python today.py now    # Show current time
python today.py s      # Show Persian date  
python today.py m      # Show Gregorian date
```

## Windows: One-Line PATH Setup (No manual steps) ⚡

This PowerShell one-liner will:

Detect your Python version

Detect your user Scripts folder

Add it to the User PATH if not already there

Show confirmation
```bash
$pyVer=(python -c "import sys;print('Python'+str(sys.version_info.major)+str(sys.version_info.minor))"); $scripts=Join-Path $env:APPDATA "Python\$pyVer\Scripts"; Write-Host "🔹 Python version: $pyVer"; Write-Host "🔹 Scripts path: $scripts"; if (Test-Path $scripts) { if (-not (([Environment]::GetEnvironmentVariable('Path','User')).Split(';') -contains $scripts)) { [Environment]::SetEnvironmentVariable('Path', [Environment]::GetEnvironmentVariable('Path','User') + ';' + $scripts, 'User'); Write-Host "✅ Added $scripts to user PATH. Restart terminal to use 'today'."; } else { Write-Host "ℹ️ $scripts is already in PATH."; } } else { Write-Host "❌ Scripts folder not found! Make sure pip is installed." }
```

## Reset PATH (Remove and Add Again) 🔄

If you want to reset the Scripts path in your User PATH:

```bash
$pyVer=(python -c "import sys;print('Python'+str(sys.version_info.major)+str(sys.version_info.minor))"); $scripts=Join-Path $env:APPDATA "Python\$pyVer\Scripts"; $current=([Environment]::GetEnvironmentVariable('Path','User')).Split(';') | Where-Object {$_ -ne $scripts}; [Environment]::SetEnvironmentVariable('Path', ($current -join ';') + ';' + $scripts, 'User'); Write-Host "🔄 Reset done: $scripts is now only once in PATH. Restart terminal."
```

## Verify Scripts Path 📋

Check your current User PATH:

```bash
([Environment]::GetEnvironmentVariable('Path','User')).Split(';') | Where-Object { $_ -ne '' }
```

Check if today.exe or other scripts exist:

```bash
$base=(python -m site --user-base).Trim(); Get-ChildItem -Path (Join-Path $base 'Scripts') -Filter "today*" -ErrorAction SilentlyContinue | Format-Table Name,FullName
```

## Usage 💡

| Command             | Description                          |
|--------------------|--------------------------------------|
| `python today.py now` | Display current time (hour, minute, second) |
| `python today.py s`   | Display Persian (Jalali) date       |
| `python today.py m`   | Display Gregorian date              |

After PATH setup, you can run from **any terminal and enywhere**:

| Command | Description |
|---------|-------------|
| `today now` | Display current time |
| `today s`   | Display Persian date |
| `today m`   | Display Gregorian date |


## Requirements 📋

- Python 3.7+
- rich >= 13.0.0
- jdatetime >= 4.0.0

<div align="center">
Give a ⭐ if you found this helpful!
</div>
