from Utils import utils
import json
equipment_state = utils.hotel_management_constants["EQUIPMENTSTATE"]

class Equipments:
    def __init__(self, equipment):
        self.equipment_type = equipment["TYPE"]
        self.power_consumption = equipment["POWER_CONSUMPTION"]
        self.equipment_state = equipment["DEFAULT_STATE"]
    
