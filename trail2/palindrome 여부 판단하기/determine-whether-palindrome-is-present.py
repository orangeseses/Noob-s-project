A = input()

# Please write your code here.
def solution(A):
    AA = A[::-1]
    if AA == A:
        return 'Yes'
    else:
        return 'No'
print(solution(A))