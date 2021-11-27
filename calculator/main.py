from abc import ABC

from utils import CalculatorUtil

from math import sqrt, log, fabs, sin, cos, tan
from matplotlib.pyplot import subplots, plot, show
from numpy import linspace



class AbsCalculator(ABC):

    @staticmethod
    def value_convertor_float(value) -> float:
        if not isinstance(value, float):
            try:
                value = float(value)
            except:
                raise TypeError
        return value

    def add(self, value_1, value_2) -> float:
        return self.value_convertor_float(value_1) + self.value_convertor_float(value_2)

    def minus(self, value_1, value_2) -> float:
        return self.value_convertor_float(value_1) - self.value_convertor_float(value_2)

    def multiple(self, value_1, value_2) -> float:
        return self.value_convertor_float(value_1) * self.value_convertor_float(value_2)

    def division(self, dividend, divider) -> float:
        divider = self.value_convertor_float(divider)
        if divider == 0:
            raise ZeroDivisionError
        dividend = self.value_convertor_float(dividend)
        return dividend/divider

    def squaring(self, value) -> float:
        return self.value_convertor_float(value)**2

    def sq_root(self, value) -> float:
        return sqrt(self.value_convertor_float(value))


class CommonCalculator(AbsCalculator):
    pass


class ScientificCalculator(AbsCalculator):
    def log_func(self, value, base=10):
        if base > 0 and base != 1 and value > 0:
            return log(self.value_convertor_float(value), self.value_convertor_float(base))

    def exponentiation(self, value_1, value_2):
        return self.value_convertor_float(value_1) ** self.value_convertor_float(value_2)

    def module(self, value):
        return fabs(self.value_convertor_float(value))

    def sin_func(self, value):
        return sin(self.value_convertor_float(value))

    def cos_func(self, value):
        return cos(self.value_convertor_float(value))

    def tan_func(self, value):
        return tan(self.value_convertor_float(value))


class Graphs(AbsCalculator):

    def sin_graph(self):
        y = lambda x: sin(x)
        self.graph(y)

    def cos_graph(self):
        y = lambda x: cos(x)
        self.graph(y)

    def tan_graph(self):
        y = lambda x: tan(x)
        self.graph(y)

    def linear_func(self, k=1, b=0):    # линейая функция
        y = lambda x: self.value_convertor_float(k)*x + self.value_convertor_float(b)
        self.graph(y)

    def quadratic_func(self, a=1, b=0, c=0):    # квадратичная функция
        y = lambda x: self.value_convertor_float(a)*x + self.value_convertor_float(b)*x + self.value_convertor_float(c)
        self.graph(y)

    def graph(self, y):
        fig = subplots()
        x = linspace(-5, 5, 100)
        plot(x, y(x))
        show()


class Calculator:
    calculator = CommonCalculator()

    def __init__(self, status: str):
        if status == CalculatorUtil.status_off:
            print('Включите калькулятор')
            raise ValueError
        elif status == CalculatorUtil.status_on:
            mod = input(f'Выбирите тип калькулятора {CalculatorUtil.models()}: ') or CalculatorUtil.common_calc
            if mod == CalculatorUtil.common_calc:
                calculator = self.calculator
            elif mod == CalculatorUtil.graphs_calc:
                calculator = Graphs()
            elif mod == CalculatorUtil.scientific_calc:
                calculator = ScientificCalculator()

    @classmethod
    def change_mode(cls, mod: str):
        if mod == CalculatorUtil.graphs_calc:
            cls.calculator = Graphs()
        elif mod == CalculatorUtil.scientific_calc:
            cls.calculator = ScientificCalculator()


if __name__ == '__main__':
    status = input(f'Включить калькулятор, да({CalculatorUtil.status_on}) или нет ({CalculatorUtil.status_off}): ')
    cal = Calculator(status=status)
    cal.change_mode('sci')
#   print("cal.calculator: -----", cal.calculator, "Type of cal.calculator is: -----", type(cal.calculator))
    print(cal.calculator.add(value_1=2, value_2=3))
