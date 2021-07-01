
from Assets.floor import Floor

def add_floors(no_of_floors, main_corridors_per_floor, sub_corridor_per_floor):
    floor_map = {}
    for i in range(0, no_of_floors):
        floor_map[i+1] = Floor(main_corridors_per_floor=main_corridors_per_floor, sub_corridor_per_floor=sub_corridor_per_floor)
    return floor_map

#  main_corridor.light.change_equipment_state() 
def validate_andmodify_consumption(floor_map, floor_id=0, sub_corridor_id=0):
    # for floor_id, floor in floor_map.items():

    pass