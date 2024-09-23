#include <boost/multiprecision/cpp_bin_float.hpp>
#include <boost/math/special_functions/gamma.hpp>
#include <iostream>


namespace bmp = boost::multiprecision;
using boost_float = bmp::number<bmp::cpp_bin_float<200>>;

int main(int argc, char ** argv)
{
    boost_float f1 = 2.1;
    boost_float f2 = 3.2;
    std::cout << argc << argv << std::endl;
    std::cout << f1 + f2 << std::endl;
    std::cout << boost::math::tgamma(f1) << std::endl;
    //call module in function.hpp
    return 0;
}
