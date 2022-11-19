class Car:
    counter = 0

    def __init__(self, model, number, color, price):
        self.model = model
        self.color = color
        self.number = number
        self.price = price
        Car.counter += 1
        self.id = Car.counter

    def buy(self, salon_name):
        salon_name.car_list[self.id] = self

    def sell(self, salon_name):
        del salon_name.car_list[self.id]

    def __repr__(self):
        return f'Авто {self.model} колір {self.color} номер {self.number} ціна {self.price}.'


class Salon:
    car_list = {}


first_salon = Salon()
car1 = Car('ford', 123, 'black', 10000)
car1.buy(first_salon)
print(first_salon.car_list)
car1.sell(first_salon)
print(first_salon.car_list)
