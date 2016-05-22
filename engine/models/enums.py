class BaseEnum(object):
    values = {}

    @classmethod
    def get_choices(cls):
        return cls.values.items()


class GearingType(BaseEnum):
    PA = 1
    PP = 2
    RP = 3
    PS = 4

    values = {
        PA:'приводы антенн радиолокаторов',
        PP:'приводы стабилизированных приборных платформ',
        RP:'рулевые приводы',
        PS:'приводы стабилизированной скорости вращения скани­рующих и '
           'лентопротяжных устройств',
    }


class GearType(BaseEnum):
    GearWheels = 1
    SpiralGear = 2
    CombinedGear = 3

    values = {
        GearWheels:'Зубчатая передача',
        SpiralGear:'Винтовая передача',
        CombinedGear:'Комбинированная передача',
    }

class AmplifierType(BaseEnum):
    Thyristor = 1
    Transistor = 2

    values = {
        Transistor:'Транзисторный',
        Thyristor:'Тиристорный',
    }