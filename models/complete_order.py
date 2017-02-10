class Order():
    def __init__(self, customer, payment_type, products, price_total):

    """
    Stores a single instance of relationship between
    :model:`customer`, :model:`payment_type`, :model:`products`, :model:`price_total`

    author: Whitney Cormack, Temporary Oysters
      # customer, payment type, products, total
    """
        self.customer = customer
        self.payment_type = payment_type
        self.products = products
        self.price_total = price_total


