
n = (1, 1, 1, 2, 2, 3, 4, 5, 7, 7, 8, 8, 8, 8, 10, 10)
m = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

hash_list = [0] * 11

for i in n:
    hash_list[i] += 1

for num in m:
    print(num, "occurs", hash_list[num], "times")


# Time Complexity: O(n + m) where n is the number of elements in the first list and m is the number of unique elements in the second list
