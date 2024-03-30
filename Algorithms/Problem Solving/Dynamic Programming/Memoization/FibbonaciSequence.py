"""
Source: https://www.youtube.com/watch?v=oBt53YbR9Kk
Description: Used memoization technique to reduce the time complexity from O(2^n) to O(n)
and space complexity remained the same O(n)
"""

def fib(n, memo = {}):
  if n in memo:
    return memo[n]
  if n <= 2:
    return 1
  else:
    memo[n] =  fib(n - 1) + fib(n - 2)
    return memo[n]
  
print(fib(200))