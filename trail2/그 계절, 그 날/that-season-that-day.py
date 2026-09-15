Y, M, D = map(int, input().split())

# Please write your code here.
YY = 0
if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
        YY = 1
else:
    YY = 0  
def solution(YY, Y, M, D):
    M_list = [1, 3, 5, 7, 8, 10, 12]
    M_list2 = [2, 4, 6, 9, 11]
    a = 0
    if M not in M_list and M not in M_list2:
        return '-1'
    elif M in M_list:
        if D > 31:
            return '-1' 
    elif M == 2 and YY == 0:
        if D > 28:
            return '-1'
    elif M == 2 and YY == 1:
        if D > 29:
            return '-1' 
    elif M in M_list2:
        if D > 30:
            return '-1'
    else:
        return '-1'
    if 3 <= M <= 5:
        return 'Spring'
    elif 6 <= M <= 8:
        return 'Summer'
    elif 9 <= M <= 11:
        return 'Fall'
    else:
        return 'Winter'

print(solution(YY, Y, M, D))    

    
