
cmake_minimum_required(VERSION 3.30)


set(PHD_PROJECT_MAJOR 0)
set(PHD_PROJECT_MINOR 1)
set(PHD_PROJECT_PATCH 0)

project(phd_project VERSION ${PHD_PROJECT_MAJOR}.${PHD_PROJECT_MINOR}.${PHD_PROJECT_PATCH}.0
        LANGUAGES CXX)

# compiler options
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)            # force use GNU standart extension
message(STATUS "CMAKE_CXX_EXTENSIONS: ${CMAKE_CXX_EXTENSIONS}")
message(STATUS "CMAKE_CXX_COMPILER_ID: ${CMAKE_CXX_COMPILER_ID}")
message(STATUS "CMAKE_CXX_COMPILER: ${CMAKE_CXX_COMPILER}")

if (NOT CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  message(FATAL_ERROR "Project requre GNU compiler")
endif()

# generator options
set(CMAKE_VERBOSE_MAKEFILE ON)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)       # force cmake create JSON output with generated compile commands with flags
set(CMAKE_POSITION_INDEPENDENT_CODE ON)     # force -fPIC compile option

find_package(Boost REQUIRED)
# find_package(Quadmath REQUIRED)

add_compile_options(
    -Werror
    -Wno-error=array-bounds
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
    -fext-numeric-literals
)

### enabling libquadmath
add_link_options(
    -lquadmath)

add_subdirectory(solvers/)
