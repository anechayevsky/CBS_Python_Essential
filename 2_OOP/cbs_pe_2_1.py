class editor:
    def view_document(self):
        print('перегляд документу \n')



    def edit_document(self):
        print('редагування документів недоступне для безкоштовної версії \n')

class proeditor(editor):
    def edit_document(self):
        print('це про-версія! ура! \n')

key = input('введіть ліцензійний ключ: ')
if key == '1234':
    document = proeditor()
else:
    document = editor()

while true:
    option = input('що бажаєте зробити з документом? \n'
                   '1. переглянути \n'
                   '2. відредагувати \n \n'
                   '0. завершити роботу \n')
    match option:
        case '1':
            document.view_document()
        case '2':
            document.edit_document()
        case '0':
            print('до побачення!')
            break





