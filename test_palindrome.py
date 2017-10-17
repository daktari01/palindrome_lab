import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    """Tests the is_palindrome function"""
    def test_input_is_string(self):
        self.assertEqual(is_palindrome([2, 4]), False)
        self.assertEqual(is_palindrome(8), False)
        
    def test_palindrome(self):
        self.assertEqual(is_palindrome('madam'), True)
        self.assertEqual(is_palindrome('English'), False)
    
        
if __name__ == '__main__':
    unittest.main()