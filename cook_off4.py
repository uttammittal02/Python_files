n, v = input().split()
n = int(n)
v = float(v)
coins = sorted(list(map(float, input().split())))
no_of_coins = int(0)
# val = 0
for i in range(n):
    if v == 0:
        break
    t = v//coins[n-i-1]
    no_of_coins += t
    v -= t * coins[n-i-1]
# no_of_coins = int(no_of_coins)
print(no_of_coins)