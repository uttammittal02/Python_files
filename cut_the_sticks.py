import bisect

n = int(input())
sticks = list(map(int, input().split()))
sticks.sort(reverse = False)
count = len(sticks)
i = 0
while i < len(sticks):
    print(count)
    count -= (bisect.bisect_right(sticks, sticks[i]) - bisect.bisect_left(sticks, sticks[i]))
    i = bisect.bisect_right(sticks, sticks[i])
