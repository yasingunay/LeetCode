class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        reversed_array = [-1]
        max = 0
        for num in arr[::-1]:
            if max < num:
                max = num
            reversed_array.append(max)
        reversed_array.pop()

        return(reversed_array[::-1])
      
     
       
       

