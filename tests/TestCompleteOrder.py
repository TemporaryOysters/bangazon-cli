import unittest
import sys
sys.path.append("../")
from models import customer, payment_options, products, shoppingcart, complete_order



class TestCompleteOrder(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.joey = customer.Customer('Joey', '787 East Silver St', 'Lebanon', 'Ohio', '35622', '5551231234')
        self.joey_mastercard = payment_options.PaymentType("Mastercard", "acct1234")
        self.joeys_cart = shoppingcart.ShoppingCart("joey")
        self.joeys_cart.add_to_cart("puppies")


# test order is complete
    def test_order_is_complete(self):
      # customer, payment type, products, total

      self.joeysorder = complete_order.Order(self.joey, self.joey_mastercard, self.joeys_cart, self.joeys_cart.price_total)

      self.assertIsInstance(self.joeysorder, complete_order.Order)












