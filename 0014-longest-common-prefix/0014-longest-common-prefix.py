class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for str in strs[1:]:
            i = 0
            while i < len(common_prefix) and i < len(str) and common_prefix[i] == str[i]:
                i += 1
            common_prefix = common_prefix[:i]
            if not common_prefix:
                return ""
    
        return common_prefix
        


            