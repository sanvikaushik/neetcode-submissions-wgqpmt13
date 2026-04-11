class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}

        if len(s) == len(t):
            # proceed
            for c1 in s:
                if c1 in char_count: # if character already in dict
                    char_count[c1] += 1
                else:
                    char_count[c1] = 1
            
            for c2 in t:
                if c2 not in char_count:
                    return False
                char_count[c2] -= 1
                if char_count[c2] == 0:
                    del char_count[c2]

        else:
            return False

        # if no hashmap
        if not char_count:
            return True

        return False
