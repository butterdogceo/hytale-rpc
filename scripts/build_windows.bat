@echo off
cd /d "%~dp0\.."

echo Building Hytale RPC for Windows...

pip install pyinstaller pypresence psutil pystray pillow --quiet

pyinstaller --onefile --windowed ^
    --name "HytaleRPC" ^
    --add-data "assets\image.png;." ^
    --hidden-import pystray ^
    --hidden-import PIL ^
    --hidden-import pypresence ^
    --hidden-import psutil ^
    hytale_rpc.py

if not exist "releases" mkdir releases
copy "dist\HytaleRPC.exe" "releases\HytaleRPC.exe"

echo.
echo Build complete!
echo Executable: releases\HytaleRPC.exe
echo.
pause
