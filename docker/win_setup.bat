:: Script to setup Windows Docker environment. Run each time if something
:: is not working. Using bat file in order to be able to set environment
:: variables persistently

echo PLEASE RUN AS ADMINISTRATOR!

:: 1. Remove old default virtual machine.
docker-machine rm default

:: 2. Create new default virtual machine.
:: Manually install vbox driver if you get "VBoxManage.exe: error"
:: C:\Program Files\Oracle\VirtualBox\drivers\vboxdrv\VBoxDrv.inf .
docker-machine create default || goto :EOF

:: 3. Connect your Docker client to the Docker engine runnin on default virtual
:: machine.
set SETUP=c:/tmp/docker_machine_setup.bat
:: Command to print the list of commands into a temporary file, replace SET
:: with SETX to make it persistent.
docker-machine env --shell cmd default | sed "s/SET/SETX \/m/" | sed "s/=/ /" |^
grep -v REM > %SETUP%
:: Run the list of command from a temporary file (requires admin rights)
%SETUP% || echo PLEASE RUN AS ADMINISTRATOR
:: Remove the temporary file
rm %SETUP%

