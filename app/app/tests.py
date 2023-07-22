"""_sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """test the calc module."""
    
    
    def test_add_numbers(self):
        """TEst adding numbers togther."""
        
        res = calc.add(5,6)
        
        self.assertEqual(res, 11)
        
    def test_substract_numbers(self):
        """TEst substracting numbers. """
        
        res = calc.substract(10,5)
        
        self.assertEqual(res,5)
        