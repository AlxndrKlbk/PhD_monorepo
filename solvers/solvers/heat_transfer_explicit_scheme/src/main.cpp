#include <iostream>

#include "heat_transfer_explicit_scheme.hpp"

int main(int argc, char ** argv)
{
    std::cout << argc << ":" << argv << std::endl;
    solve();
    return 0;
}
