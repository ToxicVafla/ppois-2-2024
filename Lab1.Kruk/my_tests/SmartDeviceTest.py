from unittest import TestCase
from src.SmartDevice import SmartDevice


class TestSmartDevice(TestCase):
    def setUp(self):
        self.smart_device = SmartDevice("smart device 1")

    def test_init(self):
        self.assertIsInstance(self.smart_device, SmartDevice)
        self.assertMultiLineEqual(self.smart_device.name, "smart device 1")

    def test_switch_smart_device(self):
        self.smart_device.switch()
        self.assertTrue(self.smart_device.status)
        self.smart_device.switch()
        self.assertFalse(self.smart_device.status)

    def test_display_value(self):
        self.assertMultiLineEqual(self.smart_device.display_value(), "smart device 1 is not active")
        self.smart_device.switch()
        self.assertMultiLineEqual(self.smart_device.display_value(), "smart device 1 is active")
