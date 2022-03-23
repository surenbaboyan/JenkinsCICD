import unittest
from sitecreator import *

class TestCalculator(unittest.TestCase):
    def test_add_function(self):
        self.assertAlmostEqual(add_function(2,4),6)
        self.assertAlmostEqual(add_function(3,6),9)
    def test_sub_function(self):
        self.assertAlmostEqual(sub_function(2,4),-2)
        self.assertAlmostEqual(sub_function(6,3),3)
