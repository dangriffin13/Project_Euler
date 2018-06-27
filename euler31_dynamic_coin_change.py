
coins = [1, 2, 5, 10, 20, 50, 100, 200]

combos = [1] + [0] * 100000

for coin in coins:
    for i in range(coin, 100001): #100000 is max range on hackerrank
        combos[i] += combos[i-coin]

t = int(input())

mod = 10**9 + 7

for _ in range(t):
    n = int(input())
    print(combos[n]%mod)