from tkinter import *
import math

def leftClickButton(event):
    BMI = int(textBoxWeight.get())/math.pow(int(textBoxHeight.get())/100,2)
    if BMI > 30:
        bmi = "อ้วนมาก"
    elif BMI > 25.0 and BMI < 29.9:
        bmi = "อ้วน"
    elif BMI > 23.0 and BMI < 24.9:
        bmi = "น้ำหนักเกิน"
    elif BMI > 18.6 and BMI < 22.9:
        bmi = "น้ำหนักปกติ"
    elif BMI < 18.5:
        bmi = "ผอมเกินไป"
    labelResult.configure(text = bmi)

mainWindow = Tk()
labelHeight = Label(mainWindow,text = "ส่วนสูง(cm.)").grid(row = 0,column = 0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row = 0,column = 1)
labelWeight = Label(mainWindow,text = "น้ำหนัก(Kg.)").grid(row = 1,column = 0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row = 1,column = 1)
calculateButton = Button(mainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row = 2,column = 0)
labelResult = Label(mainWindow,text = "ผลลัพธ์")
labelResult.grid(row = 2,column = 1)
mainWindow.mainloop()



