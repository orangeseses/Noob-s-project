num = int(input())
sts = [input() for i in range(num)]; cnt = 0; cnt2 = 0
for i in range(0, num):
    if sts[i][0] == "a":
        cnt += 1
for j in range(0, num):
    cnt2 += len(sts[j])
print(cnt2,  cnt)

