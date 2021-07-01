
from Operations.floor_operations import add_floors



floor_m = add_floors(1, 1, 2)
# print(floor_m)
floor = floor_m[1]
# print(floor.maximum_allowed_units)
print(floor.get_floor_equipment_units())


main_corridor = floor.floor_corridor_map["main_corridors"]
for key, value in main_corridor.items():
    print(value.light.equipment_type, value.light.equipment_state)
    print(value.airconditioner.equipment_type, value.airconditioner.equipment_state)


floor.floor_time_slot_shift()
for key, value in main_corridor.items():
    print(value.light.equipment_type, value.light.equipment_state)
    print(value.airconditioner.equipment_type, value.airconditioner.equipment_state)

print(floor.get_floor_equipment_units())

# main_corridor = floor.floor_corridor_map["main_corridors"]
# for key, value in main_corridor.items():

#     print(value.airconditioner.equipment_type, value.airconditioner.power_consumption, value.airconditioner.equipment_state)

#     value.airconditioner.change_equipment_state() 



#     print(value.airconditioner.equipment_type, value.airconditioner.power_consumption, value.airconditioner.equipment_state)
