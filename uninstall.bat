@echo off
schtasks /delete /tn InitHeadphone /F
sc delete SvThANSP

echo.
pause