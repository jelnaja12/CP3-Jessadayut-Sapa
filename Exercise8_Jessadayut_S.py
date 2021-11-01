usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "jel" and passwordInput == "123":
    print("------------------------")
    print("Welcome to Shop")
    print("------------------------")
    print("เลือกผลไม้ที่จะซื้อด้านล่าง")
    print("1.เงาะ โลละ 50 บาท")
    print("2.มะม่วง โลละ 90 บาท")
    print("3.ส้ม โลละ 60 บาท")
    rambutan = 50
    mango = 90
    orange = 60
    useSelect = int(input("เลือกผลไม้ :"))
    if useSelect == 1:
        selectRambutan = int(input("เลือกจำนวนที่ต้องการ :"))
        print("เงาะจำนวน",selectRambutan,"กิโล ราคา",rambutan*selectRambutan,"บาท")
    elif useSelect == 2:
        selectMango = int(input("เลือกจำนวนที่ต้องการ :"))
        print("มะม่วง",selectMango,"กิโล ทั้งหมดราคา",mango*selectMango,"บาท")
    elif useSelect == 3:
        selectOrang = int(input("เลือกจำนวนที่ต้องการ :"))
        print("ส้มจำนวน",selectOrang,"กิโล ทั้งหมดราคา",orange*selectOrang,"บาท")
else:
    print("Error")
print("ขอบคุณที่ใช้บริการ^^")








