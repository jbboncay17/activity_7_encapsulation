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


def get_numbers():
    while True:
        try:
            firstnumber = float(input("Enter first number: "))
            secondnumber = float(input("Enter second number: "))
            return firstnumber,secondnumber
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")


def main():
    while True:
        print("\n=== SIMPLE CALCULATOR ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose operation (1-4): ")

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Try again.")
            continue

        firstnumber, secondnumber = get_numbers()