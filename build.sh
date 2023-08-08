#!/bin/sh

# Delete the old build directory and create a new one
rm -rf build
mkdir build

# Navigate to the build directory
cd build

# Run CMake to generate the build files
cmake ..

# Compile the project
make
