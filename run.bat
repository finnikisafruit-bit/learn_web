@echo off
cd /d "%~dp0"
set FLASK_APP=webapp:create_app
set FLASK_ENV=development
set FLASK_DEBUG=1
env\Scripts\flask.exe run
