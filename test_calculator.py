import unittest
from calculator import Calculator
 
class TddCalculator(unittest.TestCase):
 
    def test_calculator(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)
 
 
# if __name__ == '__main__':
#     unittest.main()