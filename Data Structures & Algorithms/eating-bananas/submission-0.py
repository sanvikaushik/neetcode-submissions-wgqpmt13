from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        ans = r

        while l <= r:

            k = (l + r) // 2
            hours = 0

            for pile in piles:
                hours += ceil(pile / k)

            if hours <= h:
                ans = k
                r = k - 1 # keep moving left 
            
            else:
                l = k + 1
        return ans 