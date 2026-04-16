class SmartDevice:
    def __init__(self, brand, model, battery_level, is_on):
        self.brand = brand
        self.model = model


        if battery_level < 0:
            self.__battery_level = 0
        elif battery_level > 100:
            self.__battery_level = 100
        else:
            self.__battery_level = battery_level

        if isinstance(is_on, bool):
            self.__is_on = is_on
        else:
            self.__is_on = False


    def turn_on(self):
        if self.__battery_level == 0:
            print("Нельзя включить: заряд 0%")
        else:
            self.__is_on = True
            print("устройство включено")


    def turn_off(self):
        self.__is_on = False
        print("устройство выключено")


    def charge(self, amount):
        if amount <= 0:
            print("Заряд должен быть положительным")
            return

        self.__battery_level += amount
        if self.__battery_level > 100:
            self.__battery_level = 100

        print(f"Заряд: {self.__battery_level}%")


    def use(self, minutes):
        if not self.__is_on:
            print("устройство выключено")
            return

        if minutes <= 0:
           return

        if minutes > self.__battery_level:
            print("заряда недостаточно. устройство выключено")
            self.__battery_level = 0
            self.__is_on = False
        else:
            self.__battery_level -= minutes
            print(f"использовано {minutes} мин. Осталось {self.__battery_level}%")


    def get_status(self):
        status = "Да" if self.__is_on else "Нет"
        return f"Устройство: {self.brand} {self.model} | Включено: {status} | Заряд: {self.__battery_level}%"




device =SmartDevice("Note book", "F-14", 90, False)


print(device.get_status())


device.turn_on()
device.use(7)
device.charge(20)
device.use(100)
device.turn_off()

print(device.get_status())