from Utils import utils
from Assets.corridor import Corridor

corridor_type = utils.hotel_management_constants["CORRIDORTYPE"]

class SubCorridor:
    def __init__(self):
        Corridor.__init__(self, corridor_type["SUBCORRIDOR"])
