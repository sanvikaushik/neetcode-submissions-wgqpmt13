class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = 3 * [0]
        
        #  [0, 1, 2]   
        for i in range(len(nums)):
            counts[nums[i]] += 1
        
        # [1, 2, 1] -> [0, 1, 1, 2]
        x = 0
        for i in range(len(counts)): # 0, 1, 2
            
            for j in range(counts[i]): # 1, 2, 1
                
                nums[x] = i
                x += 1

        return nums