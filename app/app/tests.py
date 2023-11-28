"""
Sample test
"""
from django.test import SimpleTestCase
from . import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""
    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)
        self.assertEquals(res, 11)
