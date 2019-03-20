
height = []
sum = 0

for i in range(len(height)):
    temp = int(input())
    height.append(temp)
    sum += temp

for i in range(len(height)):
    for j in range(i, len(height)):
        if sum - height[i] - height[j] == 100:
            for k in range(len(height)):
                if k == i or k == j:
                    continue
                print(height[k])




