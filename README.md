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
```bash
mkdir C:/src
cd C:/src
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat
```
add vcpkg to PATH for windows so the following programs can run

```bash
vcpkg install zlib:x64-windows blosc:x64-windows tbb:x64-windows boost-iostreams:x64-windows boost-any:x64-windows boost-algorithm:x64-windows boost-interprocess:x64-windows boost:x64-windows openexr:x64-windows ilmbase:x64-windows pybind11:x64-windows glew:x64-windows eigen3:x64-windows gsl:x64-windows
or
vcpkg install zlib libpng openexr tbb gtest cppunit blosc glfw3 glew python3 jemalloc boost-iostreams boost-interprocess boost-algorithm pybind11 --clean-after-build
then
git clone https://github.com/AcademySoftwareFoundation/openvdb
cd openvdb
mkdir build
cd build
cmake -DOPENVDB_USE_DEPRECATED_ABI_9=ON -DOPENVDB_USE_DEPRECATED_ABI_10=ON -DOPENVDB_BUILD_VDB_PRINT=ON -DOPENVDB_BUILD_VDB_LOD=ON -DOPENVDB_BUILD_VDB_TOOL=ON -DOPENVDB_TOOL_USE_NANO=OFF -DOPENVDB_BUILD_PYTHON_UNITTESTS=ON -DMSVC_MP_THREAD_COUNT=8 -A x64 -G 'Visual Studio 17 2022' -DOPENVDB_CORE_STATIC=OFF -DMSVC_COMPRESS_PDB=ON -DUSE_EXR=ON -DUSE_PNG=ON -DVCPKG_TARGET_TRIPLET=x64-windows '-DCMAKE_TOOLCHAIN_FILE=C:\src\vcpkg\scripts\buildsystems\vcpkg.cmake' -DCMAKE_VERBOSE_MAKEFILE=ON -DOPENVDB_BUILD_DOCS=OFF -DOPENVDB_BUILD_VDB_VIEW=ON -DNANOVDB_BUILD_TOOLS=OFF -DNANOVDB_BUILD_EXAMPLES=OFF -DOPENVDB_BUILD_HOUDINI_PLUGIN=OFF -DOPENVDB_BUILD_AX_UNITTESTS=OFF -DOPENVDB_BUILD_PYTHON_MODULE=ON -DNANOVDB_BUILD_UNITTESTS=OFF -DOPENVDB_BUILD_AX_GRAMMAR=OFF -DNANOVDB_BUILD_BENCHMARK=OFF -DOPENVDB_BUILD_AX=OFF -DOPENVDB_BUILD_BINARIES=ON -DOPENVDB_BUILD_NANOVDB=OFF -DOPENVDB_BUILD_CORE=ON -DOPENVDB_BUILD_AX_BINARIES=OFF -DOPENVDB_BUILD_VDB_RENDER=ON -DOPENVDB_BUILD_UNITTESTS=ON ..
cmake --build . --parallel 8 --target install --verbose --config Release
ctest -V -C Release
```

Verify Installation: Ensure pyopenvdb.cp311-win_amd64.pyd is in the Python site-packages directory.
Add to PATH: Include DLL paths in the system PATH


------------------------------------------------------------------------------------------------------------------

# Step 1: Load and Visualize the STL File in Blender

Video Tutuorial: https://www.youtube.com/watch?v=usrk-Dy9nMg

## 1. Open Blender

- Start Blender on your computer. You should see the default scene with a cube, light, and camera.

## 2. Import the STL File

1. **Delete the Default Cube**:
    - Click on the cube to select it.
    - Press `X` and then `Enter` to delete the cube.

2. **Import the STL File**:
    - Go to the top left corner and select `File -> Import -> STL`.
    - Navigate to `C:\Users\Vijay\Desktop\Female.stl`.
    - Select the file and click `Import STL`.

3. **Adjust View and Scale**:
    - Press `N` to open the properties panel on the right.
    - In the properties panel, you can find the `Transform` section to adjust the location, rotation, and scale of the imported model if necessary.
    - Use the middle mouse button to rotate the view, the scroll wheel to zoom, and `Shift + Middle Mouse Button` to pan.

## 3. Inspect the Mesh

1. **Switch to Edit Mode**:
    - Press `Tab` to switch from Object Mode to Edit Mode.
    - In Edit Mode, you can see the vertices, edges, and faces of the mesh.

2. **Check for Non-Manifold Edges**:
    - In the top bar, switch to `Vertex Select` mode or press `1` on your keyboard.
    - Press `A` to select all vertices.
    - Press `Shift + Ctrl + Alt + M` to select non-manifold edges. These are edges that might cause problems in 3D printing or further processing.
    - If any non-manifold edges are highlighted, consider fixing them using Blender’s tools.

3. **Check for Holes**:
    - Press `A` to deselect all vertices.
    - Press `Alt + Shift + F` to fill holes. This will help ensure that the model is watertight, which is crucial for mold making.

4. **Clean Up the Mesh**:
    - Press `A` to select all vertices.
    - Go to the menu on the left, under `Mesh -> Clean Up` and choose `Remove Doubles`. This will merge duplicate vertices.

## 4. Save Your Work

1. **Save the Blender File**:
    - Go to `File -> Save As`.
    - Save the file as `Female.blend` to keep a copy of your work in Blender.

2. **Export Cleaned STL**:
    - If you made any modifications, export the cleaned model as an STL file.
    - Go to `File -> Export -> STL` and save the file as `Female_cleaned.stl`.
## Tips for Blender Navigation

- **Zooming**: Use the scroll wheel to zoom in and out.
- **Rotating**: Click and hold the middle mouse button to rotate the view.
- **Panning**: Hold `Shift` and the middle mouse button to pan the view.
- **Selection Modes**: Use `1` for vertices, `2` for edges, and `3` for faces in Edit Mode.
- **Manipulating Objects**: Use `G` to grab (move), `S` to scale, and `R` to rotate objects.

## Next Steps

Once you have loaded and inspected the STL file in Blender, the next step will be to use OpenVDB to generate an offset surface. Let me know when you’re ready to move forward or if you need help with any specific part of this step!

------------------------------------------------------------------------------------------------------------




