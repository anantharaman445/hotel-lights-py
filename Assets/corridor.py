from Utils import utils
from Equipments.light import Light
from Equipments.airconditioner import AirConditioner 

class Corridor:
    def __init__(self, corridor_type):
        self.light = Light()
        self.airconditioner = AirConditioner()
        self.corridor_type = corridor_type
    