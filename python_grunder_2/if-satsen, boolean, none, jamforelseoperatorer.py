num = 30
num2 = 30

if num2 > num:
    print("num2 är större")
elif num > num2:
    print("num är större")
else:
    print("num == num2")

num3 = None
if num3 == None:
    print("None")

is_sunny = True
is_warm = False

if is_sunny and is_warm:
    print("Det är varmt. Det är sorligt.")
elif is_sunny:
    print("Det är sorligt.")

elif is_warm:
    print("Det är varmt.")
else:
    print("Det är varken varmt eller sorligt.")


is_sunny = True
is_warm = False
if is_sunny:
    print("Det är soligt")
if is_sunny and is_warm:
    print("Det är soligt. Det är varmt")


number = 5
print(number)
number += 3; 
print(number)

number = 5
print(number)
number -= 2
print(number)

number = 5
print (number)
number *= 4
print(number)

number = 10
print(number)
number /=2
print(number)