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
        light_units = self.light.get_equipment_consumption()
        ac_units = self.airconditioner.get_equipment_consumption()
        return light_units+ac_units
    