from flask.ext.wtf import Form
from wtforms import DecimalField, SelectField
from wtforms.validators import DataRequired

from engine.models.enums import GearingType, GearType, AmplifierType


class InitialForm(Form):
    gearing_type = SelectField('Назначение привода: ', [DataRequired()], choices=GearingType.get_choices())
    m_st = DecimalField('Мст - активный стати­ческий момент: ')
    m_tm = DecimalField('Мтм - момент сухого трения: ', [DataRequired()])
    q_n = DecimalField('qн - коэффициент момента вязкого трения: ')
    k_sh = DecimalField('Кш - ко­эффициент шарнирного момента: ')
    j_n = DecimalField('Jn - момент инерции нагрузки: ', [DataRequired()])
    alfa_m = DecimalField('\u03B1m - максимальный угол поворота: ', [DataRequired()])
    omega_m = DecimalField('\u03A9m - наибольшая угловая скорость: ', [DataRequired()])
    epsilon_m = DecimalField('\u03B5m - наибольшее угловое ускорение: ')

    delta = DecimalField('\u03B4 - допустимая от­носительная ошибка стабилизации скорости: ')
    chi_p = DecimalField('\u03C7p - допустимая статическая ошибка: ')
    chi_s = DecimalField('\u03C7s - допустимая скоростная ошибка: ')
    chi_q = DecimalField('\u03C7q - допустимая гармоническая ошибка: ')
    sigma = DecimalField('\u03C3 - перерегулирование: ')
    t_n = DecimalField('tn - требующееся время переходного процесса: ')
    M = DecimalField('M - показатель колебательности: ')

    gear_type = SelectField('Тип передачи мех-зма: ', [DataRequired()], choices=GearType.get_choices())
    amplifier_type = SelectField('Тип услителя: ', [DataRequired()], choices=AmplifierType.get_choices())


