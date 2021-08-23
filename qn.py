for i in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    ans = 0
    large = float('inf')
    for i in range(n):
        if li[i] < large:
            large = li[i]
        ans += large
    print(ans)