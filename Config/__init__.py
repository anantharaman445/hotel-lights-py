import yaml
import json

with open('./Config/constants.yaml') as config:
    hotel_management_constants = yaml.safe_load(config)["HOTEL_MANAGEMENT"]
