from src.SmartDevice import SmartDevice
from src.Exceptions import DeviceIsNotActiveException
from src.Exceptions import DeviceHasNoObjectInDocsException


class SmartHouseholdAppliance(SmartDevice):
    type = ""  # cleaning, food
    documentation = []  # "fried eggs", "boiled eggs", "meat", "pasta", "rice", "coffe", "tea", "toast", "pancakes"

    # "dishes", "floor"

    def __init__(self, name, type, documentation):
        super().__init__(name)
        self.type = type
        self.documentation = documentation

    def work(self):
        try:
            if self.status:
                object = input("Input object of work\n")
                if self.type == "cleaning":
                    try:
                        if object in self.documentation:
                            print(f"cleaning {object}")
                            return f"cleaning {object}"
                        else:
                            raise DeviceHasNoObjectInDocsException("Sorry, there is no such object in documentation")
                    except DeviceHasNoObjectInDocsException:
                        return "process canceled, no such object in documentation"
                elif self.type == "food":
                    try:
                        if object in self.documentation:
                            print(f"{object} is done")
                            return f"{object} is done"
                        else:
                            raise DeviceHasNoObjectInDocsException("Sorry, there is no such object in documentation")
                    except DeviceHasNoObjectInDocsException:
                        return "process canceled, no such object in documentation"
                else:
                    try:
                        if object in self.documentation:
                            print(f"doing something with {object}")
                            return f"doing something with {object}"
                        else:
                            raise DeviceHasNoObjectInDocsException("Sorry, there is no such object in documentation")
                    except DeviceHasNoObjectInDocsException:
                        return "process canceled, no such object in documentation"
            else:
                raise DeviceIsNotActiveException("Device is not active")
        except DeviceIsNotActiveException:
            print("Device is not active")
            return "Turn on device to use it!"

    def display_value(self):
        print(f"{super().display_value()}")
        return f"{super().display_value()}"
