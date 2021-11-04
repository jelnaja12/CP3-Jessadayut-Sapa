systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []
def showMenu():
    print("ไก่ทอด 35 บาท,","เป็ดทอด 45 บาท,","ปลาทอด 55 บาท,","ผักทอด 20 บาท")

def showBill():
    print("---- My Food----")
    totalMenu = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalMenu += int(menuList[number][1])
    print("Total : ",totalMenu)
showMenu()
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])
showBill()  