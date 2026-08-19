class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for num, freq in count.items():
            
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            
            else:
                if freq > heap[0][0]: 
                    heapq.heappush(heap, (freq, num))
                    heapq.heappop(heap)    

        return [item[1] for item in heap]
       