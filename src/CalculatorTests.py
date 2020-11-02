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


if __name__ == '__main__':
    unittest.main()
