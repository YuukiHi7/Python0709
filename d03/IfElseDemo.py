def printBMI(h, w):
    bmi = w / ((h/100) ** 2)
    if (bmi > 23):
        result = "過重"
    elif(bmi < 18):
        result = "過輕"
    else:
        result = "正常"
    print("身高: %.1f 公尺 體重: %.1f 公頓 BMI: %.2f (%s)" % (h/100, w/1000, bmi,result))

printBMI(884800, 1565742080)