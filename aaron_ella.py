# базовано на книзі "Знищ мене"
# головним героям постійно стирали пам'ять але вони все одно постійно закохувалися один в одного, хоч і забували
# згодом вони все зрозуміють і будуть потім разом



class Human:
    def __init__(self, name, age, sex, hair, eyes, height, job, married=0, love=1, memory=0, health=50, happiness=50, eat=100):
        self.name = name
        self.age = age
        self.sex = sex
        self.hair = hair
        self.eyes = eyes
        self.height = height
        self.job = job
        self.hap = happiness
        self.eat = eat
        self.memory = memory
        self.health = health
        self.love = love
        self.married = married

    def eating(self):
        if self.eat < 100:
            self.eat = self.eat + 10
            print(f"full {self.eat}")
        else:
            print("Not hungry")

    def memory_erase(self):
        self.eat = self.eat - 10
        self.memory = 0
        self.love = 0
        self.health = self.health - 20
        print(f"memory erasing; memory {self.memory}")
        print(f"full less {self.eat}")
        print(f"forgot to love; love {self.love}")
        print(f"damaged; health {self.health}")

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Sex: {self.sex}, Hair: {self.hair}, Eyes: {self.eyes}, Height: {self.height}, Job: {self.job}")

    def meeting(self):
        self.love = 1
        self.hap = 100
        print(f"love {self.love}, happiness {self.hap}")

    def argument(self):
        self.hap = self.hap - 10
        print(f"happiness {self.hap}")

    def broke_up(self):
        self.hap = 0
        print(f"Heartbroken; happiness {self.hap}")

    def realising(self):
        self.memory = 1
        self.love = 1
        self.hap = 200
        print(f"memory complete; memory {self.memory}")
        print(f"obviously in love; love {self.love}")
        print(f"happiness {self.hap}")

    def marriage(self):
        if self.hap == 200:
            self.married = 1
            print("Married")


aaron = Human("Aaron", 19, "Male", "Blond", "Green", "5'9 ft", "Chief Commander of Sector 45")
ella = Human("Ella", 17, "Female", "Brown", "Blue", "5'3 ft", "Unemployed")


print(" === Shatter me ===")
aaron.memory_erase()
print("Recovering")
aaron.eating()
print(f"A year passed, met again...")
aaron.show()
ella.show()
aaron.meeting()
print("But argument...")
aaron.argument()
print("And after all breaking up...")
aaron.broke_up()
print("Suddenly again...")
aaron.memory_erase()
print("trying to recover...")
aaron.eating()
print("A month passed, met again")
aaron.meeting()
print("After watching some photos a docs, they realised...")
aaron.realising()
print("Proposing")
aaron.marriage()