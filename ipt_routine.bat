@REM @echo off
@REM cd /d "%~dp0"
@REM where python >nul 2>nul
@REM if errorlevel 1 (
@REM     echo Python is not installed or not in PATH.
@REM     pause
@REM     exit /b
@REM )
@REM python ipt_login.py
@REM pause

@echo off
cd /d "%~dp0"

:: Run your executable directly
ipt_login.exe

pause
