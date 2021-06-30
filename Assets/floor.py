from Utils import utils
from Assets.maincorridor import MainCorridor
from Assets.subcorridor import SubCorridor

corridor_type = utils.hotel_management_constants["CORRIDORTYPE"]

class Floor:
    def __init__(self, main_corridors_per_floor, sub_corridor_per_floor):
        self.total_main_corridors = main_corridors_per_floor
        self.total_sub_corridors = sub_corridor_per_floor
        self.floor_map = self.get_corridors()

    def get_corridors(self):
        self.floor_map = dict()
        self.get_main_corridors()
        self.get_sub_corridors()
        return self.floor_map


    def get_main_corridors(self):
        self.floor_map["main_corridors"] = {}
        for i in range(0, self.total_main_corridors):
            self.floor_map["main_corridors"][i]=MainCorridor()
    
    def get_sub_corridors(self):
        self.floor_map["sub_corridors"] = {}
        for i in range(0, self.total_sub_corridors):
            self.floor_map["sub_corridors"][i]=SubCorridor()
