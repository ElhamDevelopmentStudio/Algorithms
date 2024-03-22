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
