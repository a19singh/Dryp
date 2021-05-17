import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.addition(10, 5), 15)  #addition of two positive numbers
        self.assertEqual(calculator.addition(-5, 2), -3)  #one positive and other negative, where negative > positive
        self.assertEqual(calculator.addition(-10,-10), -20)  #addition of two negative numbers
        self.assertEqual(calculator.addition(10, -5), 5)  #one positive and other negative, where positive > negative 

    def test_sub(self):
        self.assertEqual(calculator.subtraction(10, 5), 5)  #subtraction of two positive numbers
        self.assertEqual(calculator.subtraction(-5, 2), -7)  #one positive and other negative, where negative > positive
        self.assertEqual(calculator.subtraction(-10,-10), 0)  #subtraction of two negative numbers
        self.assertEqual(calculator.subtraction(10, -5), 15)  #one positive and other negative, where negative > positive

    def test_mul(self):
        self.assertEqual(calculator.multiplication(10, 5), 50)  #multiplication of two positive numbers
        self.assertEqual(calculator.multiplication(-5, 2), -10)   #one positive and other negative
        self.assertEqual(calculator.multiplication(-10,-10), 100)  #multiplication of two negative numbers
        self.assertEqual(calculator.multiplication(5, 0), 0)   #multiplication by zero
    
    def test_div(self):
        self.assertEqual(calculator.division(10, 5), 2) #divison without remainder
        self.assertEqual(calculator.division(5, 2), 2.5)  #divison having remainder
        self.assertEqual(calculator.division(-10,-10), 1)  #divison of two negative numbers
        self.assertEqual(calculator.division(10, -5), -2) #divison of one positive and one negative number
        self.assertRaises(ValueError, calculator.division, 10, 0) #check for divide by zero error

if __name__ == "__main__":
    unittest.main()