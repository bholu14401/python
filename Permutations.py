"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
"""
class Solution:
    def permute(self, nums):
        # DPS with swapping
        res = []
        if len(nums) == 0:
            return res
        self.get_permute(res, nums, 0)
        return res

    def get_permute(self, res, nums, index):
        if index == len(nums):
            res.append(list(nums))
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            # s(n) = 1 + s(n-1)
            self.get_permute(res, nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]
