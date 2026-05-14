class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml cup chai cup "

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))
cup_two = Chaicup()
cup_two.size = 1000
print(Chaicup.describe(cup_two)) 