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
        self.payment_type = payment_type
        self.account_number = account_number
