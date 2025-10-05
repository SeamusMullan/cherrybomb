# Force use of Homebrew LLVM's libc++ for both compile and link
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++ -L/opt/homebrew/opt/llvm/lib/c++")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -stdlib=libc++ -L/opt/homebrew/opt/llvm/lib/c++")

cmake_minimum_required(VERSION 3.25)

# Force C++23 everywhere
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
add_compile_options(-std=c++23)

project(cherrybomb LANGUAGES CXX OBJCXX VERSION 1.0.0)



add_executable(${PROJECT_NAME} "src/main.cpp")
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_23)
set_target_properties(${PROJECT_NAME} PROPERTIES CXX_STANDARD 23 CXX_STANDARD_REQUIRED ON CXX_EXTENSIONS OFF)

include(cmake/CPM.cmake)
CPMAddPackage(
  NAME           saucer
  VERSION        7.0.0
  GIT_REPOSITORY "https://github.com/saucer/saucer"
)

CPMAddPackage(
  NAME           saucer-desktop
  VERSION        4.0.2
  GIT_REPOSITORY "https://github.com/saucer/desktop"
)

target_link_libraries(${PROJECT_NAME} PRIVATE saucer saucer::desktop)

