class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        close = [')', '}' , ']' ]
        pair = {'(':')', '{':'}' , '[': ']' }
        
        for char in s:
            if char in open:
                stack.append(char)
            elif char in close:
                if not stack or pair.get(stack[-1]) != char:
                    return False
                stack.pop()
        return not stack