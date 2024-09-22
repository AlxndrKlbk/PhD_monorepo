#include <boost/multiprecision/float128.hpp>
#include <boost/math/special_functions/gamma.hpp>
#include <iostream>


// using boost::multiprecision::float128;

int main(int argc, char ** argv)
{
    using namespace boost::multiprecision;
    float128 quad_float = 2.1;
    std::cout << argc << argv << std::endl;
    std::cout << boost::math::tgamma(quad_float) << std::endl;
    //call module in function.hpp
    return 0;
}
