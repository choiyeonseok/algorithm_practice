import sys
sys.stdin = open("./inputs/input_addingnumber.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    numL = list(map(int, input().split()))
    for m in range(M):
        t, add = map(int, input().split())
        numL = numL[:t] + [add] + numL[t:]
    print("#{0} {1}".format(test_case, numL[L]))

