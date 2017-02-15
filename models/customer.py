import sqlite3

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

    def __init__(self, customer_name, street_address, city, state, postal_code, phone_number, email, status=None):
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
        self.email = email
        self.status = 0

    def get_customer_name(self):
        """ Returns a customer's name """
        return self.customer_name

    def get_active_customer(self):
        """ Returns active customer """
        return self.active_customer

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

    def get_email(self):
        """ Returns a customer's email """
        return self.email

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
        with sqlite3.connect('bangazon.db') as conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Customer
                SET status=1
                WHERE name='{}'
            """.format(self.get_customer_name()))      
        self.status = 1
        return self.status

    def set_status_to_inactive(self):
        """
        Set a Users Active status 0 (False). 
        0 = Inactive User
        Active User - Ability to make purchases
        """
        with sqlite3.connect('bangazon.db') as conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE Customer
                SET status=0
                WHERE name='{}'
            """.format(self.get_customer_name()))     
        self.status = 0
        return self.status

    def register_customer(self, user):
        """
        Registers customer and stores info into DB.
        """
        print("****** USER OBJ", user)
        if user.customer_is_registered(user):
            print("Customer is already registered")
        else:
            with sqlite3.connect('bangazon.db') as roncon:
                cursor = roncon.cursor()

                cursor.execute("""
                INSERT INTO Customer VALUES (null, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
                """.format( 
                            user.get_customer_name(),
                            user.get_street_address(),
                            user.get_city(),
                            user.get_state(),
                            user.get_postal_code(),
                            user.get_phone_number(),
                            user.get_email(),
                            user.get_status()
                            ))


    def customer_is_registered(self, user):
        """
        Checks DB to see if User is already registered / stored in DB.
        """
        with sqlite3.connect('bangazon.db') as llamaRama:
            cursor = llamaRama.cursor()


            cursor.execute("""
                SELECT * FROM Customer
                WHERE name='{}'
            """.format(user.get_customer_name()))
            selected_customer = cursor.fetchall()
            if len(selected_customer) > 0:
                return True
            else:
                False