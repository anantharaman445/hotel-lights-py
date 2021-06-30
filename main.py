from Utils import utils
from Equipments.light import Light 
from Equipments.airconditioner import AirConditioner 

hotel_management_constants = utils.hotel_management_constants

light = Light()
air_conditioner = AirConditioner()
print(light.equipment_type, light.power_consumption, light.equipment_state)
print(air_conditioner.equipment_type, air_conditioner.power_consumption, air_conditioner.equipment_state)