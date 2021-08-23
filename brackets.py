# import sys
def brackets(n):
    li = []
    n+=1
    print("n inside functoion", n, id(n))
    for i in range(n):
        li.append('(')
    for i in range(n):
        li.append(')')
    # print(*li)
    for i in range(n - 1):
        li[n - i - 1], li[2 * n - 2 * i - 2] = li[2 * n - 2 * i - 2], li[n - i - 1]
        print(*li)
    print(locals())
# print(sys.path)

# sys.argv()
n = int(input())
# y = int(sys.argv[2])
brackets(n)
print("n outside functoion", n, id(n))
# print("y =", y)