def solution(money):
    cups = money // 5500
    balance = money - (5500*cups)
    answer = [cups, balance]
    return answer

print(solution(15000))