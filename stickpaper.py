import sys
sys.stdin = open("./inputs/input_stickpaper.txt", "r")
#memoization을 활용해라
#DP문제


def solve(stack_cal, n):
    if n <= len(stack_cal):
        return stack_cal[n]
    else:
        for i in range(len(stack_cal), n + 1):
            stack_cal.append(stack_cal[len(stack_cal) - 1] + 2 * stack_cal[len(stack_cal) - 2])
        return stack_cal[n]


T = int(input())
for test_case in range(1, T+1):
    nn = int(input())
    n = nn // 10
    stack_cal = [1, 1]
    ans = solve(stack_cal, n)
    print('#{0} {1}'.format(test_case, ans))

