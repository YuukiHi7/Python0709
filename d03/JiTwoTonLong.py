def calc(x, y):
    a = 2 * x
    b = y - a
    two = b / 2
    return x - two, two

ji, two = calc(83, 240)
print("雞:%d 兔:%d" % (ji, two))
