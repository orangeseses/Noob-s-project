st1, st2, st3 = [input() for _ in range(3)]
len_list = [len(st1), len(st2), len(st3)]
new_len_list = sorted(len_list)

print(new_len_list[-1] - new_len_list[0])