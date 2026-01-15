# Building Hytale RPC for Windows

## Requirements
- Windows 10/11
- Python 3.8+ installed ([Download](https://python.org))

## Steps

1. Download or clone the repo
2. Open Command Prompt in the project folder
3. Run:
```
scripts\build_windows.bat
```
4. Wait for the build to complete
5. Find `HytaleRPC.exe` in the `releases` folder
6. Run it - look for the icon in your system tray

## Run at Startup (Optional)

1. Press `Win+R`
2. Type `shell:startup` and press Enter
3. Copy `HytaleRPC.exe` into that folder

Done! The app will now start automatically when Windows boots.
