from Utils import utils
from Equipments.light import Light
from Equipments.airconditioner import AirConditioner 
equipments = utils.hotel_management_constants["EQUIPMENTS"]

class Corridor:
    def __init__(self, corridor_type):
        self.light = Light(equipments["LIGHT"])
        self.airconditioner = AirConditioner(equipments["AIRCONDITIONER"])
        self.corridor_type = corridor_type
    
    def compute_corridor_units(self):
        total_units = 0
        light_units = total_units+ self.light.get_equipment_consumption()
        ac_units = total_units + self.airconditioner.get_equipment_consumption()
        return total_units
    