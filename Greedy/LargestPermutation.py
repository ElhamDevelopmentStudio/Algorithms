"""
Here we take an array and an integer, the integer represents the amount of times we can swap in the array. the objective here is to swap the biggest number in the array with the element in the front of the array.
source: https://www.youtube.com/watch?v=bC7o8P_Ste4&t=738s
"""

def largestPermutation(arr, swapNumber):
  copy = sorted(arr, reverse=True)
  
  for n in range(swapNumber):
    biggest = copy.pop(0)
    bigIndex = arr.index(biggest)
    if arr[n] < biggest:
      arr[n], arr[bigIndex] = arr[bigIndex], arr[n]

  
  return arr

print(largestPermutation([3, 2, 4, 1, 5], 3))