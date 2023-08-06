cmake_minimum_required(VERSION 3.10)

# set the project name
project(GlyzteraBlockchain)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 14)

# add the executable
add_executable(GlyzteraBlockchain src/main.cpp src/Block.cpp src/Blockchain.cpp)

# include headers directory
target_include_directories(GlyzteraBlockchain PRIVATE src/include)

# set the executable output directory
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})