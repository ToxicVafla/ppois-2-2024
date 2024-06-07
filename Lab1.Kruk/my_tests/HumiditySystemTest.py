from unittest import TestCase
from src.HumiditySystem import HumiditySystem
from src.SmartDevice import SmartDevice


class TestHumiditySystem(TestCase):
    def setUp(self):
        self.smart_device = HumiditySystem("humidifier")

    def test_init(self):
        self.assertIsInstance(self.smart_device, SmartDevice)
        self.assertIsInstance(self.smart_device, HumiditySystem)

    def test_display_value(self):
        self.assertMultiLineEqual(self.smart_device.display_value(), "humidifier is not active; humidity is 40%")
        self.smart_device.switch()
        self.assertMultiLineEqual(self.smart_device.display_value(), "humidifier is active; humidity is 40%")

    def test_set_temperature(self):
        self.smart_device.switch()
        self.assertTrue(self.smart_device.set_humidity(60))
        self.assertMultiLineEqual(self.smart_device.display_value(), "humidifier is active; humidity is 60%")
        self.smart_device.switch()
        self.smart_device.set_humidity(50)
        self.assertFalse(self.smart_device.set_humidity(50))
        self.assertMultiLineEqual(self.smart_device.display_value(), "humidifier is not active; humidity is 60%")
