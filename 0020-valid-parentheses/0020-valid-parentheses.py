class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        close = [')', '}', ']']
        pair = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in open:
                stack.append(char)
            elif char in close:
                if not stack or pair.get(stack[-1]) != char:
                    return False
                stack.pop()
        return not stack

def main():
    solution = Solution()

    # Test cases
    test_strings = ["()", "[", "()[]{}", "(]", "([)]", "{[]}", "((()))", "((())", "(()))"]
    
    for test_str in test_strings:
        result = solution.isValid(test_str)
        print(f"Input: {test_str}, Result: {result}")

if __name__ == "__main__":
    main()
