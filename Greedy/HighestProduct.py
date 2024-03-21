def HighestProduct(arr):
  arr.sort(reverse = True)
  product = 1
  productLow = 1
  for i in range(0, 3):
    product = product * arr[i]
  
  productLow = arr[-1] * arr[-2] * arr[0]
  
  return max(product, productLow)

arr = [-5,-2,-1,0,0,1,1,5]
print(HighestProduct(arr))