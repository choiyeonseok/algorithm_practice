n, m = map(int, input().split())

check = [False] * (n+1)
a = [0] * m


def go(index, start, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        return
    for i in range(start, n+1):
        if check[i]:
            continue
        check[i] = True  #사용했으니까 true를 넣어준다.
        a[index] = i    #제일 앞에 0부터 n까지 수를 넣고
        go(index + 1, i+1, n, m) #다음으로 넘긴다. 중복체크를 해놨기 때문에 재귀해도 순열이 된다.
        check[i] = False


go(0, 1, n, m) #출력할때 0부터 m-1번째로 출력한다고 했다.