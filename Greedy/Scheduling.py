def schedule(arr):
  arr.sort(key= lambda x: x[1])

  currentSchedule = []
  thisTime = 0
  counter = 0

  for start, end in arr:
    if start >= thisTime:
      currentSchedule.append((start, end))
      thisTime = end
      counter += 1

  return counter

arr = list(map(int, input().split()))
print(schedule(arr))

  
