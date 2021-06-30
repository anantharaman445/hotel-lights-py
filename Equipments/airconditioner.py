from Utils import utils
import json
from Equipments.equipments import Equipments

equipments = utils.hotel_management_constants["EQUIPMENTS"]


class AirConditioner:
    def __init__(self): 
        Equipments.__init__(self, equipments["AIRCONDITIONER"])
    