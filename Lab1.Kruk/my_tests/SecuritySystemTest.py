from unittest import TestCase
from src.SecuritySystem import SecuritySystem
from src.SmartDevice import SmartDevice
import time


class TestSecuritySystem(TestCase):
    def setUp(self):
        self.smart_device = SecuritySystem("camera 1", "breakIn", 2)

    def test_init(self):
        self.assertIsInstance(self.smart_device, SmartDevice)
        self.assertIsInstance(self.smart_device, SecuritySystem)
        self.assertMultiLineEqual(self.smart_device.name, "camera 1")
        self.assertMultiLineEqual(self.smart_device.device_type, "breakIn")
        self.assertEqual(self.smart_device.covering_area, 2)

    def test_charge(self):
        self.assertEqual(self.smart_device.charge_value, 20)
        self.smart_device.charge()
        self.assertGreaterEqual(self.smart_device.charge_value, 91)

    def test_security_check(self):
        self.assertEqual(self.smart_device.security_check(), "Don't forget to turn on camera 1")

    def test_alarm(self):
        self.smart_device.switch()
        self.assertMultiLineEqual(self.smart_device.alarm(), "Alarm. Police called!")
        self.assertMultiLineEqual(self.smart_device.alarm(), "Alarm. Police called! Ambulance called!")
        self.smart_device.switch()
        self.assertMultiLineEqual(self.smart_device.alarm(), "Don't forget to turn on camera 1")
        self.assertMultiLineEqual(self.smart_device.alarm(), "Don't forget to turn on camera 1")

    def test_display_value(self):
        self.assertMultiLineEqual(self.smart_device.display_value(), "camera 1 is not active; charge value is 20%")
        self.smart_device.switch()
        self.assertMultiLineEqual(self.smart_device.display_value(), "camera 1 is active; charge value is 20%")