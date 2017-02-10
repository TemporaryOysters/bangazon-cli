class Customer():
    """
    Customer class allows users to create a customer acct to make purchases with our CLI Tool.

    Method List:   
    - __init__ 
    - get_customer_name
    - get_street_address
    - get_city
    - get_state
    - get_postal_code
    - get_phone_number
    - get_status
    - set_status(self, new_status):

    Author: Joey Kirby, Temporary Oysters
    """

    def __init__(self, customer_name, street_address, city, state, postal_code, phone_number):
        """
        A new customer is created with required arguments.

        Arg List:
        - customer name
        - street address
        - city
        - state
        - postal_code
        - phone_number
        """
        self.customer_name = customer_name 
        self.street_address = street_address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.status = False

    def get_customer_name(self):
        """ Returns a customer's name """
        return self.customer_name

    def get_street_address(self):
        """ Returns a customer's street address """
        return self.street_address

    def get_city(self):
        """ Returns a customer's city """
        return self.city

    def get_state(self):
        """ Returns a customer's state """
        return self.state

    def get_postal_code(self):
        """ Returns a customer's postal code """
        return self.postal_code

    def get_phone_number(self):
        """ Returns a customer's phone number """
        return self.phone_number

    def get_status(self):
        """
        Returns a customer's active status. True = Active User, False = Non-active User
        Active User - Abilityto  make purchases
        """
        return self.status

    def set_status_to_active(self):
        """
        Set a Users Active status to True. 
        True = Active User
        Active User - Ability to make purchases
        """
        self.status = True
        return self.status

    def set_status_to_inactive(self):
        """
        Set a Users Active status False. 
        False = Inactive User
        Active User - Ability to make purchases
        """
        self.status = False
        return self.status