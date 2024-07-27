import json
import unittest
from unittest.mock import MagicMock

# Load the configuration from the JSON file
with open("odrive_config.json", "r") as f:
    config = json.load(f)

def apply_config(odrive, config):
    for key, value in config.items():
        if isinstance(value, dict):
            apply_config(getattr(odrive, key, MagicMock()), value)
        else:
            setattr(odrive, key, value)

class TestOdriveConfig(unittest.TestCase):

    def setUp(self):
        # Create a mock ODrive object
        self.odrv0 = MagicMock()

        # Apply the configuration using the mock ODrive device
        apply_config(self.odrv0, config)

    def test_motor_config(self):
        self.assertEqual(self.odrv0.axis0.motor.config.pole_pairs, 7)
        self.assertEqual(self.odrv0.axis0.motor.config.motor_type, "MOTOR_TYPE_HIGH_CURRENT")
        self.assertEqual(self.odrv0.axis0.motor.config.torque_constant, 0.1)
        self.assertEqual(self.odrv0.axis0.motor.config.current_lim, 50.0)
        self.assertEqual(self.odrv0.axis0.motor.config.calibration_current, 10.0)
        self.assertEqual(self.odrv0.axis0.motor.config.resistance_calib_max_voltage, 4.0)
        self.assertEqual(self.odrv0.axis0.motor.config.direction, 1)

    def test_controller_config(self):
        self.assertEqual(self.odrv0.axis0.controller.config.control_mode, 3)
        self.assertEqual(self.odrv0.axis0.controller.config.pos_gain, 1.0)
        self.assertEqual(self.odrv0.axis0.controller.config.vel_gain, 0.02)
        self.assertEqual(self.odrv0.axis0.controller.config.vel_integrator_gain, 0.1)
        self.assertEqual(self.odrv0.axis0.controller.config.vel_limit, 10.0)

    def test_encoder_config(self):
        self.assertEqual(self.odrv0.axis0.encoder.config.cpr, 8192)
        self.assertEqual(self.odrv0.axis0.encoder.config.mode, 0)

    def test_axis_config(self):
        self.assertEqual(self.odrv0.axis0.config.startup_motor_calibration, True)
        self.assertEqual(self.odrv0.axis0.config.startup_encoder_index_search, True)
        self.assertEqual(self.odrv0.axis0.config.startup_closed_loop_control, True)
        self.assertEqual(self.odrv0.axis0.config.startup_sensorless_control, False)

    def test_general_config(self):
        self.assertEqual(self.odrv0.config.dc_bus_overvoltage_trip_level, 56.0)
        self.assertEqual(self.odrv0.config.dc_bus_undervoltage_trip_level, 8.0)

if __name__ == '__main__':
    unittest.main()