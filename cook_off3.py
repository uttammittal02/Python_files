for _ in range(int(input())):
    n, q = map(int,input().split())
    li = list(map(int, input().split()))
    dp1 = []
    dp2 = []
    r = li[0]
    y = li[n-1]
    for i in range(0,n):
        dp1.append(r)
        r|li[i]
        dp2.append(y)
        y|li[n-i-1]
    print(dp1, dp2)
    for j in range(q):
        x, v = map(int,input().split())
        print((dp1[x-1] | x) | (dp2[n-x] | x)

