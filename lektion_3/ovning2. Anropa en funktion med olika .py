#Övning 4: Anropa en funktion med olika argument

def mening(namn):
    print(f"Hej {namn}, Välkommen!")

while True:
    user_name = input("Hej, välkommen, vad heter du? ")
    mening(user_name)
