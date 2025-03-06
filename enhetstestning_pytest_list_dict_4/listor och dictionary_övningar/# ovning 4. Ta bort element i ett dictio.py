# Övning 7: Ta bort element i ett dictionary

book = {"titel": "Funny Story", "författare": "Emily Henry", "år": 2025}

book.pop("år")
del book["författare"]

print(book)