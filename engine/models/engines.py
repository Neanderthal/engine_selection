from peewee import CharField, DecimalField

from engine.models.base_model import PeeweeModel


class Engine(PeeweeModel):
    name = CharField()  # Pn
    nominal_power = DecimalField()  # MN
    nominal_momentum = DecimalField()  # omega_n
    start_momentum = DecimalField()  # Mn
    nominal_angular_velocity = DecimalField()  # Jd
    static_loosing_momentum = DecimalField()  # Mtr
    rotor_momentum = DecimalField()  # Jd
    characteristical_hardness = DecimalField()  # gd
    momentum_overload_coefficient = DecimalField()  # lambda
