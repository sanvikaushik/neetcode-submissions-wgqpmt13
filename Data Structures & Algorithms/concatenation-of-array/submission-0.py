class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return

        n = len(nums)
        ans = [0] * len(nums) * 2

        for i in range(len(nums) * 2):
            if i <= len(nums) - 1:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-n]

        return ans