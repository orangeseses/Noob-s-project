n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def solution(arr):
    new_arr = []
    for e in arr:
        if e % 2 != 0:
            new_arr.append(e)
        else:
            new_arr.append(e // 2)
    return new_arr
print(*solution(arr))