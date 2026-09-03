class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_count = [0] * 26
        t_count = [0] * 26

        for ch in s:
            s_count[ord(ch) - ord('a')] += 1
        
        for ch in t:
            t_count[ord(ch) - ord('a')] += 1

        return s_count == t_count