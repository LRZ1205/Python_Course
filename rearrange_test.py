from rearrange import arrange_name
import unittest

class TestRearrange (unittest.TestCase):
    def test_basic(self):
        testcase = "Luis, Romero"
        expected = "Romero Luis"
        self.assertEqual(arrange_name(testcase),expected)
    def test_double_name (self):
        testcase = "Cristina L., Bautista"
        excepted = "Bautista Cristina L."
        self.assertEqual(arrange_name(testcase),excepted)
    def test_one_name (self):
        testcase = "Voltaire"
        excepted = "Voltaire"
        self.assertEqual(arrange_name(testcase),excepted)
unittest.main()