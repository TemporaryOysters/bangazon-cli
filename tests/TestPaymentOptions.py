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

        self.payment = payment_options.PaymentType("visa", "1234", 1)

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

    """
    These tests confirm that payment types can be added to the database.

    Method List:
    -test_payment_type_can_be_added_to_database
    -test_added_payment_option_has_correct_attributes

    Argument List: unittest.TestCase provides necessary model information for testing.

    Author: Mark Ellis, Temporary Oysters
    """
    def test_payment_type_can_be_added_to_database(self):
        self.test_type = payment_options.PaymentType("MC", "1234567890123456", 4)
        self.test_type.add_payment_type()
        self.assertTrue(self.test_type.return_payment_type_from_db)

        