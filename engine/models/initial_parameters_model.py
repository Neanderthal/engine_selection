import operator
from cmath import sqrt

from functools import reduce

from engine.models.base_model import BaseModel
from engine.models.enums import GearingType, GearType, AmplifierType


class InitialParametersModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.gear_type = GearingType.PA
        self.m_st = 10
        self.m_tm = 2.0
        self.q_n = None
        self.k_sh = None
        self.j_n = 2.0
        self.alfa_m = None
        self.omega_m = 2.0
        self.epsilon_m = 0.4

        self.delta = None
        self.chi_p = None
        self.chi_s = 10
        self.chi_q = 5
        self.sigma = None
        self.t_n = None
        self.M = 1.5

        self.gear_type = GearType.GearWheels
        self.amplifier_type = AmplifierType.Transistor

        self.Kr = 1.1
        self.Kq = 1.5

        self.nu = 0.85
        self.nu_zero = 0.8
        self.alfa_zero = 1.2

    def calculate_power(self):
        nu_mul = self.nu * self.nu_zero
        nu_sq = self.nu * sqrt(2)

        vars = (self.m_tm / nu_mul, self.m_st / nu_mul,
                    (self.q_n * self.omega_m) / nu_sq,
                    (self.k_sh * self.alfa_m) / nu_sq,
                    (self.j_n * self.epsilon_m))

        sum_m_sq = reduce(operator.add, [item^2 for item in vars])
        return sum_m_sq

