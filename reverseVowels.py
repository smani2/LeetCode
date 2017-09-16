class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        # as_dict = {}
        # for index, char in enumerate(s):
        #     if char in vowels:
        #         as_dict[index] = char
        s = list(s)
        end = len(s) - 1
        forward = 0
        while forward < end:
            if (s[forward] in vowels) and (s[end] in vowels):
                tmp = s[forward]
                s[forward] = s[end]
                s[end] = tmp
                forward += 1 
                end -= 1
            elif s[forward] not in vowels:
                forward += 1
            else:
                end -= 1
        return "".join(s)