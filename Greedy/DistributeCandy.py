"""
The way this challenge works is you have an array of people and each person has a rating in the array down below
there is 5 people or len(kids) and each person has a rating associated with it, our objective here is to assign
at least 1 candy to each kid but if the rating of the kid is higher he gets more candy, for example the first kid
has a rating of one and gets one candy, the second one has a rating of 7 so we give him 2, the third one is less than
7 so we give him 1 candy and so on and so forth.
Source: https://www.youtube.com/watch?v=bC7o8P_Ste4&t=738s
"""

kids = [1,7,4,3,1]

base = kids[0]
candy = 1
totalCandy = 1

for i in range(1, len(kids)):
  if kids[i] > kids[i - 1]:
    candy += 1
  else:
    candy = 1
  totalCandy += candy


print(totalCandy)
