import unittest
import json
from Config import hotel_management_constants as constants


from hotel_automation import HotelAutomation as ha

class TestHotel(unittest.TestCase):
    # NOTE : in all test cases slot changed will be invoked first since the slot will be changed to night by default while creating it will be day
    def test_time_slot(self):
        hotel = ha(1,1,2)
        self.assertEqual(hotel.time_slot, constants["TIMESLOT"]["DAY"])
        hotel.time_slot_change()
        self.assertNotEqual(hotel.time_slot, constants["TIMESLOT"]["DAY"])
        self.assertEqual(hotel.time_slot, constants["TIMESLOT"]["NIGHT"])
    
    def test_main_corridor_time_slot(self):
        hotel = ha(1,1,2)
        main_corridor = hotel.floor_map[1].floor_corridor_map["main_corridors"][1]
        self.assertEqual(main_corridor.light.equipment_state , constants["EQUIPMENTSTATE"]["OFF_STATE"])
        self.assertEqual(hotel.time_slot, constants["TIMESLOT"]["DAY"])

        hotel.time_slot_change()
        self.assertEqual(hotel.time_slot, constants["TIMESLOT"]["NIGHT"])        
        self.assertEqual(main_corridor.light.equipment_state , constants["EQUIPMENTSTATE"]["ON_STATE"])
        self.assertEqual(main_corridor.airconditioner.equipment_state , constants["EQUIPMENTSTATE"]["ON_STATE"])

    def test_sub_corridor_time_slot(self):
        hotel = ha(1,1,2)
        main_corridor = hotel.floor_map[1].floor_corridor_map["main_corridors"][1]
        sub_corridor = hotel.floor_map[1].floor_corridor_map["sub_corridors"][1]
        

        hotel.time_slot_change()
        self.assertEqual(hotel.time_slot, constants["TIMESLOT"]["NIGHT"])        
        self.assertEqual(sub_corridor.light.equipment_state , constants["EQUIPMENTSTATE"]["OFF_STATE"])
    
    def test_sub_corridor_movement_slot(self):
        hotel = ha(1,1,2)
        main_corridor = hotel.floor_map[1].floor_corridor_map["main_corridors"][1]
        movement_sub_corridor = hotel.floor_map[1].floor_corridor_map["sub_corridors"][2]
        impacted_sub_corridor  = hotel.floor_map[1].floor_corridor_map["sub_corridors"][1]

        hotel.time_slot_change()
        self.assertEqual(hotel.time_slot, constants["TIMESLOT"]["NIGHT"])        
        self.assertEqual(movement_sub_corridor.light.equipment_state , constants["EQUIPMENTSTATE"]["OFF_STATE"])
        self.assertEqual(impacted_sub_corridor.airconditioner.equipment_state , constants["EQUIPMENTSTATE"]["ON_STATE"])
        self.assertEqual(movement_sub_corridor.airconditioner.equipment_state , constants["EQUIPMENTSTATE"]["ON_STATE"])
  
        hotel.movement_change(1, 2)
        self.assertEqual(movement_sub_corridor.light.equipment_state , constants["EQUIPMENTSTATE"]["ON_STATE"])
        self.assertEqual(movement_sub_corridor.airconditioner.equipment_state , constants["EQUIPMENTSTATE"]["ON_STATE"])
        self.assertEqual(impacted_sub_corridor.airconditioner.equipment_state , constants["EQUIPMENTSTATE"]["OFF_STATE"])

        hotel.movement_change(1, 2, "NO_MOVEMENT")
        self.assertEqual(movement_sub_corridor.light.equipment_state , constants["EQUIPMENTSTATE"]["OFF_STATE"])
        self.assertEqual(movement_sub_corridor.airconditioner.equipment_state , constants["EQUIPMENTSTATE"]["ON_STATE"])
        self.assertEqual(impacted_sub_corridor.airconditioner.equipment_state , constants["EQUIPMENTSTATE"]["ON_STATE"])

        

if __name__ == "__main__":
    unittest.main()