N = int(input())
arr = [input().split() for _ in range(N)]


arr.sort(key=lambda x: int(x[0]))

for i in arr:
    print(*i)
