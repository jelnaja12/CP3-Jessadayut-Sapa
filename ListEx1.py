menuList = []
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.upper() == "EXIT":
        break
    else:
        price1 = 0
        menuPrice = int(input("Price :"))
        menuList.append([menuName,menuPrice])
    price1 += menuPrice

def showBill():
    print("---- My FoodS ----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number])
        totalPrice += price1
    print("Total : "totalPrice)



showBill()

