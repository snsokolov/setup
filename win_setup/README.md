# Windows development setup

## Install required tools

Git installation is required. Other tools like Python, GCC are optional.

Git Install: http://git-scm.com/download/win

## Setup scripts

Run `setup_all.bat` script to setup/re-setup everything, or run sep by step
setup scripts for each particular step.

    :: Run everything
    setup_all.bat

Step by step setup scripts:

    :: 1. Setup global env variables and enable sh execution.
    setup_admin.bat

    :: 2. Clone all repos.
    clone_repos.bat

    :: 3. Setup RC files.
    rc_files.bat
