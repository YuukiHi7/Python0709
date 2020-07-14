def getBMI(h, w):
    bmi = w / ((h/100)**2)
    return bmi


bmi = getBMI(8848, 156000)
print("%.2f" % bmi)