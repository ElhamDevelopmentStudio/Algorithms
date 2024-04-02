"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Description: Given a target and a list of words, count the number of ways you can construct the target using the given words, return the count of numbers. By using memoization technique we can improve the time complexity from O((n^m) * m) to O(n * m^2) and the space complexity remains O(m^2)
"""
def CountConstruct(target, words, memo = {}):
  if target in memo:
    return memo[target]
  if target == "":
    return 1
  
  count = 0

  for word in words:
    if target[:len(word)] == word:
      waysCount = CountConstruct(target[len(word):], words)
      count += waysCount

  memo[target] = count
  return memo[target]


print(CountConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
