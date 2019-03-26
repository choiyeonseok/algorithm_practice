Case = int(input())
number = []
sum = 0
for i in range(Case):
    number.append(int(input()))

def OTTSum(sum, goal):
    if sum > goal:
        return 0
    if sum == goal :
        return 1
    now = 0
    for i in range(3):
        now += OTTSum(sum + 1 + i, goal)

    return now

for i in range(Case):
    print(OTTSum(sum, number[i]))

