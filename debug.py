n, m = 3, 4
for l in range(1, min(n, m)+1):
        #l = 1
        left = 0
        i = n - l
        while i >= 0:
            row = i
            print(i)
            #index = BinarySearchOnMatrix(k, l, m, n, row, left)
            #left = index
            #if index == -1:
            #    break
            #else:
            #    count += m - index - l + 1
            i-=1