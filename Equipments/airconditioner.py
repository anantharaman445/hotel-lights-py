from Utils import utils
import json


hotel_management_constants = utils.hotel_management_constants["EQUIPMENTS"]["AIRCONDITIONER"]

class AirConditioner:
    def __init__(self):
        self.equipment_type = hotel_management_constants["TYPE"]
        self.power_consumption = hotel_management_constants["POWER_CONSUMPTION"]
        
