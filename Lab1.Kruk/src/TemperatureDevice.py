from src.SmartDevice import SmartDevice
from src.Exceptions import DeviceIsNotActiveException


class TemperatureDevice(SmartDevice):
    temperature = 20

    def set_temperature(self, temperature):
        try:
            if self.status:
                self.temperature = temperature
                print(self.name, "temperature set to", self.temperature)
                return True
            else:
                raise DeviceIsNotActiveException("Device is not active")
        except DeviceIsNotActiveException:
            return False

    def display_value(self):
        print(f"{super().display_value()}; temperature is {self.temperature} degrees Celsius")
        return f"{super().display_value()}; temperature is {self.temperature} degrees Celsius"
