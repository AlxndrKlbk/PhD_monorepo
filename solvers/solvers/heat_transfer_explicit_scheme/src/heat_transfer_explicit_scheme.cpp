#include "heat_transfer_explicit_scheme.hpp"

#include <boost/multiprecision/float128.hpp>
#include <boost/multiprecision/cpp_bin_float.hpp>
#include <boost/math/special_functions/gamma.hpp>

#include <iostream>
#include <array>

// типы повышенной точности
namespace bmp = boost::multiprecision;
using boost_float = bmp::number<bmp::cpp_bin_float<200>>;

// параметры моделируемой области
// ToDo: нормально считать температуропроводность
const boost_float a = 1;               // коэффициент температуропроводности a = теплопроводность / (теплоемкость * плотность)
const boost_float L = 100;             // длина моделируемой области (м)
constexpr size_t x_steps = 100;      // количество точек по пространству
constexpr ulong t = 3600;            // период времени для моделирования (секунд)
constexpr ulong tau_steps = 100;      // количество временных шагов

// граничные условия
// r {0;1}
boost_float U_r_tau0 = 20;              // U(r, 0) начальное распределние температуры (C) в области
boost_float U_r0_tau = 400;             // U(0, tau) - функция(const) температура на левой границе
boost_float U_r_tau = U_r_tau0;          // U(1, tau) - функция(const) температура на правой границе

// таким образом
constexpr ulong tau = t / tau_steps;                                            // шаг по времени в секундах
const boost_float h = 1.0 / tau_steps;                                          // h параметр (приращение по безразмерной координате)
const boost_float dtau = t / tau_steps * (bmp::pow(a, 2) / bmp::pow(L, 2));     // dtau (приращение по безразмерному времени)

using calculation_net = std::array<std::array<boost_float, tau_steps>, x_steps>;

int solve()
{
    std::cout << sizeof(double) << std::endl;
    // std::cout << sizeof(bmp::float128) << std::endl;
    std::cout << sizeof(boost_float) << std::endl;
    //call module in function.hpp

    std::cout << "calculation output:" << std::endl;
    calculation_net u {{{0}}};

    // начальное распределение температуры в области в каждой точке
    for(ulong i = 0; i < x_steps; i++) {
        u[i][0] = U_r_tau0;
    }

    // левая и правая граница с постоянной температурой
    for (ulong tau = 0; tau < tau_steps; tau++) {
        u[0][tau] = U_r0_tau;
        u[x_steps - 1][tau] = U_r_tau;
    }

    // start явная схема
    auto h_square = bmp::pow(h, 2);
    auto&& h_square_str = h_square.str();
    auto&& dtau_str = dtau.str();

    for (ulong tau = 0; tau < tau_steps; tau++) {
        for (ulong i = 1; i < x_steps - 1; i++) {
            // debug code
            auto&& a1 = u[i+1][tau] - 2 * u[i][tau] + u[i-1][tau];
            auto const&& a1_str = a1.str();

            auto&& u_prev = u[i-1][tau].str();
            auto&& u_next = u[i+1][tau].str();
            auto&& u_here = u[i][tau].str();
            auto&& a2 = (a1 / h_square * dtau).str();
            // debug code end
            auto&& calculated = (((u[i+1][tau] - 2 * u[i][tau] + u[i-1][tau]) / h_square ) * dtau + u[i][tau]);
            auto const&& calc_val = calculated.str();
            u[i][tau+1] = calculated;
        }
    }
    // stop явная схема

    // тут можно вывести произвольную точку в произвольный момент времени и сравнить с аналитическими решениями?
    for (ulong tau = 0; tau < tau_steps; tau++) {
        std::cout << "step " << tau << ": " << u[1][tau] << std::endl;
    }

    return 0;
}
