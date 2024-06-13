# Save as test_import.py in the same directory as the .pyd file
import sys
import os

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Append the current directory to sys.path
sys.path.append(os.getcwd())

try:
    import pyopenvdb  # Replace pyopenvdb with the name of your module if different
    print("pyopenvdb imported successfully")
except ImportError as e:
    print("Failed to import pyopenvdb:", e)