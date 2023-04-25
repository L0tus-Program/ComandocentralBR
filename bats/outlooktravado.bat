@echo off

echo Finalizando outlook
taskkill /f /im outlook.exe
timeout /t 5 /nobreak
start outlook
exit