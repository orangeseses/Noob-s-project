n, m = map(int, input().split())

# Please write your code here.
def a(n, m):
    cnt = 1
    i = 1
    while True:
        if i % n == 0 and i % m == 0:
            cnt = i
            break
        i += 1
    return cnt
print(a(n, m))




    

