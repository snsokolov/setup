:: Script to clone all my repost

REM Checking for Github directory. Will not overwrite it and exit.
if EXIST %GITHUB% echo "Github directory already exists, exiting." && exit /b

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
