"""
Source: https://www.youtube.com/watch?v=H9bfqozjoqs
"""
def coinChange(coins, amount: int) -> int:
        da = [float("inf")] * (amount + 1)
        da[0] = 0
        ddict = {}

        for a in range(1, len(da)):
            for c in coins:
                if a - c >= 0:
                    da[a] = min(da[a], 1 + da[a - c])
                    ddict[a] = [c]

        print(ddict)
        if da[amount] != float("inf"):
            return da[amount]
        else:
            return -1
        
coins = [1,5,6,9]
amount = 11 
print(coinChange(coins, amount))