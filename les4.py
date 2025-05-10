#task 1 - homework
#task 2, 3, 4, 5 - classwork

print("================ Task 1 ================")
class Animal:
    paws = 4
    eyes = 2

class Cat(Animal):
    size = "small"
class Dog(Animal):
    size = "big"

marsik = Cat()
bud = Dog()
print("Marsik")
print(f"Paws: {marsik.paws}")
print(f"Eyes: {marsik.eyes}")
print(f"Size: {marsik.size}")
print("Buddy")
print(f"Paws: {bud.paws}")
print(f"Eyes: {bud.eyes}")
print(f"Size: {bud.size}")

print("================ Task 2 ================")
class Person:
    name = "Tolik"
    def age(self):
        self.age = 38
        print(self.age)

class Driver(Person):
    number = 2846469372

tolik = Driver()
print(tolik.name)
tolik.age()
print(tolik.number)

print("================ Task 3 ================")
class Vehicle:
    v = "50 mph"
    s = "100 m"
class Bus(Vehicle):
    seats = 30
class SmallBus(Vehicle):
    seats = 20
class Car(Vehicle):
    seats = 5
bus = Bus()
small = SmallBus()
car = Car()
print(f"Bus. V: {bus.v}, S: {bus.s}, Seats: {bus.seats}")
print(f"Smaller bus. V: {small.v}, S: {small.s}, Seats: {small.seats}")
print(f"Car. V: {car.v}, S: {car.s}, Seats: {car.seats}")

print("================ Task 4 ================")
class Device:
    def TurnOn(self):
        print("Turned on")
    def TurnOff(self):
        print("Turned off")

class Phone(Device):
    print("Phone")
class Laptop(Device):
    print("Laptop")
ph = Phone()
lap = Laptop()
ph.TurnOn()
ph.TurnOff()
lap.TurnOn()
lap.TurnOff()

print("================ Task 5 ================")
class Language:
    def __init__(self, name):
        self.name = name
    def print(self):
        print(f"Hello, world! I'm {self.name}")
class Python(Language):
    def __init__(self):
        super().__init__("Python")
class JavaScript(Language):
    def __init__(self):
        super().__init__("JavaScript")
class Java(Language):
    def __init__(self):
        super().__init__("Java")
python = Python()
javascript = JavaScript()
java = Java()
python.print()
javascript.print()
java.print()