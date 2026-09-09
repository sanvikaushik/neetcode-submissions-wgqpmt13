class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets = { ']' : '[',
                     ')' : '(',
                     '}' : '{'
                    }

        for i in range(len(s)):

            if s[i] not in brackets:
                stack.append(s[i])
            
            else: # closing
                if not stack:
                    return False
                
                if stack and brackets[s[i]] != stack[-1]:
                    return False
                else:
                    stack.pop()

        return not stack