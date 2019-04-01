import sys
sys.stdin = open("./inputs/input_coloring.txt", "r")

T = int(input())
counts = []
for test_case in range(1, T + 1):
    num = int(input())
    pos_list = []
    for i in range(num):
        pos_list.append(list(map(int, input().split())))

    red = []
    blue = []
    for i in range(num):
        r1, c1, r2, c2 = pos_list[i][0], pos_list[i][1], pos_list[i][2], pos_list[i][3]
        for j in range(r2-r1+1):
            for k in range(c2-c1+1):
                if pos_list[i][-1] == 1:
                    red.append([r1+j, c1+k])
                elif pos_list[i][-1] == 2:
                    blue.append([r1+j, c1+k])

    count = 0
    for i in range(len(red)):
        for j in range(len(blue)):
            if red[i] == blue[j]:
                count += 1
    counts.append(count)

for test_case in range(1, T + 1):
    print(f'#{test_case}', counts[test_case - 1])

