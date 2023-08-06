cmake_minimum_required(VERSION 3.10)

# set the project name
project(GlyzteraBlockchain)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# add the executable
add_executable(GlyzteraBlockchain src/Block.cpp src/Blockchain.cpp src/main.cpp)
