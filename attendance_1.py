arr = []


def sub(x, i, p):
    if i >= len(x):
        a = p.copy()
        arr.append(a)
        # print(p)
        return
    sub(x, i + 1, p)
    p.append(x[i])
    sub(x, i + 1, p)
    p.pop()


li = list(map(int, input().split()))
sub(li, 0, [])

# print(arr)
print(*arr)
