def simple_heap(nums):
    heap = []
    for num in nums:
        heap.append(num)
        i = len(heap) - 1
        while i > 0 and heap[(i - 1) // 2] < heap[i]:
            heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
            i = (i - 1) // 2
    return heap

nums = list(map(int, input().split()))
print(simple_heap(nums))
