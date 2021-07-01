from Utils import utils
import json
from Equipments.equipments import Equipments

equipments = utils.hotel_management_constants["EQUIPMENTS"]
equipment_state = utils.hotel_management_constants["EQUIPMENTSTATE"]

class AirConditioner:
    def __init__(self): 
        Equipments.__init__(self, equipments["AIRCONDITIONER"])
    

    def change_equipment_state_n(self):
        if self.equipment_state == equipment_state["ON_STATE"]:
            self.equipment_state = equipment_state["OFF_STATE"]
        else:
            self.equipment_state = equipment_state["ON_STATE"]
    
    def get_equipment_consumption(self):
        if self.equipment_state == equipment_state["ON_STATE"]:
            return self.power_consumption
        else:
            return self.power_consumption_off_state
