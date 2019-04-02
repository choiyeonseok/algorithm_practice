import sys
sys.stdin = open("./inputs/input_binaryfind.txt", "r")


def solve(P, Target):
    start = 1
    end = P
    count = 0
    while 1:
        count += 1
        mid = (start + end) // 2
        if mid < Target:
            start = mid
        elif mid > Target:
            end = mid
        elif mid == Target:
            break
    return count


T = int(input())
answer = []
for test_case in range(1, T+1):
    P, A, B = map(int, input().split())
    count_A = solve(P, A)
    count_B = solve(P, B)
    if count_A > count_B:
        answer.append('B')
    elif count_A < count_B:
        answer.append('A')
    else:
        answer.append(0)


for test_case in range(1, T+1):
    print(f"#{test_case}", answer[test_case - 1])
