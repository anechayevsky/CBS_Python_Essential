class Book:

    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.description = []

    def __str__(self):
        return f'Книжка автора {self.author} під назвою {self.title} рік видання {self.year} в жанрі {self.genre}. Відгуки: {self.description} '

    def __repr__(self):
        return f'Книжка автора {self.author} під назвою {self.title} рік видання {self.year} в жанрі {self.genre}. Відгуки: {self.description}'


class Book_Description:
    def __init__(self, book, description):
        self.description = description
        book.description.append(self)

    def __repr__(self):
        return self.description


b1 = Book('Кінг', 'Протистояння', 1978, 'Постапокаліпсис')
desc_b1 = Book_Description(b1, 'Класна книга!')
desc_b2 = Book_Description(b1, 'Автор, пиши ще!')
desc_b3 = Book_Description(b1, 'Книга низької якості, автор нехороша людина')

print(b1)
