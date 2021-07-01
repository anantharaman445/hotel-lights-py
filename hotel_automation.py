from Utils.floor_utils import create_floors
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
    
    def validate_power_consumption(self):
        return None