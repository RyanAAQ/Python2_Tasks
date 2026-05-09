from unittest import TestCase
from promotional_code import *

class TestPromoCode(TestCase):
    
    def test_the_promo_code_returns_ten_percent_discount(self):
        self.assertEqual(discount("item", 100, "save10"), 90)
        
    def test_that_the_promo_code_returns_fifty_percent_discount(self):
        self.assertEqual(discount("item", 100, "halfoff"), 50)
             
    def test_if_no_promo_code_is_entered(self):
        self.assertEqual(discount("item", 100, ""), 100)
