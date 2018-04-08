:: Script to setup Windows Docker environment. Run each time if something
:: is not working. Using bat file in order to be able to set environment
:: variables persistently

:: TODO: Use my windows setup hack to run as administrator.
echo PLEASE RUN AS ADMINISTRATOR!

REM ---------- 1. Remove old default virtual machine.
:: If you get "error removing host default. The system cannot find the file
:: specified.", delete the machine directory manually and remove
:: C:\Users\%USER%\.VirtualBox directory.
docker-machine rm default

REM ---------- 2. Create new default virtual machine.
:: NOTE: The disk size can only be changed when machine is created.
:: NOTE: You may need to manually install vbox driver if you get
:: "VBoxManage.exe: error". Click install on this file:
:: TODO: Do this from batch file?
:: C:\Program Files\Oracle\VirtualBox\drivers\vboxdrv\VBoxDrv.inf
docker-machine create -d virtualbox --virtualbox-disk-size=11000 default || goto :EOF

REM ---------- 3. Configure the VM to a specific workstation
:: My specific settings: 2 CPUs and 6 GB RAM
docker-machine stop
VBoxManage modifyvm default --cpus 2
VBoxManage modifyvm default --memory 6000
docker-machine start

REM ---------- 4. Connect your Docker client to the Docker engine default VM.
set SETUP=c:/tmp/docker_machine_setup.bat
:: Command to print the list of commands into a temporary file, replace SET
:: with SETX to make it persistent.
docker-machine env --shell cmd default | sed "s/SET/SETX \/m/" | sed "s/=/ /" |^
grep -v REM > %SETUP%
:: Run the list of command from a temporary file (requires admin rights)
%SETUP% || echo PLEASE RUN AS ADMINISTRATOR
:: Remove the temporary file
rm %SETUP%

