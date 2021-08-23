for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    # n = int(input())
    set_ = set(arr)
    if n - len(set_) >= x:
        print(len(set_))
        continue
    print(min(len(set_), n - x))
