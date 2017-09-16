class Solution(object):
    def twoSum(self, nums, target):
        lst = list()
        dictionary = dict()
        curr_index = 0
        for item in nums:
            values = dictionary.keys()
            if (target - item) in values:
                lst.append(dictionary.get(target-item)[1])
                lst.append(curr_index)
                return lst
            dictionary[item] = (target - item, curr_index)
            curr_index += 1
