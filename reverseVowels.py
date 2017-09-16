class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = list(s)
        backward = len(s) - 1
        forward = 0
        while forward < backward:
            if (s[forward] in vowels) and (s[backward] in vowels):
                tmp = s[forward]
                s[forward] = s[backward]
                s[backward] = tmp
                forward += 1 
                backward -= 1
            elif s[forward] not in vowels:
                forward += 1
            else:
                backward -= 1
        return "".join(s)