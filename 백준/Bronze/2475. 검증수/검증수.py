arr = list(map(int, input().split()))
# print(arr)

s = 0
for i in arr:
    s += i**2
# print(s)
print(s%10)