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
    def setUp(self):
        """
        Sets up a Test User, "Joey", so we can test if our code is behaving as expected.
        """
        self.joey = customer.Customer('Joey', '787 East Silver St', 'Lebanon', 'Ohio', '35622', '5551231234')
        self.joey_mastercard = payment_options.PaymentType("Mastercard", "acct1234")
        self.joeysorder = complete_order.Order(self.joey, self.joey_mastercard)


    def test_order_is_complete(self):
        """
        Tests that our user has created an order which includes correct attributes with assigned values.
        An Order is 'complete' when it has attributes and values for a customer, a payment type, products in cart, and cart total cost.
        """
        self.assertIsInstance(self.joeysorder, complete_order.Order)


    def test_can_get_order_status(self):
        self.assertFalse(self.joeysorder.get_order_status())

    def test_can_set_order_status_to_complete(self):
        self.assertTrue(self.joeysorder.order_status_is_complete())






