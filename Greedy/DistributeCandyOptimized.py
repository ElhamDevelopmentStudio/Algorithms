"""
Source: https://www.youtube.com/watch?v=bC7o8P_Ste4&t=738s
"""

kids = [1,2,7,4,3,3,1]

base = kids[0]
data = [(x, i) for i, x in enumerate(kids)]
candies = [1] * len(kids)  

for x, i in data:
  if i > 0 and kids[i] > kids[i - 1]:
    candies[i] = max(candies[i], 1 + candies[i -1])
  if i < (len(kids) - 1) and kids[i] > kids[i + 1]:
    candies[i] = max(candies[i], 1 + candies[i + 1]) 

print(sum(candies))