"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        row, col= len(grid), len(grid[0])
        count=0 
        counted={}

        def dfs(R,C):
            if(R<0 or R>=row or C<0 or C>=col or grid[R][C] == 0 or (R,C) in counted):
                return 0
            counted[(R,C)] = True
            left = dfs(R,C-1)
            right = dfs(R,C+1)
            top = dfs(R-1,C)
            bottom = dfs(R+1,C)
            return 1 + left + right + top + bottom
            

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:

                    count=max(count,dfs(r,c))                       
        return count
   
