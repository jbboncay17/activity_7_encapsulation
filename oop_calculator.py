class Calculator:
    def __init__(self, firstnum, secondnum):
        self.firstnum = firstnum
        self.secondnum = secondnum

    def calculate(self):
        pass


class Addition(Calculator):
    def calculate(self):
        return self.firstnum + self.secondnum


class Subtraction(Calculator):
    def calculate(self):
        return self.firstnum - self.secondnum


class Multiplication(Calculator):
    def calculate(self):
        return self.firstnum * self.secondnum


class Division(Calculator):
    def calculate(self):
        if self.secondnum == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return self.firstnum / self.secondnum