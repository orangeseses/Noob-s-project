a, b = map(int, input().split())

# Please write your code here.
def num(a, b):
    cnt = 0
    num2 = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            cnt += 1
            continue
        num2 = str(i)
        if '3' in num2 or '6' in num2 or '9' in num2:
            cnt += 1
    return cnt
print(num(a, b))