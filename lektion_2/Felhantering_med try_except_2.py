#övning 2:  Felhantering med try och except 

try:
    number = int(input("Skriv in ett heltal: "))
    print(f"Du skrev in: {number}")
except ValueError:
    print("Fel: du måste skriva in ett heltal!")