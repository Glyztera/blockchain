@echo off

REM Delete the old build directory and create a new one
if exist build rmdir /s /q build
mkdir build

REM Navigate to the build directory
cd build

REM Run CMake to generate the build files
cmake ..

REM Compile the project (modify with your actual .sln file)
msbuild MyProject.sln /p:Configuration=Release
