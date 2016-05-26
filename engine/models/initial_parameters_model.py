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

    def update(self, values):
        def sets(name):
            if not values[name] == 'None' and not values[name] == None:
                return Decimal(values[name])
            else: return None
        self.gear_type = sets('gear_type')
        self.m_st = sets('m_st')
        self.m_tm = sets('m_tm')
        self.q_n = sets('q_n')
        self.k_sh = sets('k_sh')
        self.j_n = sets('j_n')
        self.alfa_m = sets('alfa_m')
        self.omega_m = sets('omega_m')
        self.epsilon_m = sets('epsilon_m')

        self.delta = sets('delta')
        self.chi_p = sets('chi_p')
        self.chi_s = sets('chi_s')
        self.chi_q = sets('chi_q')
        self.sigma = sets('sigma')
        self.t_n = sets('gear_type')
        self.M = sets('M')

        self.gear_type = GearType.values[int(values['gear_type'])]
        self.amplifier_type = AmplifierType.values[int(values['amplifier_type'])]

        self.Kr = Decimal(1.1)
        self.Kq = Decimal(1.5)

        self.nu = Decimal(0.85)
        self.nu_zero = Decimal(0.8)
        self.alfa_omega = Decimal(1.2)
