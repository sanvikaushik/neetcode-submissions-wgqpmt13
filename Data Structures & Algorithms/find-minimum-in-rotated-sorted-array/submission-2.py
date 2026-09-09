class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] <= nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1