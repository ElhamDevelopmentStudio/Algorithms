"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Description: Given a target and a list of words, return the different ways that the target can be constructed using those words. By using memoization technique we can improve the time complexity from O((n^m) * m) to O(n * m^2) and the space complexity remains O(m^2)
"""
def CountConstruct(target, words):
  if target == "":
    return [[]]
  
  results = []
  

  for word in words:
    if target[:len(word)] == word:
      ways = CountConstruct(target[len(word):], words)
      targetWays = [[word] + i for i in ways] 
      results.extend(targetWays)

  return results


print(CountConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
