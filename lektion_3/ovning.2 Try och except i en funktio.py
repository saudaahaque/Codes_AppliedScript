# Övning 13: Try och except i en funktion:

def heltal():
    try: 
        a = int(input("Skriv ett heltal"))
        return True
    except:
        return False
while True:
    print(heltal())

        