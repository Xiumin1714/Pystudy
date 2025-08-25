def solution(answers):
    answer = []
    scores = [0,0,0]
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == arr1[i%5]:
            scores[0] += 1
        if answers[i] == arr2[i%8]:
            scores[1] += 1
        if answers[i] == arr3[i%10]:
            scores[2] += 1

    for idx, num in enumerate(scores):
        if num == max(scores):
            answer.append(idx+1)
    return answer