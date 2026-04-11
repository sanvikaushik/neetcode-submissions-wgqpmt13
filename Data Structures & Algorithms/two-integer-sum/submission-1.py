class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        index = 0

        for num in nums:

            complement = target - num  # to see if there is a pair

            if complement in seen:
                return [seen[complement], index]
            
            seen[num] = index
            index += 1


            