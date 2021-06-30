
from Assets.floor import Floor
from Utils import utils
from Operations.corridor_operations import get_coridor_units, update_corridor_light_state, update_corridor_airconditioner_state

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

"""

def get_floor_equipment_units(floor):
    cost = 0
    main_corridors = floor.floor_corridor_map["main_corridors"]
    sub_corridors  = floor.floor_corridor_map["sub_corridors"]

    for corridor_id, main_corridor in main_corridors.items():
        cost = cost + get_coridor_units(main_corridor)
    
    for corridor_id, sub_corridor in sub_corridors.items():
        cost = cost + get_coridor_units(sub_corridor)

    return cost

def switch_floor_equipments(floor, slor, switch_type="default"):
    main_corridors = floor.floor_corridor_map["main_corridors"]
    sub_corridors  = floor.floor_corridor_map["sub_corridors"]
    
    if switch_type == "default" and slot == time_slot["NIGHT"]:
        for corridor_id, main_corridor in main_corridors.items():
            main_corridors[corridor_id] = update_corridor_light_state(main_corridor, equipment_state["ON_STATE"])

        
    



    return 0

