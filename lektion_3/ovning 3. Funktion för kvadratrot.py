# Övning 1: Funktion för kvadratrot 
import math

from math import sqrt
print(sqrt(25))

def give_number():
    user_answer = int(input("Ange ett tal "))
    return sqrt (user_answer)

result = give_number()
print(result)

