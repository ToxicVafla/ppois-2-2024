from unittest import TestCase
from src.SmartHome import SmartHome
from src.SecuritySystem import SecuritySystem
from src.SmartHome import SmartDevice
from datetime import datetime, time


class TestSmartHome(TestCase):
    def setUp(self):
        self.my_home = SmartHome([])
        self.smart_device = SecuritySystem("camera 1", "breakIn", 2)
        self.not_security_smart_device = SmartDevice("smart device 1")

    def test_init(self):
        self.assertIsInstance(self.my_home, SmartHome)
        self.assertListEqual(self.my_home.devices, [])

    def test_add_smart_device(self):
        self.my_home.add_smart_device(self.smart_device)
        self.assertListEqual(self.my_home.devices, [self.smart_device])
        self.assertListEqual(self.my_home.security_systems, [self.smart_device])
        self.my_home.add_smart_device(self.not_security_smart_device)
        self.assertListEqual(self.my_home.devices, [self.smart_device, self.not_security_smart_device])
        self.assertListEqual(self.my_home.security_systems, [self.smart_device])

    def test_list_devices(self):
        self.assertFalse(self.my_home.list_devices())
        self.my_home.add_smart_device(self.smart_device)
        self.my_home.add_smart_device(self.not_security_smart_device)
        self.assertTrue(self.my_home.list_devices())
