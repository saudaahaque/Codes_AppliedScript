#Övning 6: Använd logiska operatorer

vecka = ["måndag", "tidag", "onsdag", "torsdag", "fredag"]
helg = ["lördag", "söndag"]

user_answer = input("Välj en dag ")
user_time = int(input("Välj en tid "))

if (user_answer in vecka and 9 <= user_time < 18) or (user_answer in helg and 10 <= user_time < 16):
    print("Det är öppet!")

else:
    print("Det är stängt!")