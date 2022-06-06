"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]
"""

class Solution(object):
    def letterCasePermutation(self, S):

        result = [[]]
        for c in S:
            if c.isalpha():
                for i in xrange(len(result)):
                    result.append(result[i][:])
                    result[i].append(c.lower())
                    result[-1].append(c.upper())
            else:
                for s in result:
                    s.append(c)
        return map("".join, result)
