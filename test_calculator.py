import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.addition(1, 1), 2)
        self.assertEqual(calculator.addition(3432, 43254), 46686)
        self.assertEqual(calculator.addition(1, 0), 1)
        self.assertEqual(calculator.addition(-2, 1), -1)
        self.assertEqual(calculator.addition(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(1, 1), 0)
        self.assertEqual(calculator.subtraction(1, 2), -1)
        self.assertEqual(calculator.subtraction(-1, -4), 3)
        self.assertEqual(calculator.subtraction(-3, 1), -4)

    def test_division(self):
        self.assertEqual(calculator.division(-3, 4), -.75)
        self.assertEqual(calculator.division(-2, 1), -2)
        self.assertEqual(calculator.division(1, 0), "error: divide by zero")
        self.assertEqual(calculator.division(25, 5), 5)
        self.assertEqual(calculator.division(-3, -3), 1)
        self.assertEqual(calculator.division(1, -2), -.5)
        self.assertEqual(calculator.division(0, 4), 0)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(-3, 4), -12)
        self.assertEqual(calculator.multiplication(-2, -1), 2)
        self.assertEqual(calculator.multiplication(3, -5), -15)
        self.assertEqual(calculator.multiplication(5, 1.2), 6)
        self.assertEqual(calculator.multiplication(5, -1.2), -6)
        self.assertEqual(calculator.multiplication(0, 4), 0)
        self.assertEqual(calculator.multiplication(0, 0), 0)


if __name__ == "__main__":
    unittest.main()







