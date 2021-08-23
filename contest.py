n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = b[0]
idx = 0
for i in range(n):
    if abs(b[i]) > abs(m):
        m = b[i]
        idx = i
if m > 0:
    a[idx] += k
else:
    a[idx] -= k
ans = 0
for i in range(n):
    ans += a[i]*b[i]
print(ans)
