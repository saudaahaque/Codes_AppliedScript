#Övning 1-4: Lägg till en konstruktor
#övning 1
class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
#övning 2:
    def describe(self):
        return f"Animal({self.species}, {self.age} år)" 

#övning 4: 
    def __str__(self):
        return f"Animal({self.species}), {self.age} år)"