from unittest import TestCase
from src.Lighting import Lighting
from src.SmartDevice import SmartDevice


class TestLighting(TestCase):
    def setUp(self):
        self.smart_device = Lighting("light bulb 1")

    def test_init(self):
        self.assertIsInstance(self.smart_device, SmartDevice)
        self.assertIsInstance(self.smart_device, Lighting)

    def test_display_value(self):
        self.assertMultiLineEqual(self.smart_device.display_value(), "light bulb 1 is not active; brightness is 100%")
        self.smart_device.switch()
        self.assertMultiLineEqual(self.smart_device.display_value(), "light bulb 1 is active; brightness is 100%")

    def test_set_temperature(self):
        self.smart_device.switch()
        self.assertTrue(self.smart_device.set_brightness(50))
        self.assertMultiLineEqual(self.smart_device.display_value(), "light bulb 1 is active; brightness is 50%")
        self.smart_device.switch()
        self.smart_device.set_brightness(70)
        self.assertFalse(self.smart_device.set_brightness(70))
        self.assertMultiLineEqual(self.smart_device.display_value(), "light bulb 1 is not active; brightness is 50%")
