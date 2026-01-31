import heapq
li=[]
heapq.heappush(li,6)
heapq.heappush(li,1)
heapq.heappush(li,12)
heapq.heappush(li,7)

print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
#if added - then it's max heap, if +ve its min heap