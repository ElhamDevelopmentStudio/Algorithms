"""
Source: https://www.youtube.com/watch?v=bC7o8P_Ste4
Issue: The problem here is that our time complexity is O(n^2) check out the optimized solution for a better time complexity.
"""

def bulbOn(arr):
  count = 0
  for i in range(len(arr)):
      if arr[i] == 1:
          continue
      elif arr[i] == 0: 
          arr[i] = 1  
          for n in range(i + 1, len(arr)):  
              arr[n] = 1 - arr[n]  
          count += 1  

  return count


arr = [1, 0, 1]

print(bulbOn(arr))