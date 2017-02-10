import unittest 
import sys
sys.path.append("../")
from models import customer

class TestCustomer(unittest.TestCase):
    """
    TestCustomer tests the creation of a customer and it's methods.

    Method List:   
    -test_customer_acct_can_be_created
    -test_customer_has_correct_attributes
    -test_customer_can_change_active_status

    Argument List:  unittest.TestCase gives the unittest model knowledge on what to test.

    Author: Joey Kirby, Temporary Oysters
    """

    @classmethod
    def setUpClass(self):
        """
        Sets up a Test User, "Joey", so we can TEST if our code is behaving as expected.
        """
        self.joey = customer.Customer('Joey', '787 East Silver St', 'Lebanon', 'Ohio', '35622', '5551231234')
        
    def test_customer_acct_can_be_created(self):
        """
        Sets up a Test User, "Joey", so we can TEST if our code is behaving as expected.
        """
        self.assertIsInstance(self.joey, customer.Customer)

    def test_customer_has_correct_attributes(self):
        """
        Tests that our users has created with the correct amount of attributes (6) & have value. 
        """
        self.assertIsNotNone(self.joey.customer_name)
        self.assertIsNotNone(self.joey.street_address)
        self.assertIsNotNone(self.joey.city)
        self.assertIsNotNone(self.joey.state)
        self.assertIsNotNone(self.joey.postal_code)
        self.assertIsNotNone(self.joey.phone_number)

    def test_customer_can_change_active_status(self):
        """
        Tests that customer has ability to change active status. 
        """
        self.joey.status = True
        self.assertTrue(self.joey.status)

        self.joey.status = False
        self.assertFalse(self.joey.status)

'''
run in CL within the test directory to RUN TESTS. 

python -m unittest discover -s . -p "Test*.py" -v

'''

