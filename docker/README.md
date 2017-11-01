# Docker howto

## Windows 7 setup

Run [win_setup.bat](win_setup.bat) as Administrator to setup Virtual box. This
also will update global environment variables. Run 'docker images' command to
make sure everything is working correctly

    # Windows only
    (Administrator)cmd> win_setup.bat

    # In the new shell to make sure everything is working correctly
    cmd> docker images

## Build images from Dockerfiles

Run [build_images.sh](build_images.sh) script in order to rebuild all images.
Script will print the list of available images at the end.

    # Windows
    cmd> bash build_images.sh

## Run Development image container shell

Run development image container shell script [run_dev.sh](run_dev.sh).
Basically it is just a 'docker run -i -t <image>' call.

    # Windows
    cmd> bash run_dev.sh

