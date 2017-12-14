import random
suiji=random.randint(1,6)
print("-"*15+"猜猜看"+"-"*15)
temp=input("输入一个数字\n")
guess=int(temp)
a=1
while guess!=suiji and a<3:
    a = a + 1
    print(a)
    if guess>suiji:
        temp=input("大了重新输入:\n")
        guess=int(temp)
    else:
        temp=input("小了重新输入:\n")
        guess=int(temp)
if guess==suiji:
    print("恭喜答对了")
    print("对了游戏结束")
else:
    if guess>suiji:
        print("大了GG")
        print("答错了游戏结束")
    else:
        print("小了GG")
        print("答错了游戏结束")
