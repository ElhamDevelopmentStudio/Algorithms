def coinChange(coins, amount: int) -> int:
    da = [float("inf")] * (amount + 1)
    da[0] = 0
    coinsItself = [None] * (amount + 1)
    coinsItself[0] = []

    for a in range(1, len(da)):
        for c in coins:
            if a - c >= 0 and 1 + da[a - c] < da[a]:
                da[a] = 1 + da[a - c]
                coinsItself[a] = coinsItself[a - c] + [c]

    if da[amount] != float("inf"):
        return coinsItself[amount]
    else:
        return -1

coins = [1,2,5]
amount = 11 
print(coinChange(coins, amount))
