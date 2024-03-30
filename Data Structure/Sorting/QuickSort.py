def quickSort(numbers):
  if len(numbers) < 2:
    return numbers

  pivot = numbers[int(len(numbers) / 2)]

  smallerNumbers = [i for i in numbers[1:] if i <= pivot]
  biggerNumbers = [i for i in numbers[1:] if i > pivot]

  return quickSort(smallerNumbers) + [pivot] + quickSort(biggerNumbers)

numbers = list(map(int, input().split()))
print(quickSort(numbers))