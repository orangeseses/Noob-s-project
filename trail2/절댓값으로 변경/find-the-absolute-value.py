n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def solution(arr):
    arrr = []
    a = 0
    for e in arr:
        if e < 0:
            a = -e
            arrr.append(a)
        else:
            arrr.append(e)
    return arrr
print(*solution(arr))

