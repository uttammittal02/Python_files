for _ in range(int(input())):
    k, n, l, r = list(map(int, input().split()))
    li = []
    sum_ = []
    for i in range(k):
        arr = list(map(int, input().split()))
        s = sum(arr)
        arr.sort()
        li.append(arr)
        sum_.append(s)
    x = min(sum_)
    y = max(sum_)
    # print(x, y)
    # z = sum(sum_)
    mid = (x+y)//2
    no_of_operations = 0
    # print('mid = ', mid)
    for i in range(k):
        if mid == sum_[i]:
            continue
        if mid > sum_[i]:
            t = 0
            cnt = 0
            for j in range(n):
                t += r - li[i][j]
                cnt+=1
                # print("t = ", t, "j= ", j)
                if t >= mid - sum_[i]:
                    no_of_operations = max(no_of_operations, cnt)
                    break
        else:
            t = 0
            cnt = 0
            for j in range(n):
                t += li[i][n - j - 1] - l
                cnt+=1
                if t >= sum_[i] - mid:
                    no_of_operations = max(no_of_operations, cnt)
                    break
        # print(no_of_operations)
    print(no_of_operations)
