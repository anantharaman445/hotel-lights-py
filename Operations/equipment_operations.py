from Utils import utils
from Equipments.equipments import Equipments

equipment_state = utils.hotel_management_constants["EQUIPMENTSTATE"]

def change_equipment_state(equipment):
    if equipment.equipment_state == equipment_state["ON_STATE"]:
        equipment.equipment_state = equipment_state["OFF_STATE"]
    else:
        equipment.equipment_state = equipment_state["ON_STATE"]
    return equipment