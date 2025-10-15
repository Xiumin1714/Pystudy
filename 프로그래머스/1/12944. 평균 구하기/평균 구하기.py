def solution(arr):
    tmp = 0
    for i in range(len(arr)):
        tmp += arr[i]
    answer = tmp / len(arr)
    return answer