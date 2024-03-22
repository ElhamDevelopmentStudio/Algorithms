"""
here we find the multiplication result of highest 3 numbers in an array, we also consider if there is two high negative number the result of them would be a positive and might be higher than 3 positive number so we adjust our solution accordingly.
source: https://www.youtube.com/watch?v=bC7o8P_Ste4&t=738s
"""

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