import operator
from decimal import Decimal
from functools import reduce


class Calculations(object):
    @staticmethod
    def calculate_power(data):
        nu_mul = data.nu * data.nu_zero
        nu_sq = data.nu * Decimal.sqrt(Decimal(2))

        vars = (data.m_tm / nu_mul, data.m_st / nu_mul,
                ((data.q_n * data.omega_m) / nu_sq )if data.q_n else 0,
                ((data.k_sh * data.alfa_m) / nu_sq) if data.k_sh else 0,
                ((data.j_n * data.epsilon_m) / nu_sq) if data.j_n else 0)

        sum_m_sq = reduce(operator.add, [item**2 for item in vars])
        sqrt_arg = sum_m_sq + (data.j_n * data.epsilon_m * Decimal.sqrt(
            sum_m_sq)) / (data.nu * Decimal.sqrt(Decimal(2)))
        p_tr = ((Decimal.sqrt(Decimal(2)) * data.omega_m / data.alfa_omega) *
                Decimal.sqrt(sqrt_arg))

        return p_tr

    @classmethod
    def check_engine(cls, data, power, engines, engine):


        nu = data.nu if data.nu else 0
        nu_zero = data.nu_zero if data.nu_zero else 0
        nu_mul = nu * nu_zero
        m_tm = data.m_tm if data.m_tm else 0
        m_st = data.m_st if data.m_st else 0
        q_n = data.q_n if data.q_n else 0
        omega_m = data.omega_m if data.omega_m else 0
        k_sh = data.k_sh if data.k_sh else 0
        alfa_m = data.alfa_m if data.alfa_m else 0
        j_n = data.j_n if data.j_n else 0
        epsilon_m = data.epsilon_m if data.epsilon_m else 0
        alfa_omega = data.alfa_omega if data.alfa_omega else 0
        vars = (m_tm / nu_mul, m_st / nu_mul,
                ((q_n * omega_m) / nu),
                ((k_sh * alfa_m) / nu) if k_sh else 0,
                ((j_n * epsilon_m) / nu) if j_n else 0)
        i_range = range(1, 50)

        fist_neq = lambda i : (alfa_omega *
                               engine.nominal_angular_velocity >=
                               i * data.omega_m)
        summ_mhj = reduce(operator.add, [item for item in vars])

        #Вместо qd используем data.q_n
        eq_left = abs(engine.nominal_momentum + ((engine.nominal_angular_velocity *
                                                  q_n) /
                                                 data.Kq) - engine.static_loosing_momentum)
        eq_right = lambda i: (summ_mhj / i +
                              abs((q_n * omega_m) / data.Kq +
                                  data.Kr * engine.rotor_momentum * epsilon_m) * i)
        sec_neq = lambda i : eq_left >= eq_right(i)

        third_neq = lambda i:(( engine.momentum_overload_coefficient *
                               engine.nominal_momentum) >=
                              (summ_mhj / i) +
                              data.Kr * engine.rotor_momentum * epsilon_m * i
                              )


        first_eq = [i for i in i_range if fist_neq(i)]
        sec_eq = [i for i in i_range if sec_neq(i)]
        third_eq = [i for i in i_range if third_neq(i)]

        all_sets = set(first_eq) & set(sec_eq) & set(third_eq)
        return (min(all_sets), max(all_sets))




