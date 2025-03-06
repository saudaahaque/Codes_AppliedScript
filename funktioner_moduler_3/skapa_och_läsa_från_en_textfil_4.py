# Övning 4: Skapa och läsa från en textfil:

with open("textfilModuler.txt", "w") as file:
    file.write("Hej, jag heter Sauda Haque\n")
    file.write("Jag är 28 år gammal!\n")
    file.write("Jag bor i Bredäng.\n")
    file.write("Jag började utbildningen i januari 2025.\n")

    with open("textfilModuler.txt", "r") as file:
        print(file.read())