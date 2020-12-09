import unittest
from main import Range

class TestRangeKata(unittest.TestCase):

    def test_init(self):
        range = "[2, 6)" # 2, 3, 4, 5
        x = Range(range)
        self.assertEqual(x.interval, range)

    def test_contains_integers(self):
        range = Range("[2, 6)")
        self.assertTrue(range.contains_integers("{2, 4}"))

    def test_get_all_points(self):
        range = Range("[2, 12)")
        self.assertEqual(range.get_all_points(), "{2,3,4,5,6,7,8,9,10,11}")

    def test_contains_range(self):
        range = Range("[3, 5)")
        self.assertFalse(range.contains_range("[2,10)"))

    def test_end_points(self):
        range = Range("(2,6)")
        self.assertEqual(range.end_points(), "{3,5}")

    def test_overlaps_range(self):
        range = Range("[2, 10)")
        self.assertTrue(range.overlaps_range("[3,5)"))

    def test_equals(self):
        range = Range("[3,5)")
        self.assertFalse(range.equals("[2,10)"))