class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        max_c = 0
        curr_c = 0 

        for i in range(len(nums)):
            
            if nums[i] == 1:
                curr_c += 1
            else:
                curr_c = 0
            
            max_c = max(curr_c, max_c)
        return max_c