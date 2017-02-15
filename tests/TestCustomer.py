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
        self.joey = customer.Customer('Joey', '787 East Silver St', 'Lebanon', 'Ohio', '35622', '5551231234', "j@j.com")
        
    def test_customer_acct_can_be_created(self):
        """
        Tests User, "Joey", has been created.
        """
        self.assertIsInstance(self.joey, customer.Customer)

    def test_customer_can_be_registered_to_db(self):
        """
        Tests User, "Joey", is added to Database.
        """
        self.joey.register_customer(self.joey)
        self.assertTrue(self.joey.customer_is_registered(self.joey))

    def test_customer_has_correct_attributes(self):
        """
        Tests that our users has created with the correct amount of attributes (6) & have value. 
        """
        self.assertEqual(self.joey.customer_name, 'Joey')
        self.assertEqual(self.joey.street_address, '787 East Silver St')
        self.assertEqual(self.joey.city, 'Lebanon')
        self.assertEqual(self.joey.state, 'Ohio')
        self.assertEqual(self.joey.postal_code, '35622')
        self.assertEqual(self.joey.phone_number, '5551231234')
        self.assertEqual(self.joey.email, 'j@j.com')

    def test_customer_can_change_status_to_active(self):
        """
        Tests that customer has ability to change active status to True/Active. 
        """
        self.assertTrue(self.joey.set_status_to_active())

    def test_customer_can_change_status_to_inactive(self):
        """
        Tests that customer has ability to change active status to False/Inactive. 
        """
        self.assertFalse(self.joey.set_status_to_inactive())

'''
run in CL within the test directory to RUN TESTS. 
python -m unittest discover -s . -p "Test*.py" -v
'''