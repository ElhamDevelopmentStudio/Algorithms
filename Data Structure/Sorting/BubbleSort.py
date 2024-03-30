def FindSmallest(nums):
  smallest_index = 0

  for i in range(1, len(nums)):
    if nums[i] < nums[smallest_index]:
      smallest = nums[i]
      smallest_index = i
  return smallest_index

def BubbleSort(nums):
  sortedNumbers = []
  for _ in range(len(nums)):
    # we give the list to the FindSmallest function to get the smallest value so we can sort the list in a ascending manner.
    currentSmallNumber = FindSmallest(nums)
    # in here we append the returned number from FindSmallest to the new list and pop it from the old list this way each new nunber
    # which is the smallest in the given array will be appended one by one to the new list in ascending order.
    sortedNumbers.append(nums.pop(currentSmallNumber))

  print(sortedNumbers)

nums = list(map(int, input().split()))
BubbleSort(nums)