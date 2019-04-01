import sys
sys.stdin = open("inputs/bus_input.txt")

def solve(K, N, stops):
    prev = 0
    now = K
    count = 0

    for i in range(len(stops) - 1):
        now -= stops[i] - prev

        if now < 0:
            return 0
        if now < stops[i + 1] - stops[i]:
            now = K
            count += 1
        prev = stops[i]
    last = stops[-1]
    now -= last - prev
    if N - last > K:
        return 0
    elif N - last > now:
        count += 1
    return count


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        K, N, M = map(int, input().split())
        stops = list(map(int, input().split()))
        print(f'#{i+1}', solve(K, N, stops))


