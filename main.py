

from hotel_automation import HotelAutomation as ha

yy = ha(2,1,2)
yy.time_slot_change()
yy.print_floor_states()
print("::Status after movement in Floor 1 and sub-corridor 2::")
yy.movement_change(1, 2)
yy.print_floor_states()
print("::Status after No movement in Floor 1 and sub-corridor 2::")
yy.movement_change(1, 2, "NO_MOVEMENT")
yy.print_floor_states()

#this is a dummy file to be removed