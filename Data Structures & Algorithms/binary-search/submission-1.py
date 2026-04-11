class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1

        l = 0
        r = len(nums) - 1

    
        while l <= r:
            mid = (r + l) // 2

            if target < nums[mid]:
                r = mid - 1
            
            elif target > nums[mid]:
                l = mid + 1
            
            else:
                return mid

        return -1