cmake_minimum_required(VERSION 2.8.3)
project(Go1_Project)

message("-- CMAKE_SYSTEM_PROCESSOR: ${CMAKE_SYSTEM_PROCESSOR}")
if("${CMAKE_SYSTEM_PROCESSOR}" MATCHES "x86_64.*")
  set(ARCH amd64)
endif()
if("${CMAKE_SYSTEM_PROCESSOR}" MATCHES "aarch64.*")
  set(ARCH arm64)
endif()

include_directories(legged_sdk/include)
link_directories(legged_sdk/lib/cpp/${ARCH})

set(EXTRA_LIBS -pthread libunitree_legged_sdk.a)
set(CMAKE_CXX_FLAGS "-O3 -fPIC -no-pie")
set(CMAKE_CXX_STANDARD 14)

find_package(catkin QUIET)
if(${catkin_FOUND})
  catkin_package(
    INCLUDE_DIRS include
    LIBRARIES ${PROJECT_SOURCE_DIR}/legged_sdk/lib/cpp/${ARCH}/libunitree_legged_sdk.a
  )
endif()

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

add_executable(run src/run.cpp)
target_link_libraries(run ${EXTRA_LIBS})


install(TARGETS
  run
  DESTINATION bin/unitree)
install(DIRECTORY /legged_sdk/lib/cpp/${ARCH}/
  DESTINATION lib/unitree
  USE_SOURCE_PERMISSIONS)