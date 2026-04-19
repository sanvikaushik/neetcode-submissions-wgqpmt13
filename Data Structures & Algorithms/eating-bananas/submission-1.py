from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # minimum k such that within h hours

        l = 1
        r = max(piles)
        

        while l <= r:

            k = (l + r) // 2
            time = 0

            for pile in piles:
                time += ceil(pile / k)

            if time <= h:
                r = k - 1

            else:
                l = k + 1

        return l


        