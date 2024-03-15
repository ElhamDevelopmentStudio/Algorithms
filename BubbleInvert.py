def findBiggest(numbers):
  biggest_index = 0

  for i in range(len(numbers)):
    if numbers[i] > numbers[biggest_index]:
      biggest_index = i
    
  return biggest_index
  

def bubbleBig(numbers):
  sortedNumbers = []

  for i in range(len(numbers)):
    bigNumber = findBiggest(numbers)

    sortedNumbers.append(numbers.pop(bigNumber))
  print(sortedNumbers)

numbers = [3,5,2,5,6,8,4,4,9,6,0,0,34,65]

bubbleBig(numbers)
