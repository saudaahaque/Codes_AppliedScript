import random

random_number = random.randint(1,3)

guess = int(input("Gissa ett nummer mellan 1 och 3:"))
if guess == random_number:
    print("Rätt gissat!")
else:
    print ("Fel!")