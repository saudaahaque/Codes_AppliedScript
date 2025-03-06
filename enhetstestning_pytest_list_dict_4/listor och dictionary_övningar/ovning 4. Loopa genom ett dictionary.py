# Övning 8: Loopa genom ett dictionary

person = {"namn": "Sauda", "ålder": 28, "stad": "Uppsala"}
lärare = {"namn": "Håkan", "ålder": 53, "stad": "Stockhom"}
student = {"namn": "Habbenur", "ålder": 32, "stad": "Göteborg"}

for key, value in person.items():
    print(key, "->", value)

for key, value in lärare.items():
    print(key, "->", value)

for key, value in student.items():
    print(key, "->", value)
