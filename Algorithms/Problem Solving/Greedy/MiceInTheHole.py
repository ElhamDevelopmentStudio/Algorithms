mice = [3,2,-4]
holes = [0,-2,4]

def MiceInHole():
  mice.sort()
  holes.sort()

  # mice = [-4, 2, 3]
  # hole = [-2, 0, 4]
  differences = []

  for i in range(len(mice)):
    differences.append(abs(mice[i] - holes[i]))

  return max(differences)

print(MiceInHole())