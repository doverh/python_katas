import unittest
from prime import is_prime 

class testPrime(unittest.TestCase):
# tests Prime class
    def test_if_number_is_prime(self):
        self.assertTrue(is_prime(5))

if __name__ == "__main__":
    unittest.main()