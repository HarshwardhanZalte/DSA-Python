str = "adgfsbfdtaervfdsaarafdbgargagvsgrgbhjtyujryh"

freq = {}

for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

max = 0
for i in freq:
    if freq[i] > max:
        max = freq[i]
        res = i

print(res,"=",max)

# Time Complexity: O(n)
# Space Complexity: O(n)