import random

num = int(input())
colorList = []
for i in range(num):
    randNum = random.randint(1, 10)
    colorList.append(randNum)

print(colorList)


