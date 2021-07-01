from Config import hotel_management_constants
from Equipments.light import Light
from Equipments.airconditioner import AirConditioner 
equipments = hotel_management_constants["EQUIPMENTS"]

class Corridor:
    def __init__(self, corridor_type):
        self.light = Light(equipments["LIGHT"])
        self.airconditioner = AirConditioner(equipments["AIRCONDITIONER"])
        self.corridor_type = corridor_type
    
    def compute_corridor_units(self):
        total_units = 0
        total_units = total_units + self.light.get_equipment_consumption()
        total_units = total_units + self.airconditioner.get_equipment_consumption()
        return total_units
    