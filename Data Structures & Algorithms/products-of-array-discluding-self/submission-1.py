class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = 1
        for i in range(1, len(prefix)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        suffix[len(suffix) - 1] = 1
        for i in range(len(suffix) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        for i in range(0, len(nums)):
            nums[i] = prefix[i] * suffix[i]
        
        return nums
