
from Assets.floor import Floor

def create_floors(no_of_floors, main_corridors_per_floor, sub_corridor_per_floor):
    floor_map = {}
    for i in range(0, no_of_floors):
        floor_map[i+1] = Floor(main_corridors_per_floor=main_corridors_per_floor, sub_corridor_per_floor=sub_corridor_per_floor)
    return floor_map

def floor_movement_sub_corridor(floor_map, floor_id, sub_corridor_id):
    floor_map[floor_id].change_sub_corridor_light_state(sub_corridor_id)
    return floor_map

def change_ac_state_sub_corridor(floor_map, floor_id, sub_corridor_id):
    floor_map[floor_id].change_sub_corridor_ac_state(sub_corridor_id)
    return floor_map


