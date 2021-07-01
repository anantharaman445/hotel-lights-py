from Utils.floor_utils import add_floors


class HotelAutomation:
    def __init__(self, no_of_floors, main_corridors_per_floor, sub_corridor_per_floor):
        self.floor_map = add_floors(no_of_floors, main_corridors_per_floor, sub_corridor_per_floor)

    def time_slot_change(self):
        for floor_id, floor in self.floor_map.items():
            floor.floor_time_slot_shift()
    