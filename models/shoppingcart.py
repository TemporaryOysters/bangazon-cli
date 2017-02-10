class ShoppingCart():

    def __init__(self, user):
        """
        Initializes a user, a message lets the user know there 
        are no products added yet, and price total set to zero
        author: Richie Van Sickle
        """
        self.user = user
        self.products = "No products have been added yet"
        self.price_total = 0

    def add_to_cart(self, product):
        """
        Allows the user to add the product to cart
        author: Richie Van Sickle
        """
        self.products = []
        self.products.append(product)

    def get_cart(self):
        """
        Returns the cart with list of products
        author: Richie Van Sickle
        """
        return self.products

    def cart_total_price(self):
        """
        Returns the total price of products in the cart
        author: Whitney Cormack
        """
        for product in products:
          self.price_total + product.self

    def get_total_price(self):
        """
        Returns the total price
        author: Whitney Cormack
        """
        return self.price_total
