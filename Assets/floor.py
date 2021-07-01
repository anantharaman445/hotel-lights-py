from Utils import utils
from Assets.maincorridor import MainCorridor
from Assets.subcorridor import SubCorridor

corridor_type = utils.hotel_management_constants["CORRIDORTYPE"]

class Floor:
    def __init__(self, main_corridors_per_floor, sub_corridor_per_floor):
        self.total_main_corridors = main_corridors_per_floor
        self.total_sub_corridors = sub_corridor_per_floor
        self.floor_corridor_map = self.__create_corridors()
        self.maximum_allowed_units = (self.total_main_corridors * 15) + (self.total_sub_corridors * 10)

    # __ indicates private functions of the class
    def __create_corridors(self):
        self.floor_corridor_map = dict()
        self.__create_main_corridors()
        self.__create_sub_corridors()
        return self.floor_corridor_map


    def __create_main_corridors(self):
        self.floor_corridor_map["main_corridors"] = {}
        for i in range(0, self.total_main_corridors):
            self.floor_corridor_map["main_corridors"][i+1]=MainCorridor(corridor_type["MAINCORRIDOR"])
    
    def __create_sub_corridors(self):
        self.floor_corridor_map["sub_corridors"] = {}
        for i in range(0, self.total_sub_corridors):
            self.floor_corridor_map["sub_corridors"][i+1]=SubCorridor(corridor_type["SUBCORRIDOR"])

    def get_floor_equipment_units(self):
        units_consumptionn = 0
        main_corridors = self.floor_corridor_map["main_corridors"]
        sub_corridors  = self.floor_corridor_map["sub_corridors"]

        for corridor_id, main_corridor in main_corridors.items():
            units_consumptionn = units_consumptionn + main_corridor.compute_corridor_units()
        
        for corridor_id, sub_corridor in sub_corridors.items():
            units_consumptionn = units_consumptionn + sub_corridor.compute_corridor_units()

        return units_consumptionn
    
    def floor_time_slot_shift(self):
        main_corridors = self.floor_corridor_map["main_corridors"]
        for corridor_id, main_corridor in main_corridors.items():
            main_corridor.light.change_equipment_state() 
        