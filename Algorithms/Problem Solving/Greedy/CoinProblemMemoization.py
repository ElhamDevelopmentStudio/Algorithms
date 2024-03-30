myCache = {}
import time

def coinChange(coins, amount: int) -> int:
    if amount in myCache and coins in myCache[amount]:
          return myCache[amount][0]
    da = [float("inf")] * (amount + 1)
    da[0] = 0

    for a in range(1, len(da)):
        for c in coins:
            if a - c >= 0:
                da[a] = min(da[a], 1 + da[a - c])
                
                
    if da[amount] != float("inf"):
        time.sleep(1)
        myCache[amount] = da[amount], coins
        return da[amount]
    else:
        return -1
      
coins = [1,5,6,9]
amount = 11 
print(coinChange(coins, amount))

amount = 12
print(coinChange(coins, amount))

amount = 13
print(coinChange(coins, amount))

amount = 11
print(coinChange(coins, amount))

coins = [1, 3, 5]
print(coinChange(coins, amount))