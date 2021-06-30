
from Assets.floor import Floor
from Utils import utils

time_slot = utils.hotel_management_constants["TIMESLOT"]


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

def get_floor_running_units(floor, time_slot):
    cost = 0
    main_corridors_len

    return cost

