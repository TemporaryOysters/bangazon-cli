import unittest
from models import shoppingcart, products, customer

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Stores a product with name and price, customer and a shopping cart
        author: Richie Van Sickle
        """
        self.battery = products.Product('9V Battery', 3.59)
        self.toy = products.Product('Tonka Truck', 2.00)
        self.richie = customer.Customer("Richie", "1234 NSS Ave", "Nashville", "TN", "37811", "9014873143")
        self.richies_cart = shoppingcart.ShoppingCart(self.richie)
        """
        Adding products to cart
        """
        self.richies_cart.add_to_cart(self.battery)
        self.richies_cart.add_to_cart(self.toy)

    def test_product_can_be_created(self):
        """
        Tests to make sure a product is available 
        author: Mark Ellis
        """
        self.assertIsInstance(self.battery, products.Product)

    def test_product_has_correct_attributes(self):
        """
        Tests to make sure the product has the correct atrributes
        author: Mark Ellis
        """
        self.assertEqual(self.battery.name, "9V Battery")
        self.assertEqual(self.battery.price, 3.59)    
            
    def test_products_can_be_added_to_order(self):
        """
        Tests to make sure a product can be added to the order/shopping cart
        author: Richie Van Sickle
        """
        self.assertIn(self.battery, self.richies_cart.products)
        self.assertIn(self.toy, self.richies_cart.products)

    def test_can_get_total_price(self): 
        """
        Tests to make sure the total price of products
        is equal to the total price in the cart
        author: Richie Van Sickle
        """
        self.assertEqual(self.richies_cart.get_total_price(), 5.59)

"""
python -m unittest discover -s . -p "Test*.py" -v
"""