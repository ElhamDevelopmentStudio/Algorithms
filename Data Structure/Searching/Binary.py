numbers = [1,2,3,4,5,6,7,8,9]
item = 6

low = 0
high = len(numbers) - 1

while low <= high:
  mid = (low + high) // 2

  if item == numbers[mid]:
    print(mid)
    break

  elif item < numbers[mid]:
    high = mid - 1

  elif item > numbers[mid]:
    low = mid + 1