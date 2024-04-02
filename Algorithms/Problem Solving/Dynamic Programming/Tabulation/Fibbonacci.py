"""
Source: https://youtu.be/oBt53YbR9Kk?t=12085
Description: Create a fibbonaci sequence program using the tabulation method in dynamic programming. Time Complexity: O(n),
Space Complexity: O(n)
"""

# def fib(n):
#   tabulation = [0] * (n + 1)
#   tabulation[1] = 1

#   for i in range(2, len(tabulation)):
#     tabulation[i] = tabulation[i - 1] + tabulation[i - 2]

#   return tabulation[n]

def fib(n):
  tabulation = [0] * (n + 1)
  tabulation[1] = 1

  for i in range(n):
    if i + 1 <= n:
        tabulation[i + 1] += tabulation[i]
    if i + 2 <= n:
        tabulation[i + 2] += tabulation[i]
  
  return tabulation[n]

print(fib(7)) 