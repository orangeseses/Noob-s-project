a, b = map(int, input().split())

# Please write your code here.
def solution(a, b):
    a = a + 10 if a < b else a * 2
    b = b * 2 if a < b else b + 10
    return a, b
print(*solution(a, b))