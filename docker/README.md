# Docker howto

## Windows 7 setup

Run [setup script]](win_setup.bat) as Administrator to setup Virtual box. This also will update
global environment variables. Run 'docker images' command to make sure
everything is working correctly

    # Windows only
    (Administrator)cmd> win_setup.bat

    # In the new shell to make sure everything is working correctly
    cmd> docker images

## Build images from Dockerfiles

Run [image building](build_images.sh) script in order to rebuild all images. Script
will print the list of available images at the end.

    # Windows
    cmd> bash build_images.sh

## Run Development image container shell

Run development shell [invocation script](run_dev.sh). Basically it is just
'docker run -i -t <image>' call.

    # Windows
    cmd> bash run_dev.sh

