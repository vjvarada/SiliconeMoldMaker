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
    import pyopenvdb as openvdb
    print("pyopenvdb module imported successfully.")
    # Initialize OpenVDB
    openvdb.initialize()
    print("OpenVDB initialized successfully.")
except ImportError as e:
    print(f"ImportError: {e}")
except AttributeError as e:
    print(f"AttributeError: {e}")

# Verify the pyopenvdb functions
print("pyopenvdb functions and classes:")
print(dir(openvdb))

['Axis', 'BoolGrid', 'BoolGridAccessor', 'BoolGridConstAccessor', 'BoolGridValueAllCIter', 'BoolGridValueAllCIterValue',
 'BoolGridValueAllIter', 'BoolGridValueAllIterValue', 'BoolGridValueOffCIter', 'BoolGridValueOffCIterValue', 'BoolGridValueOffIter',
 'BoolGridValueOffIterValue', 'BoolGridValueOnCIter', 'BoolGridValueOnCIterValue', 'BoolGridValueOnIter', 'BoolGridValueOnIterValue',
 'COORD_MAX', 'COORD_MIN', 'FILE_FORMAT_VERSION', 'FloatGrid', 'FloatGridAccessor', 'FloatGridConstAccessor', 'FloatGridValueAllCIter',
 'FloatGridValueAllCIterValue', 'FloatGridValueAllIter', 'FloatGridValueAllIterValue', 'FloatGridValueOffCIter', 'FloatGridValueOffCIterValue',
 'FloatGridValueOffIter', 'FloatGridValueOffIterValue', 'FloatGridValueOnCIter', 'FloatGridValueOnCIterValue', 'FloatGridValueOnIter',
 'FloatGridValueOnIterValue', 'GridBase', 'GridClass', 'GridTypes', 'LEVEL_SET_HALF_WIDTH', 'LIBRARY_VERSION', 'Metadata', 'Transform',
 'Vec3SGrid', 'Vec3SGridAccessor', 'Vec3SGridConstAccessor', 'Vec3SGridValueAllCIter', 'Vec3SGridValueAllCIterValue', 'Vec3SGridValueAllIter',
 'Vec3SGridValueAllIterValue', 'Vec3SGridValueOffCIter', 'Vec3SGridValueOffCIterValue', 'Vec3SGridValueOffIter', 'Vec3SGridValueOffIterValue',
 'Vec3SGridValueOnCIter', 'Vec3SGridValueOnCIterValue', 'Vec3SGridValueOnIter', 'Vec3SGridValueOnIterValue', 'VectorType', 'X', 'Y', 'Z',
 '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'createFrustumTransform', 'createLevelSetSphere',
 'createLinearTransform', 'getLoggingLevel', 'read', 'readAll', 'readAllGridMetadata', 'readGridMetadata', 'readMetadata',
 'setLoggingLevel', 'setProgramName', 'write']