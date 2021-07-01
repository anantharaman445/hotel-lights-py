

from hotel_automation import HotelAutomation as ha

yy = ha(1,1,2)
yy.print_floor_states()
yy.time_slot_change()
yy.print_floor_states()
yy.movement_change(1, 2)
yy.print_floor_states()
yy.movement_change(1, 2)
yy.print_floor_states()

# print(yy.floor_map[1].get_floor_equipment_units(), yy.floor_map[1].maximum_allowed_units)

# print(yy.time_slot)
# yy.time_slot_change()
# print(yy.time_slot)
# print(yy.floor_map[1].get_floor_equipment_units(), yy.floor_map[1].maximum_allowed_units, yy.floor_map[1].validate_power_consumption())

# yy.floor_map[1].change_sub_corridor_light_state(1)
# print(yy.floor_map[1].get_floor_equipment_units(), yy.floor_map[1].maximum_allowed_units, yy.floor_map[1].validate_power_consumption())

# yy.floor_map[1].change_sub_corridor_ac_state(1)
# print(yy.floor_map[1].get_floor_equipment_units(), yy.floor_map[1].maximum_allowed_units, yy.floor_map[1].validate_power_consumption())

 
# print(yy.time_slot)
# yy.time_slot_change()
# print(yy.time_slot)
# print(yy.floor_map[1].get_floor_equipment_units(), yy.floor_map[1].maximum_allowed_units, yy.floor_map[1].validate_power_consumption())