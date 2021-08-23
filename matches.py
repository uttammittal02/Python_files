def no_of_matches(n):
    if n == '0' or n=='6' or n=='9':
        return 6
    if n=='1':
        return 2
    if n=='2' or n=='5' or n=='3':
        return 5
    if n=='4':
        return 4
    if n=='7':
        return 3
    if n=='8':
        return 7
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    sum = a+b
    sum = str(sum)
    ans = 0
    for i in range(len(sum)):
        ans += no_of_matches(sum[i])
    print(ans)