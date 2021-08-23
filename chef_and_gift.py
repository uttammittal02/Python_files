for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    li = list(map(int, input().split()))
    cnt = 0
    found = False
    if k == 0:
        for i in range(n):
            if li[i] % 2 != 0:
                found = True
                print("YES")
                break
    else:
        for i in range(n):
            if li[i]%2 == 0:
                cnt += 1
            if cnt >= k:
                print('YES')
                found = True
                break
    if not found:
        print('NO')
