import sys
sys.stdin = open("./inputs/input_forth.txt", "r")


def solve(equation):
    stack = []
    n = len(equation)
    for i in range(n):
        temp = []
        if equation[i] != '+' and equation[i] != '-' and equation[i] != '*' and equation[i] != '/' and equation[i] != '.':
            stack.append(equation[i])
        elif equation[i] == '+' or equation[i] == '-' or equation[i] == '*' or equation[i] == '/':
            if len(stack) >= 2:
                s1 = stack.pop()
                s2 = stack.pop()
                temp.append(s2)
                temp.append(equation[i])
                temp.append(s1)
                temp = ''.join(temp)
                temp =eval(temp)
                stack.append(str(temp))
            else:
                return "error"
        elif equation[i] == '.':
            return int(stack.pop())
    return "error"


T = int(input())
answer = []
for test_case in range(1, T + 1):
    equation = list(input().split())
    answer.append(solve(equation))


for i in range(T):
    print(f'#{i + 1}', answer[i])
