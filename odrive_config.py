import json
import odrive
from odrive.enums import *

# load config values from json file
with open("odrive_config.json", "r") as f:
    config = json.load(f)

def apply_config(odrive, config):
    for key, value in config.items():
        if isinstance(value, dict):
            apply_config(getattr(odrive, key, None), value)
        else:
            setattr(odrive, key, value)

# Find ODrive
odrv0 = odrive.find_any()
``
# Call func to apply config using actual device
apply_config(odrv0, config)

# Printing applied configuration to check if correct values set
print(odrv0.axis0.motor.config.pole_pairs)  # Should print 7
print(odrv0.axis0.motor.config.motor_type)  # Should print "MOTOR_TYPE_HIGH_CURRENT"
print(odrv0.config.dc_bus_overvoltage_trip_level)  # Should print 56.0
print(odrv0.config.dc_bus_undervoltage_trip_level)  # Should print 8.0