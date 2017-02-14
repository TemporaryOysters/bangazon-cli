import sys

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

    print("\nUser created!\n")  
    #ADD THE METHOD TO BRING UP MAIN MENU   
status = newUser()

#this code is designed to exit the program and should be called when the user selects option 7
def leave_bangazon():
    sys.exit("Thank you for visiting Bangazon!")
