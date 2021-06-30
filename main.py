from Utils import utils
from Assets.maincorridor import MainCorridor 
from Assets.subcorridor import SubCorridor

hotel_management_constants = utils.hotel_management_constants

# light = Light()
# air_conditioner = AirConditioner()
# print(light.equipment_type, light.power_consumption, light.equipment_state)
# print(air_conditioner.equipment_type, air_conditioner.power_consumption, air_conditioner.equipment_state)

main_corridor = MainCorridor()
print(main_corridor.airconditioner.equipment_type, main_corridor.airconditioner.power_consumption)
print(main_corridor.corridor_type)