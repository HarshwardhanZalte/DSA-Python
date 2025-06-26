
n = (1, 1, 1, 2, 2, 3, 4, 5, 7, 7, 8, 8, 8, 8, 10, 10)
m = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

hash_list = [0] * 11

for i in n:
    hash_list[i] += 1

for num in m:
    print(num, "occurs", hash_list[num], "times")

