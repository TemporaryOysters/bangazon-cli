#COMMAND LINE MENU - OPTIONS 1 & 2

#Author: Trent Hand, Temporary Oysters
#empty list to hold users and a blank status to hold the information
users = {}
status = ""

#initial menu to
def displayMenu():
    status = input("Are you a registered user? y/n? Press q to quit: ")
    if status == "y":
        #calls the oldUser() function below
        oldUser()
    elif status == "n":
        #prompts the user to create a new account by calling the function below
        newUser()
    return status

def newUser():
    createLogin = input("Create login name: ")

    if createLogin in users: # check if login name exists
        print("\nLogin name already exist!\n")
        #these inputs will need to be passed into a Customer object from customer.py
    else:
        createPassw = input("Create password: ")
        createName = input("Enter Customer name: ")
        createAddress = input("Enter Street Address: ")
        createCity = input("Enter City: ")
        createState = input("Enter State: ")
        createPostalCode = input("Enter Postal Code: ")
        createPhoneNumber = input("Enter Phone Number: ")
        users[createLogin] = createPassw # add login and password

        print("\nUser created!\n")

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    # check if user exists and login matches password
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")

while status != "q":
#keeps the user in the program until they type "q"
    status = displayMenu()