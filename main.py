from Utils import utils
from Equipments.light import Light 
from Equipments.airconditioner import AirConditioner 

hotel_management_constants = utils.hotel_management_constants

light = Light()
ait_conditioner = AirConditioner()
print(light.equipment_type, light.power_consumption)
print(ait_conditioner.equipment_type, ait_conditioner.power_consumption)