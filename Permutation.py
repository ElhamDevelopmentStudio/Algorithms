from itertools import permutations


arr = [1,2,3]
this = permutations(arr,len(arr))

print(this.__sizeof__())

print(list(this))
