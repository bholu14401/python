class Solution(object):
    def twoSum(self, nums, target):
        x = len(nums)
        ext = list()
        bottom = 0
        top = x-1
        while(top>=bottom):
  
            if( nums[bottom] + nums[top] == target):
              
                if len(ext)<2: 
                    if top!=bottom:
                        ext.append(bottom+1)
                        ext.append(top+1)
                return ext
            elif (nums[bottom] + nums[top] > target):  
                top = top - 1
            else:
                bottom = bottom + 1
