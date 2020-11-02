def addition(a, b):
    c = a + b
    return c


def square_root(a):
    c = a ** (1 / 2)
    return c


def subtraction(a, b):
    c = a - b
    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def sqrt(self, a):
        self.result = square_root(a)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result



