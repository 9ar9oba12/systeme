@echo off
REM Launch the Houssam Ascension CLI morning briefing.
REM Update PYTHON or VENV_PYTHON to point to your interpreter if needed.
set "SCRIPT_DIR=%~dp0.."
set "PYTHON=%VENV_PYTHON%"
if "%PYTHON%"=="" set "PYTHON=python"
cd /d "%SCRIPT_DIR%"
%PYTHON% main.py morning
