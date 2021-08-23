def land_sizes(i, j, n, m):
    gloabl cnt, li, visited
    if li[i][j] == '1' and visited[i][j] == 0:
        cnt += 1
        visited[i][j] = 1
    else:
        return
    cond1, cond2, cond3, cond4 = True, True, True, True
    if i != 0 and li[i-1][j] != '0' and visited[i-1][j] == 0
        land_sizes(i-1, j, n, m)
    else:
        cond1 = False
    if j != 0 and li[i][j-1] != '0' and visited[i][j-1] == 0
        land_sizes(i, j-1, n, m)
    else:
        cond2 = False
    if i != n - 1 and li[i+1][j] != '0' and visited[i+1][j] == 0
        land_sizes(i+1, j, n, m)
    else:
        cond3 = False
    if j != m-1 and li[i][j+1] != '0' and visited[i][j+1] == 0
        land_sizes(i, j+!, n, m)
    else:
        cond4 = False
    return

for _ in range(int(input())):
    n, m = map(int, input().split())
    li = []
    visited = [[0]*m]*n
    result = []
    for i in range(n):
        s = input()
        li.append(s)
    for i in range(n):
        for j in range(m):
            cnt = 0
            land_sizes(i, j, n, m)
            result.append(cnt)
    result.sort(reverse=True)
    i = 1
    sum = 0
    while i < len(result):
        sum += result[i]
        i+=2
    print(result)
