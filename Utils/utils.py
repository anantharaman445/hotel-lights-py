import yaml
import json

with open('constants.yaml') as config:
    cons = yaml.safe_load(config)

hotel_management_constants = cons["HOTEL_MANAGEMENT"]