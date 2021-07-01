
# from Utils.floor_utils import add_floors


from hotel_automation import HotelAutomation as ha

yy = ha(1,1,2)

print(yy.floor_map[1].get_floor_equipment_units())

yy.time_slot_change()

print(yy.floor_map[1].get_floor_equipment_units())
 
