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


print("==========================")


# успадкування
class human:
    height = 170
    age = 40
    def print(self):
        print("Hello world!")

class student(human):
    age = 17

class teacher(human):
    age = 30
    def print(self):
        print("hello")

zhora = student()
patricia = teacher()
print(zhora.age)
print(patricia.age)
zhora.print()
patricia.print()


print("==========================")


# приватність/публічність - для безпеки даних від користувачів
class HelloWorld:
    hello = "hello"         # public
    _hello = "_hello"       # marked as protected (you can but better not)
    __hello = "__hello"     # they ARE protected (error)

    def __init__(self):
        self.world = "world"
        self._world = "_world"
        self.__world = "__world"

hello = HelloWorld()
print(hello.hello)     #public
print(hello.world)     #public
print(hello._hello)    #підкреслені
print(hello._world)    #підкреслені
#print(hello.__hello)   #error
#print(hello.__world)   #error


print("==========================")


# витягнути з батьківського
class One:
    var = 20
    def __init__(self):
        self.var = 10

class Two(One):
    def __init__(self):
        print(self.var)
        super().__init__()     #залізли у батьківський ініт (вар=10)
        print(self.var)
        print(super().var)     #залізли в бат. клас до вар=20

hello = Two()


print("==========================")


# множинне успадкування -- super().__init__()
class Comp:
    def __init__(self):
        super().__init__()
        self.memory = 100

class Display:
    def __init__(self):
        super().__init__()
        self.resol = "4K"

class All(Comp, Display):
    def print(self):
        print(self.memory)
        print(self.resol)

obj = All()
obj.print()