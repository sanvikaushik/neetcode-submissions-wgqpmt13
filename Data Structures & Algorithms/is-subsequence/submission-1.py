class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sub = ""

        i = 0
        j = 0

        while i < len(s) and j < len(t):
            
            if s[i] == t[j]:
                sub += t[j]
                i += 1

            j += 1
        return sub == s