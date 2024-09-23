
project(heat_explicit_solver CXX)

set(TARGET implicit_heat_radial)

set(SOURCE_PATH "${PROJECT_SOURCE_DIR}/src" )
set(INCLUDE_PATH "${PROJECT_SOURCE_DIR}/include" )

file( GLOB_RECURSE HEADERS "${INCLUDE_PATH}/*.hpp" )
file( GLOB_RECURSE SOURCES "${SOURCE_PATH}/*.cpp" )

add_executable(${TARGET}
        ${HEADERS}
        ${SOURCES})

target_link_libraries(${TARGET}
    # PUBLIC
    #     Quadmath::quadmath
    PRIVATE
        Boost::headers
        Boost::boost
    )


# get_target_property(VAR Quadmath::quadmath INTERFACE_INCLUDE_DIRECTORIES)
# message(${VAR})
# set_target_properties(Quadmath::quadmath PROPERTIES INTERFACE_INCLUDE_DIRECTORIES "${Quadmath_INCLUDE_DIR}"
#     IMPORTED_LINK_INTERFACE_LANGUAGES "C"
#     IMPORTED_LOCATION "${Quadmath_LIBRARY}")
