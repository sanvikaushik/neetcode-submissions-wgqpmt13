class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for ch in s: # iterate character by character

            count[ch] += 1
        
        for ch in t:
             
            count[ch] -= 1

            if count[ch] == 0:
                del count[ch]

        return not count