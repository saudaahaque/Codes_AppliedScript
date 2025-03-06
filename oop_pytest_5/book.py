#Övning 6: Användning av lista med objekt

class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author

    def summary(self):
        return f"Book information: ({self.title}, {self.author})"
    
