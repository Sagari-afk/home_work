class Calculator:

    def __init__(self, type_of_calculator="common"):

        if type_of_calculator in ["common", "accounting", "scientific"]:
            self.type_of_calculator = type_of_calculator

        else:
            print("Error. Wrong type of calculator. There are only: common, accounting and scientific")


    def addition(self, first_number, second_number):
        result = int(first_number) + int(second_number)
        print("The result is", result)

    def subtraction(self, first_number, second_number):
        result = int(first_number) - int(second_number)
        print("The result is", result)

    def multiplication(self, first_number, second_number):
        result = int(first_number) * int(second_number)
        print("The result is", result)

    def division(self, first_number, second_number):
        result = int(first_number) / int(second_number)
        print("The result is", result)


a = Calculator()

a.addition(5, 10)
a.subtraction(5, 10)
a.multiplication(5, 10)
a.division(5, 10)
