# Define the Mammal class
class Mammal:
    def __init__(self, name):
        self.name = name

    def spot_prey(self):
        return f"{self.name} spots prey."

    def chase_prey(self):
        return f"{self.name} chases prey."

    def flee(self):
        return f"{self.name} flees from danger."

    def rest(self):
        return f"{self.name} rests after a long day."

    def eat(self):
        return f"{self.name} eats the captured prey."

# Create instances of Mammal
lion = Mammal("Lion")
tiger = Mammal("Tiger")

# Simulate the sequence of interactions
print(lion.spot_prey())
print(lion.chase_prey())
print(tiger.flee())
print(lion.rest())
print(lion.eat())
