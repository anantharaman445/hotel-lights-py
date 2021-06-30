from Utils import utils
from Equipments.airconditioner import AirConditioner 

hotel_management_constants = utils.hotel_management_constants

light = AirConditioner()
print(light.power_consumption)