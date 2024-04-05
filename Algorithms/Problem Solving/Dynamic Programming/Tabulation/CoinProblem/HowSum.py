def HowSum(target, coins):
  if target == 0:
    return []
  
  table = [None] * (target + 1)
  table[0] = []

  for i in range(len(table)):
    if table[i] != None:
      for c in coins:
        if i + c < len(table):
          tempResult = table[i] + [c]
          if table[i + c] is None:
            table[i + c] = tempResult
          else:
            if len(table[i + c]) > len(tempResult):
              table[i + c] = tempResult  


  return table[target]

print(HowSum(7, [5,3,4,7]))