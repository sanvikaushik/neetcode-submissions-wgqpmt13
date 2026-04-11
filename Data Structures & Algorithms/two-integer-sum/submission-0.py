class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        i = 0

        for num in nums:
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i # [3] : 1
            i = i + 1
