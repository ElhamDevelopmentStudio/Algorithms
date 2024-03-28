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