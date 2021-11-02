def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return login()
def showMenu():
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return selectMunu()
def selectMunu():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vat()
    elif userSelected == 2:
        return price()
    else:
        return selectMunu()
def vat():
    price = int(input("Price (THB) : "))
    vat = 7
    result = price + (price * vat / 100)
    print(result)
def price():
    vat = 7
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    total = price1 + price2
    result = total + (total * vat / 100)
    print(result)

login()























"""
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1 + price2)
"""