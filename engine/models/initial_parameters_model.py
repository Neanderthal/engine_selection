import operator
from decimal import *
from functools import reduce

from engine.models.base_model import BaseModel
from engine.models.enums import GearingType, GearType, AmplifierType


class InitialParametersModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.gear_type = GearingType.PA
        self.m_st = Decimal(10)
        self.m_tm = Decimal(2.0)
        self.q_n = None
        self.k_sh = None
        self.j_n = Decimal(2.0)
        self.alfa_m = None
        self.omega_m = Decimal(2.0)
        self.epsilon_m = Decimal(0.4)

        self.delta = None
        self.chi_p = None
        self.chi_s = Decimal(10)
        self.chi_q = Decimal(5)
        self.sigma = None
        self.t_n = None
        self.M = Decimal(1.5)

        self.gear_type = GearType.GearWheels
        self.amplifier_type = AmplifierType.Transistor

        self.Kr = Decimal(1.1)
        self.Kq = Decimal(1.5)

        self.nu = Decimal(0.85)
        self.nu_zero = Decimal(0.8)
        self.alfa_omega = Decimal(1.2)

    def calculate_power(self):
        nu_mul = self.nu * self.nu_zero
        nu_sq = self.nu * Decimal.sqrt(Decimal(2))

        vars = (self.m_tm / nu_mul, self.m_st / nu_mul,
                (self.q_n * self.omega_m) / nu_sq if self.q_n else 0,
                (self.k_sh * self.alfa_m) / nu_sq if self.k_sh else 0,
                (self.j_n * self.epsilon_m) /nu_sq if self.q_n else 0)

        sum_m_sq = reduce(operator.add, [item**2 for item in vars])
        sqrt_arg = sum_m_sq + (self.j_n * self.epsilon_m * Decimal.sqrt(
            sum_m_sq)) / (self.nu * Decimal.sqrt(Decimal(2)))
        p_tr = (Decimal.sqrt(Decimal(2)) * self.omega_m / self.alfa_omega)*Decimal.sqrt(sqrt_arg)

        return p_tr
