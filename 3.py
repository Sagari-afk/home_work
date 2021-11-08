import math

class Calculator:


    def addition(self, first_number, second_number):
        result = float(first_number) + float(second_number)
        return result


    def subtraction(self, first_number, second_number):
        result = float(first_number) - float(second_number)
        return result


    def multiplication(self, first_number, second_number):
        result = float(first_number) * float(second_number)
        return result


    def division(self, first_number, second_number):
        if second_number != 0:
            result = float(first_number) / float(second_number)
            return result
        else:
            print("Error. Division by zero")


    def exponentiation(self, first_number, second_number):
        result = float(first_number) ** float(second_number)
        return result

    
    def sq_root(self, number):
        result = math.sqrt(number)
        return result


class Common_Calculator(Calculator):
    pass


class Accounting_Calculator(Calculator):

    addition_res = []
    subtractionn_res = []
    multiplication_res = []
    division_res = []
    exponentiation_res = []
    sq_root_res = []


    def addition(self, first_number, second_number):
        self.addition_res.append(super().addition(first_number, second_number))


    def subtraction(self, first_number, second_number):
        self.subtractionn_res.append(super().addition(first_number, second_number))


    def multiplication(self, first_number, second_number):
        self.multiplication_res.append(super().addition(first_number, second_number))


    def division(self, first_number, second_number):
        self.division_res.append(super().addition(first_number, second_number))


    def exponentiation(self, first_number, second_number):
        self.exponentiation_res.append(super().addition(first_number, second_number))

    
    def sq_root(self, number):
        self.sq_root_res.append(super().addition(number))

    def get_information(self):
        print(self.addition_res,
              self.subtractionn_res,
              self.multiplication_res,
              self.division_res,
              self.exponentiation_res,
              self.sq_root_res)


class Scientific_Calculator(Calculator):


    def trig(self, trig, number):
        if trig == "sin":
            return math.sin(number)

        elif trig == "cos":
            return math.cos(number)

        elif trig == "tg":
            return math.tan(number)
        
        else:
            print("Error. Not a trigonometric func")


first = Common_Calculator()
print(first.addition(9, 3))
print(first.sq_root(4))

second = Accounting_Calculator()
second.addition(9, 3)
second.get_information()

third = Scientific_Calculator()
print(third.trig("sin", 1))
