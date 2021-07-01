
from Assets.floor import Floor
from Utils import utils
from Operations.corridor_operations import get_coridor_units

time_slot = utils.hotel_management_constants["TIMESLOT"]

equipment_state = utils.hotel_management_constants["EQUIPMENTSTATE"]


def add_floors(no_of_floors, main_corridors_per_floor, sub_corridor_per_floor):
    floor_map = {}
    for i in range(0, no_of_floors):
        floor_map[i+1] = Floor(main_corridors_per_floor=main_corridors_per_floor, sub_corridor_per_floor=sub_corridor_per_floor)
    return floor_map
"""
floor_map = {1 : <floor> }
floor_corridor_map = floor.floor_corridor_map
floor_corridor_map = {"main_corridors" : main_corridor_map}
main_corridor_map = {<main-corridor-id> : <corridor>}
corridor = object = obj.airconditioner, obj.light
light.type, powerconsumptionn, state
    print(value.airconditioner.equipment_type, value.airconditioner.power_consumption, value.airconditioner.equipment_state)

1. check units_consumptionn for every shift roaster
2. check units_consumptionn for every movement
"""
# move this to corridor ops
def get_floor_equipment_units(floor):
    units_consumptionn = 0
    main_corridors = floor.floor_corridor_map["main_corridors"]
    sub_corridors  = floor.floor_corridor_map["sub_corridors"]

    for corridor_id, main_corridor in main_corridors.items():
        units_consumptionn = units_consumptionn + get_coridor_units(main_corridor)
    
    for corridor_id, sub_corridor in sub_corridors.items():
        units_consumptionn = units_consumptionn + get_coridor_units(sub_corridor)

    return units_consumptionn

def regular_shift_roaster(floor):
    # just turn off and turn on lights of main corridor of a floor based on shift
    
    main_corridors = floor.floor_corridor_map["main_corridors"]
    for corridor_id, main_corridor in main_corridors.items():
        main_corridor.light.change_equipment_state() 
    
    return floor



