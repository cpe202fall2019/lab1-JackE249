import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

        loc2 = Location("Home", 0, 0)
        self.assertEqual(repr(loc2), "Location('Home', 0, 0)")

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = loc1

        """actual values are equal"""
        self.assertEqual(loc1 == loc2, True)

        """reference variables are equal"""
        self.assertEqual(loc1 == loc3, True)
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
