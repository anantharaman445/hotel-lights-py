from Utils import utils
from Assets.corridor import Corridor

corridor_type = utils.hotel_management_constants["CORRIDORTYPE"]

equipment_state = utils.hotel_management_constants["EQUIPMENTSTATE"]

class MainCorridor:
    def __init__(self):
        Corridor.__init__(self, corridor_type["MAINCORRIDOR"])

    def compute_corridor_units(self):
        light_units = self.light.get_equipment_consumption()
        ac_units = self.airconditioner.get_equipment_consumption()
        return light_units+ac_units
