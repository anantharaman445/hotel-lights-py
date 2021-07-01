import unittest
import json
from Config import hotel_management_constants as constants


from hotel_automation import HotelAutomation as ha

class TestHotel(unittest.TestCase):

    def test_time_slot(self):
        hotel = ha(1,1,2)
        self.assertEqual(hotel.time_slot, constants["TIMESLOT"]["DAY"])
        hotel.time_slot_change()
        self.assertNotEqual(hotel.time_slot, constants["TIMESLOT"]["DAY"])
        self.assertEqual(hotel.time_slot, constants["TIMESLOT"]["NIGHT"])
        

if __name__ == "__main__":
    unittest.main()