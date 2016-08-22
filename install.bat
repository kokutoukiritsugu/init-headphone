@echo off
schtasks /delete /tn InitHeadphone /F
schtasks /create /tn InitHeadphone /xml InitHeadphone.xml
schtasks /change /tn InitHeadphone /TR %cd%\InitHeadphone.exe

echo.
pause