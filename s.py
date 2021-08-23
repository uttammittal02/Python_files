def good(mid,n,m,a,b):
    temp = []
    sum_ = 0
    for i in range(n):
        if b[i] == 0:
            temp.append(a[i])
        else:
            temp.append(mid//b[i])
        sum_ += max(0, a[i] - temp[i])
    if sum_ <= m:
        return True
    return False
def searching(n,m,a,b):
    l=0
    r=max([a[i]*b[i] for i in range(n)])
    ans = 0
    while l<r:
        mid=l+(r-l)//2
        if good(mid,n,m,a,b):
            h = mid - 1
            ans = mid
        else:
            l = mid + 1
    return ans
n,m=map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
#li = []
#for i in range(n):
 #   li.append(a[i]*b[i])
st = searching(n, m, a, b)
print(st)