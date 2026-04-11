class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        c = 0
        m_c = 0
        for num in nums:
            
            if num == 1:
                c += 1
            else:
                c = 0

            m_c = max(c, m_c)
        return m_c