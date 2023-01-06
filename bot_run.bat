@echo off


call %~dp0chudesny_sad\venv\Scripts\activate


cd %~dp0chudesny_sad


set TOKEN=


python bot_telegram.py


pause