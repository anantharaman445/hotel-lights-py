from Utils import utils
from Equipments.equipments import Equipments


def change_equipment_state(equipment, state):
    equipment.equipment_state = state
    return equipment