# Docker howto

## Windows 7 setup

Run setup script as Administrator to setup Virtual box. This also will update
global environment variables. Run 'docker images' command to make sure
everything is working correctly

    <Administrator cmd.exe> [win_setup.bat](win_setup.bat)
    <Administrator cmd.exe> docker images

## Build images from Dockerfiles

Run image building script in order to rebuild all images. Script
will print the list of available images at the end.

    [build_images.sh](build_images.sh)

## Run Development image container shell

Run development shell invocation script. Basically it's a
'docker run -i -t <image>' call.

    [run_dev.sh](run_dev.sh)

