class Order():
    def __init__(self, customer, payment_type):

        """
        Stores a single instance of relationship between
        :model:`customer`, :model:`payment_type`

        author: Whitney Cormack, Temporary Oysters
        # customer, payment type, order status
        """
        self.customer = customer
        self.payment_type = payment_type
        self.order_status = False


    def get_customer(self):
        """
        returns customer information
        """
        return self.customer

    def get_payment_type(self):
        """
        returns payment information
        """
        return self.payment_type

    def get_order_status(self):
        """
        returns order status
        False = not a complete order
        """
        return self.order_status

    def order_status_is_complete(self):
        """
        set order status
        True = complete order
        """
        self.order_status = True
        return self.order_status

        



