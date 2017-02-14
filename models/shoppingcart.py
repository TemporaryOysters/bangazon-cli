class ShoppingCart():

    def __init__(self, user):
        """
        Initializes a user, an empty array of products, and
        sets the price total to zero
        author: Richie Van Sickle
        """
        self.user = user
        self.products = []
        self.price_total = 0

    def add_to_cart(self, product):
        """
        Allows the user to add product to cart and also
        returns the total price
        author: Richie Van Sickle
        """
        self.products.append(product)
        self.price_total = self.price_total + product.price

    def get_cart(self):
        """
        Returns the cart with list of products
        author: Richie Van Sickle
        """
        return self.products


    def cart_price_total(self):

        for product in products:
            self.price_total + product.price

        print(price_total)


    def get_total_price(self):
        """
        Returns the total price
        author: Whitney Cormack
        """
        return self.price_total
