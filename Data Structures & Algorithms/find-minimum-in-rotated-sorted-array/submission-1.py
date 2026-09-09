class Solution:
    def findMin(self, nums: List[int]) -> int:

        # not rotated
        if nums[0] <= nums[-1]:
            return nums[0]

        # min value will ALWAYS be next to greatest value
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            # left high section
            if nums[mid] >= nums[0]:
                l = mid + 1
            
            else: 
                r = mid - 1