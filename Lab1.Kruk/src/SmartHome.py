from src.SecuritySystem import SecuritySystem
from src.Schedule import Schedule
from datetime import datetime
from src.SmartDevice import SmartDevice
from src.Exceptions import EmptyListException
from src.Exceptions import NoSchedulesException


class SmartHome:
    security_systems = []
    schedules = []

    def __init__(self, devices):
        self.devices = devices
        print("Smart home created")

    def add_smart_device(self, device):
        if isinstance(device, SmartDevice):  # если device является экземляром класса или его подклассов
            self.devices.append(device)
            print(device.name, "added to smart home")
            if isinstance(device, SecuritySystem):
                self.security_systems.append(device)

    def list_devices(self):
        try:
            if self.devices:
                print("Smart devices at home:")
                print("-----------")
                for device in self.devices:
                    device.display_value()
                print("-----------")
                return True
            else:
                raise EmptyListException("List is empty")
        except EmptyListException:
            return False

    def create_schedule(self, name, scheduled_time):
        device = self.get_device_by_name(name)
        if device:
            # list functions
            schedule_methods = [method for method in dir(device) if callable(getattr(device, method)) and not method.startswith("__")]
            print(f"Choose a function of {name}:")
            for i, method in enumerate(schedule_methods):
                print(f"{i + 1}. {method}")

            # choose device function
            choice = int(input("Enter the number of the function to execute: ")) - 1
            if 0 <= choice < len(schedule_methods):
                action = getattr(device, schedule_methods[choice])
                schedule = Schedule(action, scheduled_time)
                self.schedules.append(schedule)
                print("action sheduled")
            else:
                print("No such function")
        else:
            print(f"Device '{name}' not found")

    def run_schedules(self):
        current_time = datetime.now().time()
        if self.schedules:
            for schedule in self.schedules[:]:  # делаем срез списка, чтобы при удалении элемента списка не ломалась итерация
                if schedule.is_time_to_run(current_time):
                    print("Executing schedule")
                    schedule.action()
                    print("Schedule is done")
                    self.schedules.remove(schedule)
                else:
                    print("it is not time yet for this action:")
                    schedule.display_schedule()
        else:
            print("No schedules found")

    def display_schedules(self):
        try:
            if self.schedules:
                print("Schedules:")
                print("-----------")
                for schedule in self.schedules:
                    schedule.display_schedule()
                print("-----------")
                return True
            else:
                raise NoSchedulesException("No schedules")
        except NoSchedulesException:
            print("No schedules found")
            return False

    def check_security_systems(self):
        for device in self.security_systems:
            device.security_check()
        print("Security systems check is done")

    def get_device_by_name(self, name):  # get device by name to control specific device through home class
        for device in self.devices:
            if device.name == name:
                return device
        return None

    def control_device(self, name):  # control device from SmartHome class so to not calling examples of device's class
        device = self.get_device_by_name(name)
        if device:
            # list functions
            methods = [method for method in dir(device) if callable(getattr(device, method)) and not method.startswith("__")]
            print(f"Choose a function of {name}:")
            for i, method in enumerate(methods):
                print(f"{i + 1}. {method}")

            # choose device function
            choice = int(input("Enter the number of the function to execute: ")) - 1
            if 0 <= choice < len(methods):
                method_to_call = getattr(device, methods[choice])
                method_to_call()
            else:
                print("No such function")
        else:
            print(f"Device '{name}' not found")
