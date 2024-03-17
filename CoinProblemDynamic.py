
def coinChange(coins, amount: int) -> int:
        da = [float("inf")] * (amount + 1)
        da[0] = 0

        for a in range(1, len(da)):
            for c in coins:
                if a - c >= 0:
                    da[a] = min(da[a], 1 + da[a - c])

        if da[amount] != float("inf"):
            return da[amount]
        else:
            return -1
        
coins = [9]
amount = 11 
print(coinChange(coins, amount))