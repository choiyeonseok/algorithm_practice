import sys
sys.stdin = open("./inputs/input_sumNumAr.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arrays =[]
    for i in range(M):
        arrays.append(list(map(int, input().split())))
    for i in range(1, M):
        for j in range(N):
            print(arrays[i - 1][j], "vs", arrays[i][0])
            if arrays[i - 1][j] > arrays[i][0]:
                arrays[i] = arrays[i - 1][:j] + arrays[i][:] + arrays[i - 1][j:]
        arrays[i] = arrays[i - 1] + arrays[i]

    ans = []
    print(arrays)
    for i in range(10):
        ans.append(arrays[-1][-1-i])

    print('#{0} {1}'.format(test_case, ans))