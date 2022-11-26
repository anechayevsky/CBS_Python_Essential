class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.comment = []

    def add_comment(self):
        self.review = Comment()
        self.comment.append(self.review)

    def __str__(self):
        return f'Книжка автора {self.author} під назвою {self.title} рік видання {self.year} в жанрі {self.genre}. Відгуки: {self.comment} '

    def __repr__(self):
        return f'Книжка автора {self.author} під назвою {self.title} рік видання {self.year} в жанрі {self.genre}. Відгуки: {self.comment}'


class Comment:
    def __init__(self):
        self.name = input("Введіть ваше ім'я: ")
        self.rating = int(input('Введіть числову оцінку книги: '))
        self.review = input('Введіть відгук: ')

    def __repr__(self):
        return f"Ім'я: {self.name} \n," \
               f"оцінка: {self.rating}, \n" \
               f"коментар: {self.review}"

    def __str__(self):
        return f"Ім'я: {self.name} \n," \
               f"оцінка: {self.rating}, \n" \
               f"коментар: {self.review}"


b1 = Book('Кінг', 'Протистояння', 1978, 'Постапокаліпсис')
b1.add_comment()
print(b1)
