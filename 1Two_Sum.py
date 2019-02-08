"""
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
给定一个整数数列，找出其中和为特定值的那两个数。
你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

def twoSum(self, nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
"""


class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_dict = {}
        for index, value in enumerate(nums):
            if (target - value) in new_dict:
                return [new_dict[target - value], index]
            if not new_dict.get(value):
                new_dict[value] = index


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    print(Solution().two_sum(nums, 9))
