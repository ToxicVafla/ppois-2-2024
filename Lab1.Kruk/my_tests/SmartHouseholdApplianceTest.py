from unittest import TestCase
from src.SmartHouseholdAppliance import SmartHouseholdAppliance
from src.SmartDevice import SmartDevice


class TestSmartHouseholdAppliance(TestCase):
    def setUp(self):
        self.smart_device = SmartHouseholdAppliance("coffe machine", "food", ["latte", "espresso"])

    def test_init(self):
        self.assertIsInstance(self.smart_device, SmartDevice)
        self.assertIsInstance(self.smart_device, SmartHouseholdAppliance)
        self.assertMultiLineEqual(self.smart_device.name, "coffe machine")
        self.assertMultiLineEqual(self.smart_device.type, "food")
        self.assertListEqual(self.smart_device.documentation, ["latte", "espresso"])

    def test_work(self):
        self.smart_device.switch()
        self.assertMultiLineEqual(self.smart_device.work(), "latte is done")
        self.assertMultiLineEqual(self.smart_device.work(), "process canceled, no such object in documentation")
        self.smart_device.switch()
        self.assertMultiLineEqual(self.smart_device.work(), "Turn on device to use it!")
