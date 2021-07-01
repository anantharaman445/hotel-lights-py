from Utils import utils
import json
equipment_state = utils.hotel_management_constants["EQUIPMENTSTATE"]

class Equipments:
    def __init__(self, equipment):
        self.equipment_type = equipment["TYPE"]
        self.power_consumption = equipment["POWER_CONSUMPTION"]
        self.equipment_state = equipment["DEFAULT_STATE"]
    

    def change_equipment_state_n(self):
        if self.equipment_state == equipment_state["ON_STATE"]:
            self.equipment_state = equipment_state["OFF_STATE"]
        else:
            self.equipment_state = equipment_state["ON_STATE"]

