from book import Book

book_list = []

book_list.append(Book("Främlingen", "Albert Camus"))
book_list.append(Book("Lille prins", "Antoine de Saint-Exupery"))
book_list.append(Book("Vredens druvor", "John Steinbeck"))
book_list.append(Book("Blå Lotus", "Herge"))

for book in book_list:
    print(book.summary())