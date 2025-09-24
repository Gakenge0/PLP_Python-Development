# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Derived class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.__storage = storage      # encapsulated attribute (private)
        self.battery = battery

    def get_storage(self):
        return self.__storage

    def install_app(self, app_name, size):
        if size <= self.__storage:
            self.__storage -= size
            print(f"Installed {app_name}. Remaining storage: {self.__storage}GB")
        else:
            print("Not enough storage to install the app.")

    def charge(self):
        self.battery = 100
        print(f"{self.device_info()} is fully charged!")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S22", storage=128, battery=75)
print(phone1.device_info())
phone1.install_app("WhatsApp", 2)
phone1.charge()
print(f"Storage left: {phone1.get_storage()}GB")
