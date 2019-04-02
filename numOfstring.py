import sys
sys.stdin = open("./inputs/input_numOfstring.txt", "r")


def solve(str1, str2):
    dictionary = {}
    for i in range(len(str1)):
        if str1[i] not in dictionary:
            dictionary[str1[i]] = 0

    for i in range(len(dictionary)):
        count = 0
        temp = list(dictionary.keys())[i]
        for j in range(len(str2)):
            if str2[j] == temp:
                count += 1
        dictionary[temp] = count

    result = list(dictionary.values())
    return max(result)


T = int(input())
answer = []
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    answer.append(solve(str1, str2))

for test_case in range(1, T + 1):
    print(f'#{test_case}', answer[test_case - 1])

