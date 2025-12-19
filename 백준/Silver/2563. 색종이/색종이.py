# input 
n = int(input())

# 색종이 초기화
arr = [[0]*100 for _ in range(100)]

# 입력받은 검은색 색종이 정보 넣기
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, a+10):
        for k in range(b, b+10):
            arr[j][k] = 1

# 1인 칸을 다 더하면 검은색 종이의 넓이
ans = 0
for i in arr:
    ans += sum(i)

print(ans)