import sqlite3

class Order():
    def __init__(self):

        """
        Stores a single instance of relationship between
        :model:`customer`, :model:`payment_type`
        author: Whitney Cormack, Temporary Oysters
        # customer, payment type
        """
        self.customer = self.retrieve_active_customer_from_db();
        self.payment_type = self.retrieve_payment_type_from_db();

    def get_customer(self):
        """ returns active customer on order """
        return self.customer

    def get_payment_type(self):
        """ returns active customer's payment on order """
        return self.payment_type

    def retrieve_active_customer_from_db(self):
        """ returns active customer on order which will be set to self.customer """
        with sqlite3.connect('../bangazon.db') as roncon:
            cursor = roncon.cursor()

            cursor.execute("""
                SELECT * FROM Customer
                WHERE status = 1
            """)
            selected_customer = cursor.fetchone()
            # print("$$$$$$$$$$$$ selected_customer", selected_customer)
            return selected_customer[0]

    def retrieve_payment_type_from_db(self):
        """ returns customer's payment type on order """
        with sqlite3.connect('../bangazon.db') as roncon:
            cursor = roncon.cursor()

            cursor.execute("""
                SELECT * FROM PaymentOption
                WHERE customer='{}'
            """.format(self.get_customer()
                ))
            selected_payment_option = cursor.fetchall()
            # print("****** Selected_payment_option:", selected_payment_option, self.get_customer())
            if len(selected_payment_option) > 0:
                return selected_payment_option[0][0]
            else:
                return False
            

    def add_order_to_db(self, order):
        """ 
        Adds order to DB
        w/ 
        customerId & payment_typeId
        """
        if order.is_order_in_db(order):
            print("customer is already registered")
        else:
            with sqlite3.connect('../bangazon.db') as roncon:
                cursor = roncon.cursor()

                try: 
                    cursor.execute("""
                    INSERT INTO BangOrder VALUES (null, '{}', '{}')
                    """.format( 
                                order.get_customer(),
                                order.get_payment_type()
                                ))
                except sqlite3.OperationalError:
                    print("Error")


    def is_order_in_db(self, order):
        """ 
        Checks if Order has already been created in DB by customerId & payment_typeId
        &
        Returns True or False
        """
        with sqlite3.connect('../bangazon.db') as llamaRama:
            cursor = llamaRama.cursor()

            cursor.execute("""
                SELECT * FROM BangOrder
                WHERE customer='{}'
                AND payment_option='{}'
            """.format(order.get_customer(),
                       order.get_payment_type()))
            selected_order = cursor.fetchall()
            if len(selected_order) > 0:
                return True
            else:
                False