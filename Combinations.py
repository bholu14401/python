"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:
Input: n = 1, k = 1
Output: [[1]]
"""
class Solution(object):
    def combine(self, n, k):
        res = []
        self.get_combine(res, [], n, k, 1)
        return res
    def get_combine(self, res, prefix, n, k, start):
        if k == 0:
            res.append(list(prefix))
        elif start <= n:
            prefix.append(start)
            self.get_combine(res, prefix,n, k - 1, start + 1)
            prefix.pop()
            self.get_combine(res, prefix,n, k, start + 1)        
