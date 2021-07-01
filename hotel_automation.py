from Utils import utils, floor_utils
from Operations.floor_operations import add_floors


class HotelAutomation:
    def __init__(self, no_of_floors, main_corridors_per_floor, sub_corridor_per_floor):
        self.floor_map = add_floors(no_of_floors, main_corridors_per_floor, sub_corridor_per_floor)
