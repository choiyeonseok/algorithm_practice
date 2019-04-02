import sys
sys.stdin = open("./inputs/input_string.txt", "r")


def solve(pattern, full):
    last = len(pattern) - 1
    now = last

    while now < len(full):
        if full[now - len(pattern) + 1:now + 1] == pattern:
            return 1
        elif full[now] in pattern[:-1]:
            dx = last - pattern.index(full[now])
            now += dx
        else:
            dx = len(pattern)
            now += dx
    return 0


T = int(input())
answer = []
for test_case in range(1, T+1):
    pattern = input()
    full = input()
    answer.append(solve(pattern, full))

for test_case in range(1, T+1):
    print(f"#{test_case}", answer[test_case - 1])
