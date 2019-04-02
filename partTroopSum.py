import sys
sys.stdin = open("./inputs/input_parttroop.txt", "r")

T = int(input())
counts = []
origin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
length = len(origin)
answer = []
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    count = 0
    for i in range(1 << length):
        sum = 0
        partTroop = []
        for j in range(length):
            if i & (1 << j):
                partTroop.append(origin[j])
                sum += origin[j]
        if len(partTroop) == N and sum == K:
            count += 1
    counts.append(count)


for test_case in range(1, T + 1):
    print(f'#{test_case}', counts[test_case - 1])





