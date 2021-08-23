import bisect
# for _ in range(int(input())):
n = int(input())
li = list(map(int, input().split()))
arr = [1] * n
# print(arr)
# a, b = list(map(int, input().split()))
operations = 0
ans = []
done = [False]*n
for i in range(n):
    # done = False
    if li[i] == arr[i]:
        done[i] = True
        continue
    while li[i] > arr[i]:
        ans.append([1, i+1])
        operations+=1
        arr[i] *= 2
    if li[i] < arr[i]:
        for j in range(i+2):
            if i!=j and arr[i] - li[i] == arr[j]:
                ans.append([2, i+1, j+1])
                operations+=1
                arr[i] -= arr[j]
                done[i] = True
                break
            if done[j] == False and arr[j] - li[j] == arr[i]:
                ans.append([2, j+1, i+1])
                operations+=1
                arr[j] -= arr[i]
                done[j] = True
                break
        # if done[i] != True:
        #     done[i] = False
sorted_arr = sorted(arr)
for i in range(n):
    if done[i] == True:
        continue
    