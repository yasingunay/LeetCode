class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        
        while n != 1:
            if n in numbers:
                return False
            numbers.add(n)
            
            sum_of_squares = 0
            while n > 0:
                digit = n % 10
                sum_of_squares += digit ** 2
                n //= 10
            n = sum_of_squares
        return True