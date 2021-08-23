# def safeindex(q, p):
#     if q>=0 and q<r and p>=0 and p<c:
#         return True
#     else:
#         return False
    
# t = int(input())
# for l in range(t):
#     r, c = map(int, input().split())
#     mat = [0]*r
#     for j in range(r):                                                   #OLD CODE
#         arr = list(map(int, input().split()))[:c]
#         mat[j] = arr
#     i, j = 0, 0
#     count = 0
#     ans = 0
#     for i in range(r):
#         for j in range(c):
#             if safeindex(i, j-1):
#                 if abs(mat[i][j] - mat[i][j-1]) > 1:
#                     count = abs(mat[i][j] - mat[i][j-1]) - 1
#                     ans += count
#                     if mat[i][j]>mat[i][j-1]:
#                         mat[i][j-1] += count
#                     else:
#                         mat[i][j] += count
                        
#             if safeindex(i, j+1):
#                 if abs(mat[i][j] - mat[i][j+1]) > 1:
#                     count = abs(mat[i][j] - mat[i][j+1]) - 1
#                     ans += count
#                     if mat[i][j]>mat[i][j+1]:
#                         mat[i][j+1] += count
#                     else:
#                         mat[i][j] += count
#             if safeindex(i-1, j):
#                 if abs(mat[i][j] - mat[i-1][j]) > 1:
#                     count = abs(mat[i][j] - mat[i-1][j]) - 1
#                     ans += count
#                     if mat[i][j]>mat[i-1][j]:
#                         mat[i-1][j] += count
#                     else:
#                         mat[i][j] += count
#             if safeindex(i+1, j):
#                 if abs(mat[i][j] - mat[i+1][j]) > 1:
#                     count = abs(mat[i][j] - mat[i+1][j]) - 1
#                     ans += count
#                     if mat[i][j]>mat[i+1][j]:
#                         mat[i+1][j] += count
#                     else:
#                         mat[i][j] += count
            
        
       
#     print("Case #", end = ""); print(l+1, end = ""); print(":", end = " "); print(ans)




#------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import sys
import copy

sys.setrecursionlimit(1000000)
def solve_max(arr):
    max_val = np.amax(arr)
    max_indices = np.where(arr == max_val)
    return solve_all(max_indices[0][0], max_indices[1][0])

# 1 2 3
# 4 5 6
# 7 8 9
mat = []
vis = []
def solve_all(i, j):
    global mat, vis
    count = 0
    
    cond1, cond2, cond3, cond4 = True, True, True, True
    vis[i][j] = 1
    if safeindex(i, j-1):
        if abs(mat[i][j] - mat[i][j-1]) > 1:
            count = abs(mat[i][j] - mat[i][j-1]) - 1
            
            if mat[i][j]>mat[i][j-1]:
                mat[i][j-1] += count
            else:
                mat[i][j] += count
        else:
            cond1 = False
                
    if safeindex(i, j+1):
        if abs(mat[i][j] - mat[i][j+1]) > 1:
            count = abs(mat[i][j] - mat[i][j+1]) - 1
            
            if mat[i][j]>mat[i][j+1]:
                mat[i][j+1] += count
            else:
                mat[i][j] += count
        else:
            cond2 = False
    if safeindex(i-1, j):
        if abs(mat[i][j] - mat[i-1][j]) > 1:
            count = abs(mat[i][j] - mat[i-1][j]) - 1
            
            if mat[i][j]>mat[i-1][j]:
                mat[i-1][j] += count
            else:
                mat[i][j] += count
        else:
            cond3 = False
    if safeindex(i+1, j):
        if abs(mat[i][j] - mat[i+1][j]) > 1:
            count = abs(mat[i][j] - mat[i+1][j]) - 1
            
            if mat[i][j]>mat[i+1][j]:
                mat[i+1][j] += count
            else:
                mat[i][j] += count
        else:
            cond4 = False
    if safeindex(i, j-1) and (vis[i][j-1] == 0 or cond1):
        solve_all(i, j-1)
    if safeindex(i, j+1) and (vis[i][j+1] == 0 or cond2):
        solve_all(i, j+1)
    if safeindex(i-1, j) and (vis[i-1][j] == 0 or cond3):
        solve_all(i-1, j)
    if safeindex(i+1, j) and (vis[i+1][j] == 0 or cond4):
        solve_all(i+1, j)
    
    return 


def safeindex(q, p):
    if q>=0 and q<r and p>=0 and p<c:
        return True
    else:
        return False


t = int(input())
for l in range(t):
    r, c = map(int, input().split())
    vis = [[0]*c]*r
    mat = [0]*r
    for j in range(r):                                                      #NEW CODE
        arr = list(map(int, input().split()))[:c]
        mat[j] = arr
    new = copy.deepcopy(mat)
    solve_max(mat)
    ans = 0
    for i in range(r):
        for j in range(c):
            ans += abs(new[i][j] - mat[i][j])
    # print(*new)
    print("Case #", end = ""); print(l+1, end = ""); print(":", end = " "); print(ans)

    
    
    
            
    



        