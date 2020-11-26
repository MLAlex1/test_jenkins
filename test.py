import unittest
from main import *

init_str = "abc"

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(transf_str(init_str).upper(), 'CBADE')

if __name__ == '__main__':
    unittest.main()