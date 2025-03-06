# Övning 16: Kombinera funktioner 

def name():
    user_name = input("Vad heter du?" )
    return user_name

def age():
    user_age = int(input("Hur gammal är du? "))
    return user_age

def presentation():
    user_name = name()
    user_age = age()
    print(f"Hej jag heter {user_name} och jag är {user_age} år gammal. ")

presentation()