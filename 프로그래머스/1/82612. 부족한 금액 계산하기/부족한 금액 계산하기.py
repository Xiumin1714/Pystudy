def solution(price, money, count):
    # price 이용료, count 탑승한 횟수, money 가져간 돈
    cnt = []
    for i in range(1, count+1):
        cnt.append(i)
    answer = price*(sum(cnt)) - money
    return answer if answer > 0 else 0