import random

N = int(input())
M = int(input())
Sampling = []
for i in range(N):
    for j in range(M):
        Sampling[i][j].append(random.randint(1, 1000))

print(Sampling)
#
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         if j+3 <= M:
