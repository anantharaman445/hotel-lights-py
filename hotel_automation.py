from Utils.floor_utils import create_floors, floor_movement_sub_corridor, change_ac_state_sub_corridor
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
    
    def movement_change(self, floor_id, sub_corridor_id, movement = hotel_management_constants["SENSORINPUT"]["MOVEMENT"]):
        """
        1. make default floor movement for any given subcorridor(change the light status)
        2. validate for power consumptions
        3. if power consumption exceeds expected and sensor type is MOVEMENT then turn the ac off in rest of the sub corridors until the consumption is within control
        """
        self.floor_map = floor_movement_sub_corridor(self.floor_map, floor_id, sub_corridor_id)
        sub_corridor_keys = list(self.floor_map[floor_id].floor_corridor_map["sub_corridors"].keys())
        expected_power_consumption = self.floor_map[floor_id].validate_power_consumption()
        
        sensor_inputs = hotel_management_constants["SENSORINPUT"]
        power_saver = sensor_inputs["POWER_SAVER"]

        # exceeded power usasge
        if not expected_power_consumption:
            if movement == hotel_management_constants["SENSORINPUT"]["MOVEMENT"] and power_saver == "AIRCONDITIONER":
                sub_corridor_keys.remove(sub_corridor_id)
                for key in range(0,len(sub_corridor_keys)):
                    # if not self.floor_map[floor_id].validate_power_consumption():
                    #TODO : need to confirm if above `IF` condition needs to be checked or we can switch off all the impacted sub corridors
                    self.floor_map = change_ac_state_sub_corridor(self.floor_map, floor_id, sub_corridor_keys[key])
                    self.floor_map[floor_id].non_movement_sub_corridors.append(sub_corridor_keys[key])

                return self.floor_map
        
        if movement == hotel_management_constants["SENSORINPUT"]["NO_MOVEMENT"] and power_saver == "AIRCONDITIONER":
            affected_sub_corridors = self.floor_map[floor_id].non_movement_sub_corridors
            for key in range(0,len(affected_sub_corridors)):
                self.floor_map = change_ac_state_sub_corridor(self.floor_map, floor_id, affected_sub_corridors[key])
        return self.floor_map



    def print_floor_states(self):
        for floor_id, floor in self.floor_map.items():
            print("::::Status of Floor {}::::".format(floor_id))
            main_corridors = floor.floor_corridor_map["main_corridors"]
            sub_corridors = floor.floor_corridor_map["sub_corridors"]

            for corridor_id, main_corridors in main_corridors.items():
                print(main_corridors.str_corridor_status(corridor_id))
            
            for corridor_id, sub_corridor in sub_corridors.items():
                print(sub_corridor.str_corridor_status(corridor_id))

