import math
def fun(n):
    ans = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            ans+=1
    return ans
for _ in range(int(input())):
    a = int(input())
    if a % 2 == 0 and a%4 != 0:
        print(0)
    elif a % 2 != 0:
        n = fun(a)
        print(n)
        #r = math.comb(n, 2)
    else:
        n = fun(a/4)
        print(n)
        #r = math.comb(n, 2)
