
from Assets.floor import Floor
from Utils import utils

time_slot = utils.hotel_management_constants["TIMESLOT"]


def add_floors(no_of_floors, main_corridors_per_floor, sub_corridor_per_floor):
    floor_map = {}
    for i in range(0, no_of_floors):
        floor_map[i+1] = Floor(main_corridors_per_floor=main_corridors_per_floor, sub_corridor_per_floor=sub_corridor_per_floor)
    return floor_map


def get_floor_cost(floor, time_slot):
    cost = 0
    return cost

