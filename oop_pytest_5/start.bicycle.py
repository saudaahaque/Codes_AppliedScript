from bicycle import Bicycle

monark = Bicycle("Monark", 2020, "Red")

print(monark.color)
print(monark.year)
print(monark.model)

print(monark.started)
monark.start()
print(monark.started)