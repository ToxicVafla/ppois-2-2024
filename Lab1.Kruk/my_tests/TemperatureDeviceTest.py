from unittest import TestCase
from src.TemperatureDevice import TemperatureDevice
from src.SmartDevice import SmartDevice


class TestTemperatureDevice(TestCase):
    def setUp(self):
        self.smart_device = TemperatureDevice("oil radiator")

    def test_init(self):
        self.assertIsInstance(self.smart_device, SmartDevice)
        self.assertIsInstance(self.smart_device, TemperatureDevice)

    def test_display_value(self):
        self.assertMultiLineEqual(self.smart_device.display_value(), "oil radiator is not active; temperature is 20 "
                                                                     "degrees Celsius")
        self.smart_device.switch()
        self.assertMultiLineEqual(self.smart_device.display_value(), "oil radiator is active; temperature is 20 "
                                                                     "degrees Celsius")

    def test_set_temperature(self):
        self.smart_device.switch()
        self.assertTrue(self.smart_device.set_temperature(18))
        self.assertMultiLineEqual(self.smart_device.display_value(), "oil radiator is active; temperature is 18 "
                                                                     "degrees Celsius")
        self.smart_device.switch()
        self.smart_device.set_temperature(20)
        self.assertFalse(self.smart_device.set_temperature(20))
        self.assertMultiLineEqual(self.smart_device.display_value(), "oil radiator is not active; temperature is 18 "
                                                                     "degrees Celsius")
