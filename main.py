
from Operations.floor_operations import add_floors

from Operations.corridor_operations import time_slot

from Operations.equipment_operations import change_equipment_state

print(time_slot)

floor_m = add_floors(1, 1, 2)
print(floor_m)
floor = floor_m[1]
main_corridor = floor.floor_corridor_map["main_corridors"]
for key, value in main_corridor.items():

    print(value.airconditioner.equipment_type, value.airconditioner.power_consumption, value.airconditioner.equipment_state)

    value.airconditioner = change_equipment_state(value.airconditioner, "OFF")



    print(value.airconditioner.equipment_type, value.airconditioner.power_consumption, value.airconditioner.equipment_state)
