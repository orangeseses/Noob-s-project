st, st2 = [input() for _ in range(2)]; cnt = 0
for i in range(0, len(st)):
    if st2 == st[i]:
        cnt += 1

print(cnt)
