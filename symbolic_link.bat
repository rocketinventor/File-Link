@echo off

:: Get admin permission
:: https://stackoverflow.com/questions/1894967/how-to-request-administrator-access-inside-a-batch-file

REM pushd "%CD%"
CD /D "%~dp0"

:: Run script

@echo on
py "%CD%\file_link.py" %* symbolic
@pause