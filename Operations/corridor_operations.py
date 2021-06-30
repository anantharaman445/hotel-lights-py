from Utils import utils
from Assets.corridor import Corridor

from Operations.equipment_operations import change_equipment_state


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


# def update_corridor_light_state(corridor):
#     corridor.light = change_equipment_state(corridor.light)
#     return corridor

# def update_corridor_airconditioner_state(corridor):
#     corridor.airconditioner = change_equipment_state(corridor.airconditioner)
#     return corridor