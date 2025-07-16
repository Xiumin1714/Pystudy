def solution(n, k):
    if n >= 10:
        service = n // 10
    else:
        service = 0
    answer = 12000*n + 2000*(k-service)
    return answer;
