import sqlite3
from models import complete_order

class PaymentType():
    """PaymentType class allows users to create a payment option to purchase items from our CLI.

    Method List:
    -__init__

    Author: Trent Hand, Temporary Oysters
    """

    def __init__(self, payment_type, account_number):
        """
        A payment option only requires two arguments:
        -payment_type("visa", "mastercard", "amex", etc)
        -account_number("1234", "4556", etc)
        """
        cust = complete_order.Order()
        self.payment_type = payment_type
        self.account_number = account_number
        self.customer = cust.retrieve_active_customer_from_db()

    def get_payment_type(self):
        """returns the selected payment type"""
        return self.payment_type

    def add_payment_type(self):
        """
        Adds a payment type to the database
        """
        with sqlite3.connect('../bangazon.db') as conn:
            c = conn.cursor()
            command = """
            INSERT INTO PaymentOption
            VALUES (null, "{}", "{}", "{}")
            """.format(self.payment_type, self.account_number, self.customer)
            c.execute(command)


    def return_payment_type_from_db(self):
        """
        Returns a payment type from the database
        """
        with sqlite3.connect('bangazon.db') as dbget:
            c = dbget.cursor()
            command = """
            SELECT account_number
            FROM PaymentOption
            WHERE account_number = {}
            """.format(self.account_number)

            try:
                c.execute(command)
            except:
                return False

            account_info = c.fetchall()

            return True


    #create payment
    def createPayment():

        print(
            "\n"
            "******************************* \n"
            "**  Create a Payment Option  ** \n"
            "******************************* \n"
            )

        print("\nEnter Payment Type (e.g. AmEx, Visa, Checking)")
        payment_type = str(input(">"))

        print("\nEnter Account Number")
        acct_number = str(input(">"))

