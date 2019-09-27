import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Checks for when passed a none argument"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        """checks normal functionality"""
        self.assertEqual(max_list_iter([1,2,23,2,34,8,99,102]),102)

        """checks if it works with negative numbers"""
        self.assertEqual(max_list_iter([-1,-3,-120]), -1)

        """checks how it handles empty list"""
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]), [3,2,1])

        """even number of items in the list"""
        self.assertEqual(reverse_rec([1, 2, 3, 4]), [4, 3, 2, 1])

        """only one item in the list"""
        self.assertEqual(reverse_rec([1]), [1])





    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        """find value 4"""
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

        """number outside of list (greater than)"""
        self.assertEqual(bin_search(11, 0, len(list_val) - 1, list_val), None)

        """number outside of list (less than)"""
        self.assertEqual(bin_search(-1, 0, len(list_val) - 1, list_val), None)





if __name__ == "__main__":
        unittest.main()

    
