from src.SmartDevice import SmartDevice
from src.Exceptions import DeviceIsNotActiveException


class HumiditySystem(SmartDevice):
    humidity = 40

    def set_humidity(self, humidity):
        try:
            if self.status:
                self.humidity = humidity
                print(self.name, "humidity set to", self.humidity)
                return True
            else:
                raise DeviceIsNotActiveException("Device is not active")
        except DeviceIsNotActiveException:
            return False

    def display_value(self):
        print(f"{super().display_value()}; humidity is {self.humidity}%")
        return f"{super().display_value()}; humidity is {self.humidity}%"
