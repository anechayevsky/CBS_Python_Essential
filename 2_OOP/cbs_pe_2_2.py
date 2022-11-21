class GrafObj:
    pass


class Rectangle(GrafObj):
    pass


class MouseClick:
    def click(self):
        print('Клік!')


class Button(Rectangle, MouseClick):
    pass


first_button = Button()
first_button.click()