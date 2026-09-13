a, b = map(int, input().split())

# Please write your code here.
def solution(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if (i % 2 == 0) or (i % 5 == 0) or (i % 3 == 0 and i % 9 != 0):
            continue
        cnt += 1
    return cnt

print(solution(a, b))
