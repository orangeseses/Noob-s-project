n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def solution(n1, n2, a, b):
    for i in range(n1 - n2 + 1):
        if a[i : n2 + i] == b:
            return 'Yes'
    return 'No'
print(solution(n1, n2, a, b))
    

