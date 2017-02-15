import sys
import sqlite3

sys.path.append('../bangazon-cli')
from models.payment_options import PaymentType
from models.customer import Customer
from models.complete_order import Order
from models.products import Product
from models.shoppingcart import ShoppingCart


#print main menu for user to navigate through app
def print_main_menu():
    print("""
        *********************************************************
        ** Welcome to Bangazon! Command Line Ordering System **
        *********************************************************
        Please choose a corresponding number of where you would like to navigate & then press Enter
        1. Create a customer account
        2. Choose active customer
        3. Create a payment option
        4. Add product to shopping cart
        5. Complete an order
        6. See product popularity
        7. Leave Bangazon!
    """)




#initial menu to create customer account
class CreateCustomer():
    #empty list to hold users and a blank status to hold the information
    #Author: Trent Hand, Temporary Oysters
    #empty list to hold users and a blank status to hold the information
    users = {}
    status = ""

    def newUser():
        print("press 'CTRL+C' to quit")
        createName = input("Enter Customer name: ")
        createAddress = input("Enter Street Address: ")
        createCity = input("Enter City: ")
        createState = input("Enter State: ")
        createPostalCode = input("Enter Postal Code: ")
        createPhoneNumber = input("Enter Phone Number: ")
        createEmail = input("Enter Email: ")

        print("\nUser created!\n")

        new_user = Customer(createName, createAddress, createCity, createState, createPostalCode, createPhoneNumber, createEmail)

        new_user.register_customer(new_user)
        #ADD THE METHOD TO BRING UP MAIN MENU
        print_main_menu()

        """ what does this line below mean? """
        # status = newUser()




# when user inputs "4", they are shown the list of bangazon products
class ProductMenu():
    def show_product_menu():
        print("add a product to the cart by it's corresponding number")
        print(" 1. product uno\n 2. product dos\n 3. product tres\n 4. done adding products\n")

    shopping_cart = []

    def show_list():
        print("Here's your list:")

        for item in shopping_cart:
            print(item)


#leave the app
def leave_bangazon():
    sys.exit("Thank you for visiting Bangazon!")




# main menu navigation
## start
if __name__ == '__main__':
    print_main_menu()

while True:
    nav_item = input("< ")

    if nav_item == "1":
        CreateCustomer.newUser()
        continue
    elif nav_item == "2":
        print("choose active customer")
        continue
    elif nav_item == "3":
        print("create a payment option")
        PaymentType.createPayment()
        continue
    elif nav_item == "4":
        ProductMenu.show_product_menu()
        continue
    elif nav_item == "5":
        print("you pressed 5 - complete an order")
        continue
    elif nav_item == "6":
        print("you pressed 6 - show product popularity")
        continue
    elif nav_item == "7":
        leave_bangazon()
    else:
        print_main_menu()





























