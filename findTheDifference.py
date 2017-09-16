class Solution(object):
    def findTheDifference(self, s, t):
        t = list(t)
        for i in range(len(s)):
            t.remove(s[i])
        return t[0]
        """
        :type s: str
        :type t: str
        :rtype: str
        """
