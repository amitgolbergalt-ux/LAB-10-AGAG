import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
    def test_multiply(self, a, b):
        try:
            assert(mul(a,b) == a * b)
            return True
        except AssertionError:
            return False
    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_divide(self, a, b):
        try:
            assert(divide(a,b) == a / b)
            return True
        except AssertionError:
            return False
    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    def test_log_invalid_argument(self, a, b):
        try:
            log(a,b)
            return False
        except ValueError:
            return True

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
    def test_hypotenuse(self, a, b):
        try:
            assert(hypotenuse(a,b) == (a**2+b**2)**0.5)
            return True
        except AssertionError:
            return False
    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    def test_sqrt(self, a):
        try:
            assert(sqrt(a) == math.sqrt(a))
            return True
        except ValueError:
            return True
        except AssertionError:
            return False
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()