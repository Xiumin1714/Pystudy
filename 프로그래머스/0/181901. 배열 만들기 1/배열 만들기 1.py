def solution(n, k):
    answer = []
    for i in range(1, n+1):
        if i*k <= n:
            answer.append(i*k)
        else:
            break
    return answer