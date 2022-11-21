class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('sub_method from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('sub_method from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('sub_method from class C:', b)
        super().sub_method(b + 1)


class D(C):
    def __init__(self):
        print('Initializing: class D')
        super(C, self).__init__()

    def sub_method(self, b):
        print('sub_method from class D:', b)
        super().sub_method(b + 1)


# c = C()
# c.sub_method(1)
# d = D()
# d.sub_method(1)