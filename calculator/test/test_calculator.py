from unittest import TestCase, main
from calculator.main import  Calculator, CommonCalculator
from calculator.utils import CalculatorUtil


class TestCommonCalculator(TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"setUpClass\n{'=' * 50}")
        cls.calculator = Calculator('on', 'common')

    def test_add(self):
        self.assertEqual(self.calculator.calculator.add(4, 7), 11)

    def test_minus(self):
        self.assertEqual(self.calculator.calculator.minus(10, 2), 8)

    def test_multiple(self):
        self.assertEqual(self.calculator.calculator.multiple(10, 2), 20)

    def test_division(self):
        self.assertEqual(self.calculator.calculator.division(10, 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as e:
            self.calculator.calculator.division(5, 0)
        self.assertEqual(ZeroDivisionError, e.exception.args[0])


if __name__ == '__main__':
    main()
