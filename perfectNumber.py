class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        add_val = 0
        for i in range(1, int(math.ceil(math.sqrt(num)))):
            if (num % i == 0):
                add_val += i
                add_val += num / i
        if (add_val == 2 * num):
            return True
        else:
            return False
