
from Assets.corridor import Corridor

class SubCorridor(Corridor):
   
    def change_sub_corridor_light_state(self):
        self.light.change_equipment_state()
    
    def change_sub_corridor_airconditioner_state(self):
        self.airconditioner.change_equipment_state()

