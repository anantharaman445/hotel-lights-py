from Config import hotel_management_constants
import json
equipment_state = hotel_management_constants["EQUIPMENTSTATE"]

class Equipments:
    def __init__(self, equipment):
        self.equipment_type = equipment["TYPE"]
        self.power_consumption = equipment["POWER_CONSUMPTION"]
        self.equipment_state = equipment["DEFAULT_STATE"]
        self.power_consumption_off_state = 0
    
    def change_equipment_state(self):
        if self.equipment_state == equipment_state["ON_STATE"]:
            self.equipment_state = equipment_state["OFF_STATE"]
        else:
            self.equipment_state = equipment_state["ON_STATE"]
    
    def get_equipment_consumption(self):
        if self.equipment_state == equipment_state["ON_STATE"]:
            return self.power_consumption
        else:
            return self.power_consumption_off_state