class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        out = []

        # O(n)
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # O(n)
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        freq_keys = list(sorted_freq.keys())
        
        return freq_keys[0:k]
