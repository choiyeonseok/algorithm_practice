T = int(input())
maxi_list = []
idx_list = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    counts = []
    N = int(input())
    K = input()
    K_list = []
    for i in range(len(K)):
        K_list.append(int(K[i]))
    for i in range(len(K_list)):
        count = 0
        for j in range(i, len(K_list)):
            if K_list[i] == K_list[j]:
                count += 1
        counts.append(count)
    print(counts)
    maxiComp = max(counts)
    maxi_count = 0
    maxi_value = []
    for i in range(len(counts)):
        if maxiComp == counts[i]:
            maxi_count += 1
            maxi_value.append(K_list[i])
    if maxi_count > 1:
        idx_list.append(max(maxi_value))
        maxi_list.append(max(counts))
    else:
        idx_list.append(K_list[counts.index(max(counts))])
        maxi_list.append(max(counts))


for test_case in range(1, T + 1):
    print(f'#{test_case}', idx_list[test_case - 1], maxi_list[test_case - 1])
