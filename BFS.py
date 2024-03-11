def breadthFirstSearch(graph, source):
  queue = [source]

  while len(queue) != 0:
    current = queue.pop(0)
    print(current)
    for n in graph[current]:
      queue.append(n)

graph = {
  'a': ['c', 'b'],
  'b': ['d'],
  'c': ['e'],
  'd': ['f'],
  'e': [],
  'f': []
}

breadthFirstSearch(graph, 'a')