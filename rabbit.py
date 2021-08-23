def safeindex(q, p):
    if q >= 0 and q < r and p >= 0 and p < c:
        return True
    else:
        return False

t = int(input())
for l in range(t):
    r, c = map(int, input().split())
    mat = [0]*r
    for j in range(r):
        arr = list(map(int, input().split()))[:c]
        mat[j] = arr
    i, j = 0, 0
    count = 0
    ans = 0
    for i in range(r):
        for j in range(c):
            if safeindex(i, j-1):
                if abs(mat[i][j] - mat[i][j-1]) > 1:
                    count = abs(mat[i][j] - mat[i][j-1]) - 1
                    ans += count
                    if mat[i][j]>mat[i][j-1]:
                        mat[i][j-1] += count
                    else:
                        mat[i][j] += count
                        
            if safeindex(i, j+1):
                if abs(mat[i][j] - mat[i][j+1]) > 1:
                    count = abs(mat[i][j] - mat[i][j+1]) - 1
                    ans += count
                    if mat[i][j]>mat[i][j+1]:
                        mat[i][j+1] += count
                    else:
                        mat[i][j] += count
            if safeindex(i-1, j):
                if abs(mat[i][j] - mat[i-1][j]) > 1:
                    count = abs(mat[i][j] - mat[i-1][j]) - 1
                    ans += count
                    if mat[i][j]>mat[i-1][j]:
                        mat[i-1][j] += count
                    else:
                        mat[i][j] += count
            if safeindex(i+1, j):
                if abs(mat[i][j] - mat[i+1][j]) > 1:
                    count = abs(mat[i][j] - mat[i+1][j]) - 1
                    ans += count
                    if mat[i][j]>mat[i+1][j]:
                        mat[i+1][j] += count
                    else:
                        mat[i][j] += count
            
        
       
    print("Case #", end = ""); print(l+1, end = ""); print(":", end = " "); print(ans)
