import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Storage as tuple (freq, number)
        heap: list = []
        #O(N)
        frequency_map: dict = Counter(nums)

        # Go through each entry and push them into a max heap
        #O(N)
        for num,freq in frequency_map.items():
            # O(logK)
            heapq.heappush(heap, (freq,num))

            if len(heap) > k:
                # pop minimum values O(logK)
                heapq.heappop(heap)

        return [num for freq,num in heap] 


