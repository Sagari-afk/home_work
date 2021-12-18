from abc import ABC

from calculator.utils import CalculatorUtil

from math import sqrt, log, fabs, sin, cos, tan
from matplotlib.pyplot import subplots, plot, show, gca
import numpy as np


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
        if value >= 0:
            return sqrt(self.value_convertor_float(value))
        else:
            raise ValueError


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
        y = lambda x: np.sin(x)
        return self.graph(y)

    def cos_graph(self):
        y = lambda x: cos(x)
        return self.graph(y)

    def tan_graph(self):
        y = lambda x: tan(x)
        return self.graph(y)

    def linear_func(self, k=1, b=0):    # линейая функция
        y = lambda x: self.value_convertor_float(k)*x + self.value_convertor_float(b)
        return self.graph(y)

    def quadratic_func(self, a=1, b=0, c=0):    # квадратичная функция
        y = lambda x: self.value_convertor_float(a)*x*x + self.value_convertor_float(b)*x + self.value_convertor_float(c)
        return self.graph(y)

    def graph(self, y):
        fig = subplots()
        ax = gca()
        x = np.linspace(-5, 5, 100)
        plot(x, y(x))
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        show()


class Calculator:
    calculator = CommonCalculator()

    def __init__(self, status: str, mod: str):
        if status == CalculatorUtil.status_off:
            print('Включите калькулятор')
            raise ValueError
        elif status == CalculatorUtil.status_on:
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
    print(f'10 - 5 = {cal.calculator.minus(10, 5)}')

    cal.change_mode('sci')
    print(f'логорифм с основанием 2 числа 4 = {cal.calculator.log_func(4, 2)}')

    cal.change_mode('gra')
    print('график синусоиды:')
    cal.calculator.sin_graph()
