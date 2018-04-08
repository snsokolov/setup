:: Script to setup/re-setup everything.
:: NOTE: Prior Git installation with git bash extensions is required.

REM Run the body of the script with admin rights and print the log file at the end.
@>nul 2>&1 setx /m admin "" && goto admin || goto fork
:fork
@echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\adm.vbs"
@echo UAC.ShellExecute "cmd.exe", "/c %~s0 > %temp%\adm.log", "", "runas", 1 >> "%temp%\adm.vbs"
@"%temp%\adm.vbs" && del "%temp%\adm.vbs"
:waiting
@grep DONE "%temp%\adm.log" 2>nul || goto waiting
@cat "%temp%\adm.log" && rm "%temp%\adm.log"
@goto non_admin
:admin

REM ---------- 1. (Admin) Setup global env variables and enable sh execution.
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
exit /B

:non_admin
REM ---------- 2. Clone all repos.
REM Checking for Github directory. Will not overwrite it and exit.
if EXIST %GITHUB% echo "Github directory already exists, skipping." && goto no_clone

REM Create Github directory.
mkdir %GITHUB% && cd %GITHUB%

REM Clone all repos.
git clone https://snsokolov@github.com/snsokolov/contests snsokolov/contests
git clone https://snsokolov@github.com/snsokolov/pylib snsokolov/pylib
git clone https://snsokolov@github.com/snsokolov/rcfiles snsokolov/rcfiles
git clone https://snsokolov@github.com/snsokolov/setup snsokolov/setup
git clone https://snsokolov@github.com/snsokolov/vimrc_nedit snsokolov/vimrc_nedit
git clone https://snsokolov@github.com/algoart/algoart algoart/algoart
git clone https://snsokolov@github.com/cppunit/cppunit cppunit/cppunit
git clone https://snsokolov@github.com/ideallang/ideallang ideallang/ideallang
git clone https://snsokolov@github.com/unittests/unitframe unittests/unitframe
git clone https://snsokolov@github.com/unittests/bazel unittests/bazel
git clone https://snsokolov@github.com/verilogtools/fpga verilogtools/fpga
git clone https://snsokolov@github.com/windcams/windcams.github.io windcams/windcams.github.io
:no_clone

REM ---------- 3. RC files.
REM Copy RC files into windows home directory
cp %GITHUB%/snsokolov/rcfiles/.gitconfig %HOMEPATH%
cp %GITHUB%/snsokolov/vimrc_nedit/_vimrc %HOMEPATH%

REM ---------- DONE.
