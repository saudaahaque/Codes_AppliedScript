# Övning 5:  Kombinera loopar och felhantering

while True:
    try:
        number = int(input("Ange ett heltal: "))
        print(f"Du angav talet: {number}")
        break
    except ValueError:
        print("Ogiligt tal. Var god att ange ett heltal! ")

