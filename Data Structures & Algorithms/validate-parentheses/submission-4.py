class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0 or len(s) % 2 != 0:
            return False

        brackets = {
            '(': ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []
        for ch in  s:

            if ch in brackets:
                # closing
                stack.append(ch)

            else:

                if len(stack) == 0:
                    return False
                    
                if ch == brackets.get(stack[-1]):
                    stack.pop()
                else: 
                    return False

        return not stack
        
        

