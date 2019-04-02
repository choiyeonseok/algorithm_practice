import sys
sys.stdin = open("./inputs/input_perfectstring.txt", "r")


def solve(tlist):
    n = len(tlist)
    mid = n // 2
    for i in range(mid):
        if tlist[i] != tlist[-1-i]:
            return 0
    return 1


T = int(input())
answer = []
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    input_mat = []
    full = []
    for i in range(N):
        row = input()
        input_mat.append(row)
        start = 0
        while start+M <= N:
            full.append(row[start:start+M])
            start += 1

    input_mat_T =list(zip(*input_mat))
    full_T = []
    for i in range(N):
        start = 0
        while start+M <= N:
            full_T.append(input_mat_T[i][start:start+M])
            start += 1

    for i in range(len(full)):
        if solve(full[i]) == 1:
            answer.append(full[i])
        if solve(full_T[i]) == 1:
            refine = ''.join(full_T[i])
            answer.append(refine)


for test_case in range(1, T+1):
    print(f"#{test_case}", answer[test_case - 1])
