class Human:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_pass(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_pass_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There's no passengers in {self.brand}")


alex = Human("Alex")
ella = Human("Ella")
car = Car("Peugeot")

car.add_pass(alex, ella)
car.print_pass_names()
