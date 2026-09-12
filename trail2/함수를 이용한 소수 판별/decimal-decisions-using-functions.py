a, b = map(int, input().split())

# Please write your code here.
def prime(a, b):
    cnt = 0
    for i in range(a, b + 1):
        cnt += i
        for j in range(2, i):
            if i % j == 0:
                cnt -= i
                break

                        
    return cnt
print(prime(a, b))