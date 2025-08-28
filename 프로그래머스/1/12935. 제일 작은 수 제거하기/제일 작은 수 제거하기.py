def solution(arr):
    answer = []
    min_val = 1000000
    
    for i in range(len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
    
    arr.remove(min_val)
    if len(arr) == 0:
        arr.append(-1)

    return arr