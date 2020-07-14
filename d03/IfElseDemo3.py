def calcBMI():
    h = float(input("你的身高(cm): "))
    w = float(input("你的體重(kg): "))
    bmi = w / ((h/100)**2)
    result = "正常" if 18 < bmi <= 23 else "過高" if bmi > 23 else "過低"
    print("身高: %.1f cm  體重: %.1f kg  BMI: %.2f (%s)" % (h, w, bmi,result))

def menu():
    print("BMI計算系統")
    print("----------")
    print("1. 輸入身高體重")
    print("2. 離開系統")
    id = int(input("請選擇: "))
    if id == 1:
        print("您選擇的是1")
        calcBMI()
        input("按下任意鍵繼續")
        menu()
    elif id == 2:
        print("您選擇的是2")
        print("感謝您的使用")

    else:
        print("輸入錯誤")
        menu()
menu()