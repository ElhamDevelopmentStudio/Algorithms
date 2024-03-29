"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Description: Given an array of coins and a target value find out whether or not you can sum up to the target, return true if so and false if not.
"""

def canSum(target, coins, memo = {}):
  if target in memo:
    return memo[target]
  if target == 0:
    return True
  if target < 0:
    return False
  
  for i in coins:
    targetS = target - i
    if canSum(targetS, coins) == True:
      memo[target] = True
      return True
  
  memo[target] = False
  return False
    
coins = [5,3,4,7]
target = 1000
print(canSum(target, coins))