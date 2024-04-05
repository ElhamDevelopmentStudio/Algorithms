"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Description: Given an array of coins and a target value find out whether or not you can sum up to the target, return true if so and false if not.
"""

def CanSum(target, coins):
  table = [False] * (target + 1)
  table[0] = True

  for i in range(len(table)):
    if table[i] == True:
      for j in coins:
        if i + j <= target:
          table[i + j] = True
    
  return table[target]

print(CanSum(7, [5,3,4])) 