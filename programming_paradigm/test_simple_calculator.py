import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-9, 10), 1)
        self.assertEqual(self.calc.add(4.1, 0.1), 4.2)
        
    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multipy(4,3), 12)
        self.assertEqual(self.calc.multipy(-9,1), -9)
        self.assertEqual(self.calc.multipy(1,-1), -1)
        self.assertEqual(self.calc.multipy(0,9), 0)
        
    def test_subtraction(self):
        """test subtraction method"""
        self.assertEqual(self.calc.subtract(7 ,2), 5)
        self.assertEqual(self.calc.subtract(-2,-6), -8)
        self.assertEqual(self.calc.subtract(8, 12), -4)
        self.assertEqual(self.calc.subtract(7, 3), 4)
    def test_division(self):
        """Test for division method"""
        self.assertEqual(self.calc.divide(9,3), 3)
        self.assertEqual(self.calc.divide(49,7), 7)
        self.assertEqual(self.calc.divide(7, 6), 1.167)
        self.assertEqual(self.calc.divide(-5 , 7), -0.7142)
