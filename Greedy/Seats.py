def seats (arr):
  indexOfPeople = [i for i, x in enumerate(arr) if x =="x"]
  
  middle = indexOfPeople[len(indexOfPeople) // 2]
  difference = 0
  for key in indexOfPeople:
    if key == middle:
      continue
    else:
      difference += abs(key - middle) - 1
  
  return difference

this = "...x..x..x"
print(seats(this))
