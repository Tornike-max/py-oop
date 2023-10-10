class Car():
    def __init__(self, brand, model, color, horse_power, is_sport_car):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car

    def __str__(self):
        if self.__is_sport_car == True:
            self.__is_sport_car = 'Sport car'
        else:
            self.__is_sport_car = 'Regular car'
        return f"I have a {self.__brand} {self.__model}, it's {self.__color} and it has {self.__horse_power} horse power, it's also a {self.__is_sport_car}"

    def increase_hp(self, hp):
        if hp > 0:
            self.__horse_power = hp
        else:
            return False

    def change_color(self, new_color):
        if new_color != self.__color:
            raise ValueError('choose different color')
        self.__color = new_color
        return True

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    @property
    def horse_power(self):
        return self.__horse_power

    @property
    def is_sport_car(self):
        return self.__is_sport_car


def main_func():
    brand = input('brand: ')

    model = input('model: ')

    color = input('color: ')

    horse_power = input('horse_power: ')

    is_sport_car = bool(input('is_sport_car: '))

    car = Car(brand, model, color, horse_power, is_sport_car)

    increased_hp = int(input('Enter increased horsepower: '))
    if car.increase_hp(increased_hp):
        print(f"Updated Horse Power: {car.horse_power}")
    else:
        print("Invalid input for additional horsepower.")

    print(car)
    return car


main_func()
