# SiliconeMoldMaker

Repository for the development of automatic silicone mold maker

## Setting up Development Environment

### 1. Setting up WSL& VSCode

Some packages will not install on windows, and so developing via linux is the best bet.

Setup Tutorial: https://code.visualstudio.com/docs/remote/wsl-tutorial

### 2. Set up virtual environment within WSL

    1. In the WSL terminal, install python using ```sudo apt install python3 python3-pip```
    2. navigate to the project dictrcoty ```/mnt/c/Users/Vijay/Documents/GitHub/SiliconeMoldMaker``` 
    3. enter ```code.``` to connect to VS Code
    4. create a Venv virtual environment using ```https://code.visualstudio.com/docs/python/environments#:~:text=To%20create%20local%20environments%20in,environment%20types%3A%20Venv%20or%20Conda.```
    
### 3. install openVDB
    1. Refer Documentation: https://github.com/AcademySoftwareFoundation/openvdb
    2. Refer Documentation: https://www.openvdb.org/documentation/doxygen/build.html
    3. install dependencies for openVDB:
        ```
        chmod +x openVDB_dependencies.sh
        ./openVDB_dependencies.sh 
        ```
    4.install openVDB
        ```
        git clone https://github.com/AcademySoftwareFoundation/openvdb.git
        cd openvdb
        mkdir build
        cd build
        cmake .. -DCMAKE_INSTALL_PREFIX=/usr/local -DOPENVDB_BUILD_PYTHON_MODULE=ON
        make -j4 && make install
        
        ```

---------------------------------------------------------




Refer Documentation: https://github.com/AcademySoftwareFoundation/openvdb
Refer Documentation: https://www.openvdb.org/documentation/doxygen/build.html

cd C:/src/vcpkg
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat

add vcpkg to PATH

vcpkg install zlib:x64-windows blosc:x64-windows tbb:x64-windows boost-iostreams:x64-windows boost-any:x64-windows boost-algorithm:x64-windows boost-interprocess:x64-windows boost:x64-windows openexr:x64-windows ilmbase:x64-windows pybind11:x64-windows glew:x64-windows eigen3:x64-windows gsl:x64-windows
git clone git@github.com:AcademySoftwareFoundation/openvdb.git
cd openvdb
mkdir build
cd build
cmake -DCMAKE_TOOLCHAIN_FILE=C:/src/vcpkg/scripts/buildsystems/vcpkg.cmake -DVCPKG_TARGET_TRIPLET=x64-windows -A x64 -DOPENVDB_BUILD_PYTHON_MODULE=ON ..
cmake --build . --parallel 4 --config Release --target install

