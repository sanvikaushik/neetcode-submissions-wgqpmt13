class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        max_len = 0

        for num in nums:
            if num not in seen:
                seen.add(num)
        
        for num in nums:

            if num - 1 in seen:
                continue
            
            seq = num + 1
            seq_len = 1

            while seq in seen:
                seq += 1
                seq_len += 1
            
            max_len = max(max_len, seq_len)
        
        return max_len