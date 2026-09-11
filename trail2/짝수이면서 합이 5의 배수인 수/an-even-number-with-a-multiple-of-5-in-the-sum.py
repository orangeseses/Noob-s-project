n = int(input())

# Please write your code here.
cnt = 0
if n < 20:
    cnt = 1
elif n < 30:
    cnt = 2
elif n < 40:
    cnt = 3
elif n < 50:
    cnt = 4
elif n < 60:
    cnt = 5
elif n < 70:
    cnt = 6
elif n < 80:
    cnt = 7
elif n < 90:
    cnt = 8
else:
    cnt = 9
cnt2 = n - cnt * 10

def num(n, cnt, cnt2):
    if n % 2 == 0 and (cnt + cnt2) % 5 == 0:
        return 'Yes'
    else:
        return 'No'
print(num(n, cnt, cnt2))