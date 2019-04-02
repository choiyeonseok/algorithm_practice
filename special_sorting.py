import sys
sys.stdin = open("./inputs/input_specialList.txt", "r")


def swap(slist, a, b):
    temp = slist[b]
    slist[b] = slist[a]
    slist[a] = temp


def solve(tlist):
    n = len(tlist)
    maxi = 0
    maxi_idx = 0
    mini = 10000000000
    mini_idx = 0
    if n <= 1:
        return tlist
    for i in range(n):
        if tlist[i] > maxi:
            maxi = tlist[i]
            maxi_idx = i
    swap(tlist, 0, maxi_idx)
    for i in range(n):
        if tlist[i] < mini:
            mini = tlist[i]
            mini_idx = i
    swap(tlist, 1, mini_idx)

    return tlist[:2] + solve(tlist[2:])


T = int(input())
answer = []
for test_case in range(1, T+1):
    N = int(input())
    targetList = list(map(int, input().split()))
    targetList = solve(targetList)
    answer.append(targetList)

for test_case in range(1, T+1):
    print(f"#{test_case}", end=' ')
    for i in range(10):
        print(answer[test_case - 1][i], end=' ')
    print()
