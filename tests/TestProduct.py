import unittest
import sys
sys.path.append("../")
from models import product


class TestProduct(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.battery = product.Product('9V Battery', 3.59)

    def test_product_is_available(self):
        self.assertIsInstance(self.battery, product.Product)

    def test_product_has_correct_attributes(self):
        self.assertIsNotNone(self.battery.name)
        self.assertIsNotNone(self.battery.price)

#python -m unittest discover -s . -p "tests/Test*.py" -v