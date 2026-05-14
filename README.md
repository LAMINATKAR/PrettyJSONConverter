# Pretty JSON Converter

A minimal Windows desktop app that converts minified JSON files to human-readable pretty-printed format.

## Usage

1. Click **Browse** and select a `.json` file
2. Click **Convert and Save**
3. Choose where to save the output — the file is pre-named `<original>_pretty.json`

## Development

**Requirements:** Python 3.x

```bash
# Create virtual environment and install dependencies
python -m venv .venv
.venv\Scripts\pip install pyinstaller
```

**Run from source:**
```bash
.venv\Scripts\python main.py
```

**Build `.exe`:**
```powershell
.venv\Scripts\pyinstaller --onefile --windowed --name "PrettyJSONConverter" --icon "icon.ico" --add-data "icon.ico;." --version-file "version.txt" main.py
# Output: dist\PrettyJSONConverter.exe
```

## Tech

- Python + tkinter (standard library only)
- No runtime dependencies
