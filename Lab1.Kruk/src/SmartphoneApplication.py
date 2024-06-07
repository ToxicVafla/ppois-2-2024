from src.HumiditySystem import HumiditySystem
from src.Lighting import Lighting
from src.SecuritySystem import SecuritySystem
from src.SmartDevice import SmartDevice
from src.SmartHome import SmartHome
from src.SmartHouseholdAppliance import SmartHouseholdAppliance
from src.TemperatureDevice import TemperatureDevice
from datetime import time


def app_menu():
    my_home = SmartHome([])
    available_devices = [SecuritySystem("fire alarm 1", "fire", 1), SecuritySystem("camera 1", "breakIn", 2),
                         SmartDevice("robot 1"), Lighting("light 1"), HumiditySystem("air conditioner 1"),
                         SmartHouseholdAppliance("coffee machine", "food", ["latte", "espresso"]),
                         SmartHouseholdAppliance("washer", "cleaning", ["dishes", "floor"]),
                         TemperatureDevice("heater 1")]
    while True:
        choice: str = input("Choose operation:\n"
                            "1 - add device from list\n"
                            "2 - see list of devices in smart home\n"
                            "3 - control device in smart home\n"
                            "4 - security systems monitoring\n"
                            "5 - create schedule\n"
                            "6 - list schedules\n"
                            "7 - run schedules\n"
                            "q - quit\n")

        if choice == "1":
            try:
                print(f"List of available devices: ")
                for ind, device in enumerate(available_devices):
                    print(f"{ind + 1}:{device.name}")
                print("Choose a device(input an index): ")
                ind = int(input()) - 1
                if 0 <= ind < len(available_devices):
                    my_home.add_smart_device(available_devices[ind])
                    available_devices.pop(ind)
                else:
                    print("Invalid index")
            except ValueError:
                print("invalid index")
        elif choice == "2":
            my_home.list_devices()
        elif choice == "3":
            my_home.control_device(input("Input device name to control\n"))
        elif choice == "4":
            my_home.check_security_systems()
        elif choice == "5":
            my_home.create_schedule(input("Name of device\n"), time(int(input("Input hours\n")), int(input("Input minutes\n"))))
        elif choice == "6":
            my_home.display_schedules()
        elif choice == "7":
            my_home.run_schedules()
        elif choice == "q":
            break
        else:
            print("Invalid choice")
        print("----------------------------------------------------------")


app_menu()
