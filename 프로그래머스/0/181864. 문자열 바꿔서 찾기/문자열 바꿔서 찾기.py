def solution(myString, pat):
    rule = myString.maketrans({'A':'B', 'B':'A'})
    swapped = myString.translate(rule)
    return int(pat in swapped)