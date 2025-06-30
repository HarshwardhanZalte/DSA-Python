# def fib(n):
#     if n == 0:
#         return 0
#     c = 0
#     a, b = 0, 1
#     for i in range(1,n):
#         c = a + b
#         a = b
#         b = c
#     return b

def func(n):
    if n == 0  or n == 1:
        return n
    return func(n-1) + func(n-2)
    
def fib(n):
    return func(n)

n = int(input("Enter a number: "))
print(fib(n))

# Time Complexity: O(2^n)
# Space Complexity: O(n)