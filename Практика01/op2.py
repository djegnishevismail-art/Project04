class SmartDevice:
    def init(self, brand, model, battery_level, is_on):
        self.brand = brand
        self.model = model
        self.__battery_level = battery_level
        self.__is_on = is_on


    def turn_on(self):
        self.__is_on = True


    def turn_off(self):
        self.__is_on = False


    def charge(self, amount):
        self.__battery_level += amount


    def use(self, minutes):
        self.__battery_level -= minutes


    def get_status(self):
        status = "Да" if self.__is_on else "Нет"
        return f"{self.brand} {self.model}  . Включено: {status} .  Заряд: {self.__battery_level}%"




device = SmartDevice()
device.init("Samsung", "011", 50, True)
device1 = SmartDevice()
device1.init("Notebook", "F-14", 45, False)
device2 = SmartDevice()
device2.init("Tv", "Smart1", 70, True)



print(device.get_status())
print(device1.get_status())
print(device2.get_status())

device.use(50)
device.charge(0)
device.turn_off()







