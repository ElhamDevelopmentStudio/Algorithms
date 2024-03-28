def gridTraveler(m, n, memo = {}):
  if (m, n) in memo:
    return memo[(m, n)]
  if m == 0 or n == 0:
    return 0
  if m == 1 and n == 1:
    return 1
  
  memo[(m, n)] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
  return memo[(m, n)]

print(gridTraveler(130, 70))

  
  