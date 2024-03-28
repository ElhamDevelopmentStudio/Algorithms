meetings = list(map(int, input().split()))

timeline = []
currentTime = 0
maxTime = 0

for start, end in meetings:
  timeline.append((start, +1))
  timeline.append((end, -1))

timeline.sort()

for s, n in timeline:
  currentTime += n
  if currentTime > maxTime:
    maxTime = currentTime
  # print(f"Current time: {currentTime}")
  # print(f"Max time: {maxTime}")
    
print(maxTime)