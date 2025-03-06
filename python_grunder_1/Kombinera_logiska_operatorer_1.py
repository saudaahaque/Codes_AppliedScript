#övning 1  Kombinera logiska operatorer 

user_answer = input("Har du en biljett\n")
user_age = input("Är du 18+)\n")

if user_answer and user_age == "Ja":
    print("Välkommen in!")
else:
    print("Du är inte välkommen!")


user_answer = input("Har du en biljett?\n")
user_age = int (input("Hur gammal är du?\n"))

if user_answer == "Ja" and user_age >= 18:
    print("Välkommen!")

else:
    print("Du är inte välkommen!")
          


