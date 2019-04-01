import sys
sys.stdin = open("./inputs/input.txt", "r")

T = int(input())
answer = []
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    Max_sum = 0
    Min_sum = 100000000000

    for i in range(N - M + 1):
        partsum = 0
        for j in range(M):
            partsum += M_list[i + j]
        if partsum > Max_sum:
            Max_sum = partsum
        if partsum < Min_sum:
            Min_sum = partsum
    ans = Max_sum - Min_sum
    answer.append(ans)

print(answer)
for test_case in range(1, T+1):
    print(f"#{test_case}", answer[test_case - 1])






