nums = list(map(int, input().split()))
item = int(input())

low = 0
high = len(nums) - 1

while low <= high:
  mid = int((low + high) / 2)

  if item < nums[mid]:
    high = mid - 1
  if item > nums[mid]:
    low = mid + 1
  if item == nums[mid]:
    print(mid)
    break
  print("None")
  break

  