"""
Source: https://www.youtube.com/watch?v=bC7o8P_Ste4
Name of the problem: Bulb
"""

def OptimizedBulbOn(arr):
  count = 0

  for i in range(len(arr)):
    if count % 2 == 0:
      arr[i] = arr[i]
    else:
      arr[i] = not arr[i]

    if arr[i] % 2 == 1: # if odd then just skip the iteration, otherwise flip the elements to the right and increase the count.
      continue
    else:
      count += 1
  
  return count

arr = [1, 0, 1]
print(OptimizedBulbOn(arr))