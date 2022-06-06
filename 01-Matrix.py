"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
class Solution:
    def updateMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dist = [[-1 for j in range(n)] for i in range(m)]
        visited = set()
        level = set((i,j) for i in range(m) for j in range(n) if matrix[i][j]==0)
        d = 0
        while level:
            for (i,j) in level:
                dist[i][j] = d
            d += 1
            visited |= level
            level = set((i+x,j+y) for (i,j) in level for (x,y) in [(0,1),(0,-1),(1,0),(-1,0)] if 0<=i+x<m and 0<=j+y<n and (i+x,j+y) not in visited)
        return dist
    
