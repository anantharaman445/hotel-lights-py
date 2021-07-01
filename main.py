

from hotel_automation import HotelAutomation as ha

yy = ha(1,1,2)
# yy.print_floor_states()
yy.time_slot_change()
yy.print_floor_states()
yy.movement_change(1, 2)
yy.print_floor_states()
yy.movement_change(1, 2, "NO_MOVEMENT")
yy.print_floor_states()
