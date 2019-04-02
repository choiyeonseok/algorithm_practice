import sys
sys.stdin = open("./inputs/input_deletetwice.txt", "r")


def solve(target):
    n = len(target)

    for i in range(n - 1):
        if target[i] == target[i + 1]:
            return solve(target[:i] + target[i+2:])

    return len(target)


T = int(input())
answer = []
for test_case in range(1, T + 1):
    target = input()
    answer.append(solve(target))

for i in range(T):
    print(f'#{i + 1}', answer[i])
