def largestPermutation(arr, swapNumber):
  copy = sorted(arr, reverse=True)
  
  for n in range(swapNumber):
    biggest = copy.pop(0)
    bigIndex = arr.index(biggest)
    if arr[n] < biggest:
      arr[n], arr[bigIndex] = arr[bigIndex], arr[n]

  
  return arr

print(largestPermutation([3, 2, 4, 1, 5], 3))