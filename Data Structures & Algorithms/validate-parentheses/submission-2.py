class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"]": "[", "}":"{", ")":"("}

        for ch in s:
            if ch not in m:
                stack.append(ch)
            else:
                if stack and m[ch] == stack[-1]:
                    stack.pop()
                else:
                   return False 
        return True if len(stack) == 0 else False