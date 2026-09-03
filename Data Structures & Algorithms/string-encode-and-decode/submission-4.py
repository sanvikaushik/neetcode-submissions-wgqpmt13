class Solution:

    def encode(self, strs: List[str]) -> str:

        # store lengths
        res = ""
        
        for word in strs:
            res += str(len(word)) + "%" + word 

        return res


    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):

            j = i

            while s[j] != "%":
                j += 1

            # get length -> to avoid digits just get length
            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            
            i = j + 1 + length

            res.append(word)
                
        return res