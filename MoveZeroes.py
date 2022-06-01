"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        while i < len(nums) :
            
            if nums[i] == 0:
                nums.append(0)
                nums.remove(0)
                i = i + 1
            else:
                i = i + 1
  
                
        
        
        
        
        
        
        
        
