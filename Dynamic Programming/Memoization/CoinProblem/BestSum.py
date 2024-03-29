"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Description: Given an array of coins and a target value find out which coins it would take to sum up to the target. (You have to return a list of minimum coins that amounts to the target.)
"""

def HowSum(target, coins, memo = {}):
  if target in memo:
    return memo[target]
  if target == 0:
    return []
  if target < 0:
    return None
  
  finalResult = None
  
  for c in coins:
    remainder = target - c

    remainderResult = HowSum(remainder, coins)
    
    if remainderResult is not None:
      if (finalResult == None or len(remainderResult + [c]) < len(finalResult)):
        finalResult = remainderResult + [c]
    
  memo[target] = finalResult
  return finalResult

print(HowSum(100, [1,2,5,25]))
