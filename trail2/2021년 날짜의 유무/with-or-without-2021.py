M, D = map(int, input().split())

# Please write your code here.
def solution(M, D):
    if M == 2:
        if D <= 28:
            return 'Yes'
        else:
            return 'No'
    elif M <= 7 and M % 2 != 0:
        if D <= 31:
            return 'Yes'
        else:
            return 'No'
    elif 8 <= M <= 12 and M % 2 == 0:
        if D <= 31:
            return 'Yes'
        else:
            return 'No'
    elif M <= 7 and M % 2 == 0:
        if D <= 30:
            return 'Yes'
        else:
            return 'No'
    elif 8 <= M <= 12 and M % 2 != 0:
        if D <= 30:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'
print(solution(M, D))