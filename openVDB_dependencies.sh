#!/bin/bash
# Core library
apt-get install cmake                   # CMake
apt-get install libtbb-dev              # TBB
apt-get install zlibc                   # zlib
apt-get install libboost-iostreams-dev  # Boost::iostream
apt-get install libblosc-dev            # Blosc
# AX
apt-get install llvm-10-dev             # LLVM
# Python
apt-get install pybind11-dev            # Python
apt-get install python-dev              # Python
apt-get install python-numpy            # NumPy
# Optional
apt-get install libpng-dev              # libpng
apt-get install libopenexr-dev          # OpenEXR
apt-get install liblog4cplus-dev        # Log4cplus
apt-get install googletest              # GoogleTest
apt-get install libcppunit-dev          # CppUnit
# vdb_view
apt-get install libglfw3-dev            # GLFW
# Documentation
apt-get install doxygen                 # doxygen
# CUDA for NanoVDB
apt-get install nvidia-cuda-toolkit     # CUDA
