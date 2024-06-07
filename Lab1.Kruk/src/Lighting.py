from src.SmartDevice import SmartDevice
from src.Exceptions import DeviceIsNotActiveException


class Lighting(SmartDevice):
    brightness_percentage = 100

    def set_brightness(self, percentage):
        try:
            if self.status:
                self.brightness_percentage = percentage
                print(self.name, "brightness set to", percentage)
                return True
            else:
                raise DeviceIsNotActiveException("Device is not active")
        except DeviceIsNotActiveException:
            return False

    def display_value(self):
        print(f"{super().display_value()}; brightness is {self.brightness_percentage}%")
        return f"{super().display_value()}; brightness is {self.brightness_percentage}%"
