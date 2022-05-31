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
  
                
        
        
        
        
        
        
        
        
