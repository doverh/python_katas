import unittest
#Import main class to test
from Katas import isNumberEven

class Test_Katas(unittest.TestCase):

    def test(self):
        self.assertTrue( isNumberEven(3),"This number is even")

if __name__ == '__main__':
   unittest.main()