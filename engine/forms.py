from flask.ext.wtf import Form
from wtforms import DecimalField, SelectField, RadioField, StringField, \
    IntegerField, HiddenField
from wtforms.validators import DataRequired, Optional

from engine.models.enums import GearingType, GearType, AmplifierType


class InitialForm(Form):
    gearing_type = SelectField('Назначение привода: ', [DataRequired()],
                               choices=GearingType.get_choices(), coerce=int,
                               default=GearingType.PA)
    m_st = DecimalField('Мст - активный стати­ческий момент: ', [Optional()])
    m_tm = DecimalField('Мтм - момент сухого трения: ', [DataRequired()])
    q_n = DecimalField('qн - коэффициент момента вязкого трения: ',
                       [Optional()])
    k_sh = DecimalField('Кш - ко­эффициент шарнирного момента: ', [Optional()])
    j_n = DecimalField('Jn - момент инерции нагрузки: ', [DataRequired()])
    alfa_m = DecimalField('\u03B1m - максимальный угол поворота: ',
                          [Optional()])
    omega_m = DecimalField('\u03A9m - наибольшая угловая скорость: ',
                           [DataRequired()])
    epsilon_m = DecimalField('\u03B5m - наибольшее угловое ускорение: ',
                             [Optional()])

    delta = DecimalField(
        '\u03B4 - допустимая от­носительная ошибка стабилизации скорости: ',
        [Optional()])
    chi_p = DecimalField('\u03C7p - допустимая статическая ошибка: ',
                         [Optional()])
    chi_s = DecimalField('\u03C7s - допустимая скоростная ошибка: ',
                         [Optional()])
    chi_q = DecimalField('\u03C7q - допустимая гармоническая ошибка: ',
                         [Optional()])
    sigma = DecimalField('\u03C3 - перерегулирование: ', [Optional()])
    t_n = DecimalField('tn - требующееся время переходного процесса: ',
                       [Optional()])
    M = DecimalField('M - показатель колебательности: ', [Optional()])

    gear_type = SelectField('Тип передачи мех-зма: ', [DataRequired()],
                            choices=GearType.get_choices(), coerce=int,
                            default=GearType.GearWheels)
    amplifier_type = SelectField('Тип услителя: ', [DataRequired()],
                                 choices=AmplifierType.get_choices(),
                                 coerce=int, default=AmplifierType.Transistor)


class EngineSelectForm(Form):
    engine = RadioField('Назначение привода: ',  [DataRequired()], coerce = int)



class EngineForm(Form):
    id = HiddenField()
    name = StringField('Наименование: ', [DataRequired()])
    nominal_power = DecimalField('Мст - Номинальная мощность: ', [Optional()])
    nominal_momentum = DecimalField('Мтм - Номиальный момент: ', [DataRequired()])
    start_momentum = DecimalField('qн - Стартовый момент: ',
                       [Optional()])
    nominal_angular_velocity = DecimalField('Кш - Номинальая угловая скорость: ', [Optional()])
    static_loosing_momentum = DecimalField('Jn - Потери: ', [DataRequired()])
    rotor_momentum = DecimalField('\u03B1m - Момент ротора: ',
                          [Optional()])
    characteristical_hardness = DecimalField('\u03A9m - Жесткость характеристики: ',
                           [DataRequired()])
    momentum_overload_coefficient = DecimalField('\u03B5m - перегрузка: ',
                             [Optional()])