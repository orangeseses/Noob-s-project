a, b = map(int, input().split())

# Please write your code here.
def solution(a, b):
    cnt = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(a, b + 1):
        cnt = 0; cnt2 = 0
        c = i

        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break

        if cnt == 0:
            while c > 0:
                cnt2 += c % 10
                c //= 10

            if cnt2 % 2 == 0:
                cnt3 += 1

    return cnt3 
print(solution(a, b))
        


