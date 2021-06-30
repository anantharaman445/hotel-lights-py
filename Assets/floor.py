from Utils import utils
from Assets.maincorridor import MainCorridor
from Assets.subcorridor import SubCorridor

corridor_type = utils.hotel_management_constants["CORRIDORTYPE"]

class Floor:
    def __init__(self, main_corridors_per_floor, sub_corridor_per_floor):
        self.total_main_corridors = main_corridors_per_floor
        self.total_sub_corridors = sub_corridor_per_floor
        self.floor_corridor_map = self.__get_corridors()
        self.maximum_allowed_units = (self.total_main_corridors * 15) + (self.total_sub_corridors * 10)

    # __ indicates private functions of the class
    def __get_corridors(self):
        self.floor_corridor_map = dict()
        self.__get_main_corridors()
        self.__get_sub_corridors()
        return self.floor_corridor_map


    def __get_main_corridors(self):
        self.floor_corridor_map["main_corridors"] = {}
        for i in range(0, self.total_main_corridors):
            self.floor_corridor_map["main_corridors"][i]=MainCorridor()
    
    def __get_sub_corridors(self):
        self.floor_corridor_map["sub_corridors"] = {}
        for i in range(0, self.total_sub_corridors):
            self.floor_corridor_map["sub_corridors"][i]=SubCorridor()
