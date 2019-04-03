import sys
sys.stdin = open("./inputs/input_tornument.txt", "r")


def fight(s1, s2):
    if case[s1] == 1 and case[s2] == 2:
        return s2
    elif case[s1] == 2 and case[s1] == 1:
        return s1
    elif case[s1] == 1 and case[s2] == 3:
        return s1
    elif case[s1] == 3 and case[s2] == 1:
        return s2
    elif case[s1] == 2 and case[s2] == 3:
        return s2
    elif case[s1] == 3 and case[s1] == 2:
        return s1
    else:
        return s1


def solve(a, b):
    m = (a + b) // 2
    if b - a == 0:
        return a
    elif b - a == 1:
        return fight(a, b)
    else:
        res1 = solve(a, m)
        res2 = solve(m + 1, b)
        return fight(res1, res2)


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    case = [0] + list(map(int, input().split()))
    answer = solve(1, n)
    print('#{0} {1}'.format(test_case, answer))