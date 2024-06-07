class SmartDevice:
    status = False

    def __init__(self, name):
        self.name = name
        print(name, "created")

    def switch(self):
        if not self.status:
            self.status = True
            print(self.name, "turned on")
        else:
            self.status = False
            print(self.name, "turned off")

    def display_value(self):
        if self.status:
            return f"{self.name} is active"
        else:
            return f"{self.name} is not active"
