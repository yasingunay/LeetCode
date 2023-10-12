class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      result =[]
      result.append(nums[0])  # Add the first element of 'nums' to the 'result' list
      for number in nums[1:]:
        n = result[-1] + number  #result[-1] refers to the last element in the result list.
        result.append(n)

      return result
