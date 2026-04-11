class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        close_to_open = {')': '(', '}': '{', ']': '['}
        

        stack = []

        for ch in s:

            if ch in close_to_open:
                # closing
                if not stack or stack[-1] != close_to_open[ch]:
                    return False

                stack.pop()
            # open
            else:
                stack.append(ch)

        
        return len(stack) == 0

