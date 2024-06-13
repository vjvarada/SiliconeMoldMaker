// Save as test_openvdb.cpp in C:/Users/Vijay/Documents/GitHub/SiliconeMoldMaker
#include <openvdb/openvdb.h>
#include <iostream>

int main() {
    openvdb::initialize();
    std::cout << "OpenVDB initialized!" << std::endl;
    return 0;
}