bold="\033[1m"
end="\033[0m"
green="\033[32m"
red="\033[31m"

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
            firstnumber = float(input(bold+green+"Enter first number: "+end))
            secondnumber = float(input(bold+green+"Enter second number: "+end))
            return firstnumber,secondnumber
        except ValueError:
            print(bold+red+"Invalid input! Please enter numbers only.\n"+end)


def main():
    while True:
        print("\n=== SIMPLE CALCULATOR ===")
        print("")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("")
        choice = input("Choose operation (1-4): ")

        if choice not in ['1', '2', '3', '4']:
            print(bold+red+"Invalid operation! Please try again."+end)
            continue

        firstnumber, secondnumber = get_numbers()

        try:
            if choice == '1':
                operation = Addition(firstnumber,secondnumber)
            elif choice == '2':
                operation = Subtraction(firstnumber,secondnumber)
            elif choice == '3':
                operation = Multiplication(firstnumber,secondnumber)
            elif choice == '4':
                operation = Division(firstnumber,secondnumber)

            result = operation.calculate()
            print(f"\nThe total is = {result}")

        except ZeroDivisionError as error:
            print(f"Error: {error}")

        again = input("\nDo you want to try again? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you!")
            break


if __name__ == "__main__":
    main()
