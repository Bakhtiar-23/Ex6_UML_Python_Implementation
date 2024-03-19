class Mammal:
    def spot_prey(self, prey):
        print(f"Mammal spots {prey}")

    def chase_prey(self, prey):
        print(f"Mammal chases {prey}")

    def rest(self, habitat):
        print(f"Mammal rests in {habitat}")

    def eat(self, habitat):
        print(f"Mammal eats in {habitat}")


class Prey:
    def flee(self, mammal):
        print(f"Prey flees from {mammal}")


class Habitat:
    def rest(self, mammal):
        print(f"{mammal} rests in habitat")

    def eat(self, mammal):
        print(f"{mammal} eats in habitat")


# Usage example
mammal = Mammal()
prey = Prey()
habitat = Habitat()

mammal.spot_prey("rabbit")
mammal.chase_prey("rabbit")
prey.flee("Mammal")
mammal.rest("forest")
mammal.eat("forest")
