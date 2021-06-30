
from Operations.floor_operations import add_floors, get_floor_equipment_units

from Operations.corridor_operations import time_slot

from Operations.equipment_operations import change_equipment_state

# print(time_slot)

floor_m = add_floors(1, 1, 2)
# print(floor_m)
floor = floor_m[1]
# print(floor.maximum_allowed_chargable_units)
print(get_floor_equipment_units(floor))

# main_corridor = floor.floor_corridor_map["main_corridors"]
# for key, value in main_corridor.items():

#     print(value.airconditioner.equipment_type, value.airconditioner.power_consumption, value.airconditioner.equipment_state)

#     value.airconditioner = change_equipment_state(value.airconditioner, "OFF")



#     print(value.airconditioner.equipment_type, value.airconditioner.power_consumption, value.airconditioner.equipment_state)

class HotelLights:
    def __init__(self, no_of_floors, no_of_main_corridors, no_of_sub_corridors):
        self.floors_map = add_floors(no_of_floors, no_of_main_corridors, no_of_sub_corridors)
    
    # def switch_time_slot(self, time_slot):
    #     for floor_id, floor in self.floors_map:

    #     return None
    