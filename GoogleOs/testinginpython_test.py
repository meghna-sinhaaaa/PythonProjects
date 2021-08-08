from testinginpython import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelave, Ada"
        expected = "Ada Lovelave"
        self.assertEqual(rearrange_name(testcase),expected)
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase),expected)
    def test_one_name(self):
        testcase = "Meghna"
        expected = "Meghna"
        self.assertEqual(rearrange_name(testcase),expected)
        
unittest.main()