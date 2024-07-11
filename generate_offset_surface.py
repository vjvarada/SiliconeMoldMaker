import os
import sys

# Define the working directory and configuration
working_directory = r'C:/Users/Vijay/Documents/GitHub/SiliconeMoldMaker/openvdb/build/openvdb/openvdb/python/Release'
config = 'Release'  # Change this if you have a different configuration like Debug

# Add the working directory to the system path
sys.path.append(working_directory)

# Add required DLL directories from the binary build tree
if 'add_dll_directory' in dir(os):
    dll_path = os.path.join(working_directory, '../../', config)
    os.add_dll_directory(dll_path)

    # Add additional DLL directories if specified by environment variable
    if os.getenv('OPENVDB_TEST_PYTHON_AX'):
        additional_dll_path = os.path.join(working_directory, '../../../../openvdb_ax/openvdb_ax/', config)
        os.add_dll_directory(additional_dll_path)

# Print out the current DLL directories for verification
print("Current DLL directories:")
for path in os.environ.get("PATH").split(';'):
    print(path)

# Import the pyopenvdb module
try:
    import pyopenvdb as vdb
    print("pyopenvdb module imported successfully.")
except ImportError as e:
    print(f"ImportError: {e}")
except AttributeError as e:
    print(f"AttributeError: {e}")



from stl import mesh
import numpy as np
import os

# Define the path to the STL file and the output VDB file
stl_file_path = 'Female.stl'
output_vdb_path = 'Female_offset.vdb'

# Load the STL file
stl_mesh = mesh.Mesh.from_file(stl_file_path)

# Create a new VDB FloatGrid
grid = vdb.FloatGrid()
grid.background = 1.0

# Function to add mesh vertices to the VDB grid
def add_mesh_to_vdb(grid, stl_mesh):
    accessor = grid.getAccessor()
    for triangle in stl_mesh.vectors:
        for vertex in triangle:
            coord = tuple(map(int, vertex))
            accessor.setValueOn(coord, 0.0)

# Add STL mesh data to the VDB grid
add_mesh_to_vdb(grid, stl_mesh)

# Transform the grid to a level set representation
grid.setGridClass(vdb.GridClass.LEVEL_SET)

# Apply an offset
offset_distance = 5.0
grid.offsetGrid(offset_distance)

# Ensure the output directory exists or create it if necessary
directory = os.path.dirname(output_vdb_path)
if directory and not os.path.exists(directory):
    os.makedirs(directory)

# Save the grid to a VDB file
vdb.write(output_vdb_path, grids=[grid])

print(f"Offset surface saved to {output_vdb_path}")