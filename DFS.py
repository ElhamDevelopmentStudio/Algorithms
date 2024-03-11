
def depthFirstSearch(graph, source):
  stack = [source]

  while len(stack) != 0:
    current = stack.pop()
    print(current)

    for n in graph[current]:
      stack.append(n)


# Recursive verison of the algorithm.
def depthFirstSearchRecursive(graph, source):
  print(source)

  for n in graph[source]:
    depthFirstSearchRecursive(graph, n)


graph = {
  'a': ['b', 'c'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

depthFirstSearchRecursive(graph, 'a')