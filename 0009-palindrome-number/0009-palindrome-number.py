class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_str = str(x)
        reversed_str = num_str[::-1]
        if num_str == reversed_str:
            return True
        else:
            return False
        