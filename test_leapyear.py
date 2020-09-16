from unittest import TestCase

from leapyear import is_leap


class Test(TestCase):
    def test_is_leap_non_leap_00(self):
        result = is_leap(1990)
        self.assertFalse(result)

    def test_is_leap_non_leap_standard(self):
        result = is_leap(1503)
        self.assertFalse(result)

    def test_is_leap_leap_standard(self):
        result = is_leap(1504)
        self.assertTrue(result)

    def test_is_leap_leap_00(self):
        result = is_leap(2000)
        self.assertTrue(result)