import heapq

data = [1,3,5,4,2,43,643,12,3]
heapq.heapify(data)
print(heapq.heappop(data))
print(data)
print(heapq.heappush(data, 2))
print(data)

moreData = [3,54,2,5,6,4,235,576,2,354]
mergedData = list(heapq.merge(data, moreData))
print(mergedData)

heapq._heapify_max(data)
print(data)
heapq._heappop_max(data)
print(data)