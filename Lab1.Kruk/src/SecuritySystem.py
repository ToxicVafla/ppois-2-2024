from src.SmartDevice import SmartDevice
import time
from src.Exceptions import DeviceIsNotActiveException


class SecuritySystem(SmartDevice):
    charge_value = 20
    device_type = ""  # breakIn, fire
    covering_area = 0  # there are 3 zones

    def __init__(self, name, device_type, covering_area):
        super().__init__(name)
        self.device_type = device_type
        self.covering_area = covering_area

    def charge(self):
        if self.status:
            self.switch()
        while self.charge_value <= 90:
            self.charge_value += 10
            time.sleep(1)
            print("charging...", self.charge_value)
        self.security_check()

    def security_check(self):
        if not self.status:
            print(f"Don't forget to turn on {self.name}")
            return f"Don't forget to turn on {self.name}"

    def alarm(self):
        try:
            if self.status:
                report = ""
                if self.device_type == "breakIn":
                    report = "Alarm. Police called!"
                elif self.device_type == "fire":
                    report = "Alarm. Firefighters called!"
                if int(input("Input number of injured people")) > 0:
                    print(f"{report} Ambulance called!")
                    return f"{report} Ambulance called!"
                else:
                    print(report)
                    return report
            else:
                raise DeviceIsNotActiveException("Device is not active")
        except DeviceIsNotActiveException:
            return self.security_check()

    def display_value(self):
        print(f"{super().display_value()}; charge value is {self.charge_value}%")
        return f"{super().display_value()}; charge value is {self.charge_value}%"
