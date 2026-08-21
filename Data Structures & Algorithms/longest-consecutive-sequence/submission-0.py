class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set()
        max_len = 0

        # initial set (no duplicates)
        for num in nums:
            if num not in seen:
                seen.add(num)
        

        for num in nums:

            # iterate until
            if num - 1 in seen:
                continue
                
            # found a beginning
            seq = num
            seq_len = 1
            while seq + 1 in seen:
                seq += 1
                seq_len += 1

            max_len = max(seq_len, max_len)

        return max_len
        

        # now continue finding beginning
                
