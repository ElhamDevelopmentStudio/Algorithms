"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Description: Given an array of coins and a target value find out which coins it would take to sum up to the target. (your returned array doesn't have to be the minimum amount of coins to add up to the target.)
"""

def HowSum(target, coins, memo = {}):
  if target in memo:
    return memo[target]
  if target == 0:
    return []
  if target < 0:
    return None
  
  for c in coins:
    remainder = target - c

    remainderResult = HowSum(remainder, coins)
    
    if remainderResult is not None:
      memo[target] = remainderResult + [c]
      return remainderResult + [c]
    
  memo[target] = None
  return None

print(HowSum(100, [7,3,7,3,6,7,978,24,6,7,234,6,8,3,4,7]))
