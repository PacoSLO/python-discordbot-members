title BOT NAME
:loop
start /min "BOT NAME" "PATH TO YOUR STARTBOT.bat SCRIPT"
timeout /t 4000
taskkill /FI "WindowTitle eq BOT NAME*" /T /F
timeout /t 3
goto loop

