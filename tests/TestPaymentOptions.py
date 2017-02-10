import unittest
import sys
sys.path.append("../")
from models import payment_options



class TestPaymentOptions(unittest.TestCase):
    """
    TestPaymentOptions tests the creation of a payment option and it's methods.

    Method List:
    -test_user_can_register_payment_option
    -test_payment_option_has_correct_attributes

    Argument List: unittest.TestCase gives the unittest model knowledge on what to test.

    Author: Trent Hand, Temporary Oysters
    """  
    @classmethod
    def setUpClass(self):
        """Sets up a test payment option "payment" so we can TEST if our code will add the payment option.
        """

        self.payment = payment_options.PaymentType("visa", "1234")

        """
        Tests that "payment" is an Instance of PaymentType
        """
    def test_user_can_register_payment_option(self):
        self.assertIsInstance(self.payment, payment_options.PaymentType)

        """
        Tests that the attributes in "payment" are corresponding with the correct values they are associated with.
        """
    def test_payment_option_has_correct_attributes(self):
        self.assertEqual(self.payment.payment_type, "visa")
        self.assertEqual(self.payment.account_number, "1234")

#run tests in the tests directory
#python -m unittest discover -s . -p "Test*.py" -v
