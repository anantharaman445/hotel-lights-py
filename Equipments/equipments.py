from Utils import utils
import json


class Equipments:
    def __init__(self, equipment):
        self.equipment_type = equipment["TYPE"]
        self.power_consumption = equipment["POWER_CONSUMPTION"]