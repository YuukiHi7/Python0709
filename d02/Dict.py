import random as r
print("比骰子")
flag = input("比大還是比小(比大請輸入 1, 比小請輸入 0)")
user = r.randint(1, 6) + r.randint(1, 6) + r.randint(1, 6)
pc = r.randint(1, 6) + r.randint(1, 6) + r.randint(1, 6)
if flag == 1:
    winner = "玩家" if user > pc else "電腦"
else:
    winner = "玩家" if user < pc else "電腦"
result = "比{0}, 玩家點數:{1} 電腦點數{2} 贏家:{3}"\
    .format("大" if flag == 1 else "小", user, pc, winner)
print(result)