import sys
sys.stdin = open("./inputs/input_checksigns.txt", "r")


def solve(sent):
    n = len(sent)
    stack = []
    for i in range(n):
        if sent[i] == '(' or sent[i] == '{':
            stack.append(sent[i])
            # print(stack)
        elif sent[i] == ')' or sent[i] == '}':
            # print(sent[i])
            if sent[i] == '}' and chr(ord(stack[-1]) + 2) == sent[i]:
                stack.pop()
            elif sent[i] == ')' and chr(ord(stack[-1]) + 1) == sent[i]:
                stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0


T = int(input())
answer =[]
for test_case in range(1, T+1):
    sent = input()
    answer.append(solve(sent))

for test_case in range(1, T+1):
    print(f'#{test_case}', answer[test_case - 1])

