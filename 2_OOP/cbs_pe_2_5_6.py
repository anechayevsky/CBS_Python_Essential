from datetime import date


class MyClass1:
    UA_legal_count = 0
    US_legal_count = 0

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
        self.legal_UA = (age >= 18)
        self.legal_US = (age >= 21)
        if self.legal_US:
            MyClass1.US_legal_count += 1
            MyClass1.UA_legal_count += 1
        elif self.legal_UA and not self.legal_US:
            MyClass1.UA_legal_count += 1

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    @classmethod
    def get_UA_legal(cls):
        print(cls.UA_legal_count)

    @classmethod
    def get_US_legal(cls):
        print(cls.US_legal_count)

    @staticmethod
    def legal_age(age):
        if 18 <= age < 21:
            return f'В Україні в {age} людина вже повнолітня, а в США - ні'
        elif age >= 21:
            return f'В США та в Україні  людина в {age} вже повнолітня'
        else:
            return f'В {age} людина ще неповнолітня і в Україні, і в США'

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age) + ' ' + self.legal_age(self.age))


class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2000)
m_per2.print_info()

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
m_per4.get_UA_legal()
m_per4.get_US_legal()
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))
