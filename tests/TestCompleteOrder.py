import unittest
import sys
sys.path.append("../")
from models import customer, payment_options, products, shoppingcart, complete_order



class TestCompleteOrder(unittest.TestCase):

    """
    TestCompleteOrder tests the Order is 'complete' with the appropriate attributes.
    Method List:
    -test_order_is_complete
    Argument List:  unittest.TestCase gives the unittest model knowledge on what to test.
    Author: Whitney Cormack, Temporary Oysters
    """

    @classmethod
    def setUpClass(self):
        """
        Sets up a Test User, "Joey", so we can test if our code is behaving as expected.
        """
        self.joe = customer.Customer('Joe llama', '787 Mulberry St', 'Nashville', 'TN', '35622', '5551231234', 'jllama@j.com')
        self.joe.register_customer(self.joe)
        self.joe.set_status_to_active()
        self.joe_mastercard = payment_options.PaymentType("Mastercard", "1234", 5)
        self.joe_mastercard.add_payment_type()
        self.joes_cart = shoppingcart.ShoppingCart("joe")
        self.puppies = products.Product("puppies", 3)
        self.joes_cart.add_to_cart(self.puppies)
        self.joes_order = complete_order.Order()


    def test_order_is_complete(self):
        """
        Tests that our user has created an order which includes correct attributes with assigned values.
        An Order is 'complete' when it has attributes and values for a customer, a payment type, products in cart, and cart total cost.
        """

        self.assertIsInstance(self.joes_order, complete_order.Order)

    def test_order_has_proper_attributes(self):
        """
        Tests order is able to add correct CUSTOMER & PAYMENT TYPE attributes.
        """
        self.assertIsNotNone(self.joes_order.customer)
        print("HEYYYY LOOK AT ME!", self.joes_order.payment_type)
        self.assertIsNotNone(self.joes_order.payment_type)

    def test_order_can_be_added_to_db(self):
        """
        Tests that orders can be stored in our DB.
        """
        self.joes_order.add_order_to_db(self.joes_order)
        self.assertTrue(self.joes_order.is_order_in_db(self.joes_order))

        