from unittest import TestCase
from src.SmartHome import SmartHome
from src.SecuritySystem import SecuritySystem
from src.SmartHome import SmartDevice
from datetime import datetime, time


class TestSmartHome(TestCase):
    def setUp(self):
        self.smart_device = SecuritySystem("camera 1", "breakIn", 2)
        self.not_security_smart_device = SmartDevice("smart device 1")

    def test_schedules(self):
        my_home_1 = SmartHome([])
        my_home_1.add_smart_device(self.smart_device)
        self.assertFalse(my_home_1.display_schedules())
        my_home_1.create_schedule("camera 1", time(1, 50))
        my_home_1.create_schedule("camera 1", time(1, 55))
        self.assertTrue(my_home_1.display_schedules())
        my_home_1.run_schedules()