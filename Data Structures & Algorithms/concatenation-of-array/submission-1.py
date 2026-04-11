class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []
        x = len(nums)

        for i in range(2 * len(nums)):
            ans.append(nums[i % x])

        return ans
