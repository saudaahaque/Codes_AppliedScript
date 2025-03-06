# forsättning på övning 1-4: Lägg till en konstruktor
#övning 1:
from animal import Animal

animal1 = Animal("Katt", 9)
animal2 = Animal("Hund", 15)

print(animal1.species)
print(animal1.age)

print(animal2.species)
print(animal2.age)

#övning 2:
print(animal1.describe())
print(animal2.describe())

#övning 3:

animal3 = Animal("Fågel", 25)
animal4 = Animal("Lejon", 30)
animal5 = Animal("Elefant", 35)

print(animal3.describe())
print(animal4.describe())
print(animal5.describe())

#övning 4:

animal6 = Animal("kanin", 5)
animal7 = Animal("Mask", 23)

print(animal6)
print(animal7)