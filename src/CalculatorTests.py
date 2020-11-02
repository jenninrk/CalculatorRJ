import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEquals(calculator.result, 4)

    def test_addition(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 1), 2)

    def test_square_root(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqrt(25), 5)

    def test_subtraction(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(3, 2), 1)


if __name__ == '__main__':
    unittest.main()
