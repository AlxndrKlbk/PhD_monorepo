
project(heat_explicit_solver LANGUAGES CXX)

set(TARGET implicit_heat_radial)

set(SOURCE_PATH "${PROJECT_SOURCE_DIR}/src" )
set(INCLUDE_PATH "${PROJECT_SOURCE_DIR}/include" )

file( GLOB_RECURSE HEADERS "${INCLUDE_PATH}/*.hpp" )
file( GLOB_RECURSE SOURCES "${SOURCE_PATH}/*.cpp" )

add_executable(${TARGET}
        ${HEADERS}
        ${SOURCES})

target_link_libraries(${TARGET}
    PRIVATE
        Boost::headers
        Boost::boost
    )

