class Animal:
    def __init__(self, name, species):
        self.name:str = name
        self.species:str = species
    
    def speak(self, name, sound):
        return f"{self.name} makes a {sound} sound."

class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} has given birth."

class Bird(Animal):
    def __init__(self, species, name, wingspan):
        super().__init__(species,name)
        self.wingspan:int = wingspan

class Reptile(Animal):
    def bask_in_sun(self):
        return f"{self.name} is basking in the sun"

class Primate(Mammal):
    def climb_trees(self):
        return f"{self.name} is climbing trees"

class Marsupial(Mammal):
    def carry_baby(self):
        return f"{self.name} is carrying its baby"

class Aviary:
    def __init__(self, birds:list):
        self.birds:list = birds

class ReptileEnclosure:
    def __init__(self, reptiles:list):
        self.reptiles:list = reptiles

molly = Mammal("Molly", "giraffe")
print(molly.give_birth())
print(molly.speak("Molly","crunching"))
gerald = Reptile("Gerald", "lizard")
print(gerald.bask_in_sun())
david = Primate("David", "spider monkey")
print(david.climb_trees())
karen = Marsupial("Karen", "kangaroo")
print(karen.carry_baby())

flight_bird_room = ["canary", "falcon", "eagle"]
non_flight_bird_room = ["ostrich", "chicken", "penguin"]
flying_birds = Aviary(flight_bird_room)
non_flight_birds = Aviary(non_flight_bird_room)
print(flying_birds.birds[0:])
print(non_flight_birds.birds[0:])


scarystuff = ["snake", "alligator"]
nonscarystuff = ["lizard", "gecko"]
scary_reptile_room = ReptileEnclosure(scarystuff)
non_scary_reptile_room = ReptileEnclosure(nonscarystuff)
print(scary_reptile_room.reptiles[0:])
print(non_scary_reptile_room.reptiles[0:])