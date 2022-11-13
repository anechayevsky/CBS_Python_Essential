class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f'Книжка автора {self.author} під назвою {self.title} рік видання {self.year} в жанрі {self.genre}. '

    def __repr__(self):
        return f'Книжка автора {self.author} під назвою {self.title} рік видання {self.year} в жанрі {self.genre}. '

b1 = Book('Кінг', 'Протистояння', 1978, 'Постапокаліпсис')
print(b1.__str__())
print(b1.__repr__())


