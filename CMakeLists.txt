cmake_minimum_required(VERSION 3.10)
project(GlyzteraBlockchain)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/..)

include_directories(src/include)  # Include the directory where your .h files are.

add_executable(GlyzteraBlockchain
    src/Block.cpp
    src/Blockchain.cpp
    src/main.cpp
)