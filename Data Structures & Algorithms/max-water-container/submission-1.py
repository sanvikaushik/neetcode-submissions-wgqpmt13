class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        max_area = 0

        while l < r:

            h = min(heights[l], heights[r])
            w = r - l

            if heights[l] == h:
                l += 1
            else:
                r -= 1

            max_area = max(max_area, h * w)

        return max_area
