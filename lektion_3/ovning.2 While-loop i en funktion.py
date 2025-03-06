# Övning 12: While-loop i en funktion

def räkna_ner(nummer):
    counter = nummer
    while counter >= 0:
        print(f"Counter är {counter}")
        counter -= 1
räkna_ner(20)
