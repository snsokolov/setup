:: Script to setup global env variables and enable sh execution.

REM Run the body of the script with admin rights and print the log file at the end.
@>nul 2>&1 setx /m admin "" && goto done || goto fork
:fork
@echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\adm.vbs"
@echo UAC.ShellExecute "cmd.exe", "/c %~s0 > %temp%\adm.log", "", "runas", 1 >> "%temp%\adm.vbs"
@"%temp%\adm.vbs" && del "%temp%\adm.vbs"
:waiting
@grep DONE "%temp%\adm.log" 2>nul || goto waiting
@cat "%temp%\adm.log" && rm "%temp%\adm.log"
@exit /B
:done

REM Set some standard variables.
setx /m GITHUB C:\Personal\Drive\Github
setx /m EDITOR gvim
setx /m PYTHONPATH %GITHUB%\snsokolov\pylib

REM Enable .sh files execution by inline shell and not by GUI shell.
reg add "HKEY_CLASSES_ROOT\Applications\sh.exe\shell\open\command" /f /ve /d "C:\Program Files\Git\bin\sh.exe %%1"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.sh\OpenWithList" /f /v a /d sh.exe
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\.sh\UserChoice" /f /v Progid /d Applications\\sh.exe

REM Enable 'e' alias to invoke Gvim
cp %windir%/gvim.bat %windir%/e.bat

:: DONE os required to signal the parent process that the script has finished.
echo DONE
