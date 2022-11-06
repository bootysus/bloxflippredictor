@echo off
Color 02
Title Installing modules
Echo =====================
Echo    Module installer
Echo =====================
Echo Press any key to start Basic installer
Pause>nul
Echo started the module installer...
pip install -r requirements.txt
Echo done
Echo Press any key to exit
Pause>nul
Exit
