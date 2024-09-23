
cmake_minimum_required(VERSION 3.30)


set(PHD_PROJECT_MAJOR 0)
set(PHD_PROJECT_MINOR 1)
set(PHD_PROJECT_PATCH 0)

project(phd_project VERSION ${PHD_PROJECT_MAJOR}.${PHD_PROJECT_MINOR}.${PHD_PROJECT_PATCH}.0
        LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_PREFIX_PATH "/usr/lib/gcc/x86_64-pc-linux-gnu/14.2.1/" ${CMAKE_PREFIX_PATH})
# set(CMAKE_INCLUDE_PATH "/usr/lib/gcc/x86_64-pc-linux-gnu/14.2.1/include")
# include_directories("/usr/lib/gcc/x86_64-pc-linux-gnu/14.2.1/include")
# set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

find_package(Boost REQUIRED)
# find_package(Quadmath REQUIRED)

add_compile_options(
    -Werror
    -Wall
    -Wextra
    -Wpedantic
    -Wcast-align
    -Wcast-qual
    -Wconversion
    -Wctor-dtor-privacy
    -Wenum-compare
    -Wfloat-equal
    -Wnon-virtual-dtor
    -Wold-style-cast
    -Woverloaded-virtual
    -Wredundant-decls
    -Wsign-conversion
    -Wsign-promo
)

if(NOT CMAKE_CXX_EXTENSIONS)
    set(CMAKE_CXX_EXTENSIONS OFF)
endif()

add_subdirectory(solvers/)
