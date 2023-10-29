class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numbers = {}
        for num in nums:
            if num not in numbers:
                numbers[num] = 1
            else:
                numbers[num] += 1
        majority_element = max(numbers, key= lambda key: numbers[key])
        return majority_element
        