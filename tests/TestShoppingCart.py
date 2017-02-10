import unittest
from models import shoppingcart, products, customer

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Stores a product, customer and a shopping cart
        author: Richie Van Sickle
        """
        self.battery = products.Product('9V Battery', 3.59)
        self.richie = customer.Customer("Richie", "1234 NSS Ave", "Nashville", "TN", "37811", "9014873143")
        self.richies_cart = shoppingcart.ShoppingCart(self.richie)

    def test_product_is_available(self):
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
        self.assertIsNotNone(self.battery.name)
        self.assertIsNotNone(self.battery.price)    
            
    def test_products_can_be_added_to_order(self):
        """
        Tests to make sure a product can be added to the order/shopping cart
        author: Richie Van Sickle
        """
        self.richies_cart.add_to_cart(self.battery)
        self.assertIn(self.battery, self.richies_cart.products)










# if __name__ == '__main__':
#     unittest.main()        
