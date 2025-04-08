N = int(input())
arr = [input() for _ in range(N)]
# print(arr)

arr.sort()
arr.sort(key = len)

ans = []
for i in arr:
    if i not in ans:
        ans.append(i)

for j in ans:
    print(j)