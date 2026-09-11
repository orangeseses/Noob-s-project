n = int(input())

# Please write your code here.
def num(n):
    cnt = 0
    for i in range(1, n + 1):
        cnt += i
    return cnt // 10
print(num(n))
    
