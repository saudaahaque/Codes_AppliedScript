# Övning 10: Funktion med if, elif, else

def betyg(poäng):
    if 90 <= poäng <= 100:
        return "A"
    elif 80 <= poäng <= 89:
        return "B"
    elif 70 <= poäng <= 79:
        return "C"
    elif 60 <= poäng <= 69:
        return "D"
    else:
        return "F"
    
print(betyg(77))


