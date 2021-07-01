from Utils import utils
from Assets.corridor import Corridor



corridor_type = utils.hotel_management_constants["CORRIDORTYPE"]

equipment_state = utils.hotel_management_constants["EQUIPMENTSTATE"]

sensor_type = utils.hotel_management_constants["SENSORINPUT"]

time_slot = utils.hotel_management_constants["TIMESLOT"]



def get_coridor_units(corridor):
    units = 0
    if corridor.light.equipment_state == equipment_state["ON_STATE"]:
        units += 5
    if corridor.airconditioner.equipment_state == equipment_state["ON_STATE"]:
        units += 10
    return units
