class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # non decreasing -> sorted
        # remove duplicates IN-PLACE
        k = 0
        keep_track = set()

        for num in nums:

            if num not in keep_track:
                nums[k] = num 
                k += 1
            keep_track.add(num)

        return k
            