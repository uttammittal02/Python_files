def mini_coins(n, v, coins):
    global dp
    for j in range(n):
        if coins[j] > v:
            return dp[v]
        if dp[v-coins[j]] == float('inf'):
            dp[v-coins[j]] = mini_coins(n, v-coins[j], coins)
        dp[v] = min(dp[v], 1 + dp[v-coins[j]])
    return dp[v]


n, v = map(float, input().split()); v *= 100
v = int(v)
n = int(n)
dp = [float('inf')] * (v+1)
dp[0] = 0
coins = list(map(float, input().split()))
for i in range(n):
    coins[i] *= 100
    coins[i] = int(coins[i])
result = mini_coins(n, v, coins)
# print(*dp)
if result == float('inf'):  print(-1)
    # exit(0)
print(result)

