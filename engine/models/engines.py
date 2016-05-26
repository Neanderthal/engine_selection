from peewee import CharField, DecimalField

from engine.models.base_model import PeeweeModel


class Engine(PeeweeModel):
    name = CharField()
    nominal_power = DecimalField()  # Pn
    nominal_momentum = DecimalField() # MN
    start_momentum = DecimalField()  # Mn
    nominal_angular_velocity = DecimalField()  # omega_n
    static_loosing_momentum = DecimalField()  # Mtr
    rotor_momentum = DecimalField()  # Jd
    characteristical_hardness = DecimalField()  # gd
    momentum_overload_coefficient = DecimalField()  # lambda
