from Utils.floor_utils import create_floors, floor_movement_sub_corridor
from Config import hotel_management_constants

class HotelAutomation:
    def __init__(self, no_of_floors, main_corridors_per_floor, sub_corridor_per_floor):
        self.floor_map = create_floors(no_of_floors, main_corridors_per_floor, sub_corridor_per_floor)
        self.time_slot = hotel_management_constants["TIMESLOT"]["DAY"]

    def time_slot_change(self):
        if self.time_slot == hotel_management_constants["TIMESLOT"]["DAY"]:
             self.time_slot = hotel_management_constants["TIMESLOT"]["NIGHT"]
        else:
            self.time_slot = hotel_management_constants["TIMESLOT"]["DAY"]
        
        for floor_id, floor in self.floor_map.items():
            floor.floor_time_slot_shift()
    
    def movement_change(self, floor_id, sub_corridor_id):
        self.floor_map = floor_movement_sub_corridor(self.floor_map, floor_id, sub_corridor_id)


    def print_floor_states(self):
        for floor_id, floor in self.floor_map.items():
            print("::::States of Floor {}::::".format(floor_id))
            main_corridors = floor.floor_corridor_map["main_corridors"]
            sub_corridors = floor.floor_corridor_map["sub_corridors"]

            for corridor_id, main_corridors in main_corridors.items():
                print(main_corridors.str_corridor_status(corridor_id))
            
            for corridor_id, sub_corridor in sub_corridors.items():
                print(sub_corridor.str_corridor_status(corridor_id))

