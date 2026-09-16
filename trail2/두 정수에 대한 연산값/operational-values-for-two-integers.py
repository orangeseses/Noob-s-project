a, b = map(int, input().split())

# Please write your code here.
def solution(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    return a, b

print(*solution(a, b))