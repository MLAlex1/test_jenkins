import unittest
import numpy as np
from main import *

init_str = "abc"

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(transf_str(init_str).upper(), 'CBADE')

    def test_numpy(self):
        self.assertEqual(np.sum([1,2]), 3)

if __name__ == '__main__':
    unittest.main()