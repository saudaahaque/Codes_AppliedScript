#Övning 7

computer = "sten"
while True:
    user_choice = input("sten, sax, eller påse?\n")
    if user_choice == "sax":
        print("Du förlorade!")
    elif user_choice == computer:
        print("Oavgjort!")
    elif user_choice == "påse":
        print("Du vann!")
        break
    else:
        print("Försök igen!")

