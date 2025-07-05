# n = int(input("Enter a size: "))
# l1 = []
# for i in range(1,n+1):
#     l1.append(input(f"Enter {i} Element: "))
# l2 = l1[::-1]
# if l1 == l2:
#     print("True")
# else:
#     print("False")


# def printNo(n):
#     print(n)
#     printNo(n+1)

# printNo(1)


class Car:
    def sayHello(self):
        print(self,"Hello")


c1 = Car()
c1.sayHello()