class BaseEnum(object):
    values = {}

    @classmethod
    def get_choices(cls):
        return cls.values.items()


class GearingType(BaseEnum):
    PA = 0
    PP = 1
    RP = 2
    PS = 3

    values = {
        PA:'приводы антенн радиолокаторов',
        PP:'приводы стабилизированных приборных платформ',
        RP:'рулевые приводы',
        PS:'приводы стабилизированной скорости вращения скани­рующих и '
           'лентопротяжных устройств',
    }


class GearType(BaseEnum):
    GearWheels = 0
    SpiralGear = 1
    CombinedGear = 2

    values = {
        GearWheels:'Зубчатая передача',
        SpiralGear:'Винтовая передача',
        CombinedGear:'Комбинированная передача',
    }

class AmplifierType(BaseEnum):
    Thyristor = 0
    Transistor = 1

    values = {
        Transistor:'Транзисторный',
        Thyristor:'Тиристорный',
    }