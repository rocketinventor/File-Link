@echo off

:: Set the correct working directory
CD /D "%~dp0"

:: Run script
@echo on
py "%CD%\file_link.py" %*
@pause