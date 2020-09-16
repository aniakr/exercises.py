from unittest import TestCase

from ubs_zadanko import increment


class Test(TestCase):
    def test_increment_no_overflow(self):
        result=increment([5,6])
        self.assertEqual(result,[5,7])

    def test_increment_overflow_at_later_places(self):
        result=increment([5,9,9])
        self.assertEqual(result,[6,0,0])

    def test_increment_overflow_at_first_place(self):
        result=increment([9,9])
        self.assertEqual(result,[1,0,0])

    def test_increment_nine(self):
        result = increment([9,7])
        self.assertEqual(result, [9,8])