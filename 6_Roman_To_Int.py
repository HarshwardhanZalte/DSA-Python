def romanToInt(s):
    rom = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    num = 0
    for i in s:
        num += rom[i]
    return num

n = input("Enter a roman number: ")
print("Integer number is: ", romanToInt(n.upper))

# Time Complexity: O(n)
# Space Complexity: O(1)