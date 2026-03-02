@echo off
chcp 65001 >nul
title Kasmir Árajánlat Generátor
echo.
echo  Kasmir Árajánlat Generátor indul...
echo  Cim: http://localhost:8765
echo  Jelszó: kasmir2025
echo  Leállítás: Ctrl+C
echo.

python --version >nul 2>&1
if %errorlevel% == 0 ( python app.py & goto :end )

python3 --version >nul 2>&1
if %errorlevel% == 0 ( python3 app.py & goto :end )

echo HIBA: Python nem talalhato!
echo Toltsd le: https://www.python.org/downloads/
pause
:end
