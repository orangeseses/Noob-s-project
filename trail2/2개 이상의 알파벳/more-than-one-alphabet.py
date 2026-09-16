A = input()

# Please write your code here.
def solution(A):
    if len(set(A)) >= 2:
        return 'Yes'
    else:
        return 'No'
print(solution(A))