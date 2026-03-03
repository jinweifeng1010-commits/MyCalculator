
```python name=test_calculator.py
"""
Unit tests for MyCalculator
Test all calculator functions
"""

import unittest
from calculator import add, subtract, multiply, divide, power

class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions"""

    def test_add(self):
        """Test addition function"""
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(3.5, 2.5), 6.0)

    def test_subtract(self):
        """Test subtraction function"""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        """Test multiplication function"""
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-10, 5), -50)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        """Test division function"""
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Test division by zero error handling"""
        result = divide(10, 0)
        self.assertEqual(result, "Error: Cannot divide by zero!")

    def test_power(self):
        """Test power function"""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(10, 0), 1)

if __name__ == '__main__':
    unittest.main()
