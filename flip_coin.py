import math
for _ in range(int(input())):
    for g in range(int(input())):
        i, n, q = list(map(int, input().split()))
        if i == q:
            print(math.floor(n/2))
        else:
            print(math.ceil(n//2))