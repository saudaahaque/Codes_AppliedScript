# forsättning på övning 5: Skapa en ny klass Car

from car import Car

car1 = Car("Volvo", 2023)
car2 = Car("Tesla", 2020)
car3 = Car("Audi", 1997)


print(car1.brand)
print(car1.year)

print(car2.brand)
print(car2.year)

print(car3.brand)
print(car3.year)


print(car1.car_age())
print(car2.car_age())
print(car3.car_age())