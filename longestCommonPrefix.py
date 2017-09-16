class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        shortest = min(strs)
        longest = max(strs)
        for index, char in enumerate(shortest):
            if char != longest[index]:
                return shortest[:index]
        return shortest
