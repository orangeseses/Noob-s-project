sts = [input() for _ in range(10)]
st = input()
cnt = 0

for x in range(0, 10):
    if sts[x][-1] == st:
        print(sts[x])
        cnt += 1
if cnt == 0:
    print('None')