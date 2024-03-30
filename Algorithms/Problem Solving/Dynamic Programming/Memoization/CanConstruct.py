"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Description: Given a target and a list of words, see if you can construct the target using the given words, if possible return true otherwise return false. By using memoization technique we can improve the time complexity from O((n^m) * m) to O(n * m^2) and the space complexity remains O(m^2)
"""

def CanConstruct(target, words, memo = {}):
  if target in memo:
    return memo[target]
  if target == "":
    return True
  
  for word in words:
    if target[:len(word)] == word:
      remainder = target[len(word):]
      if CanConstruct(remainder, words) == True:
        memo[target] = True
        return memo[target]
  
  memo[target] = False
  return memo[target]

print(CanConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"
                   , ["eeee", "eeeeeeeeeeeeeeee", "eeeeeeeeeeeeeee", "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "eeeeeeeeeeeeeeeeeeee"]))