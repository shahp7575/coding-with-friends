"""
Runtime: 32 ms
Memory: 13.8 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
    """

    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1
            print(row)

            for j in range(1, len(row)-1):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
        
        return triangle

if __name__ == "__main__":

    result = Solution()
    num = 5
    print(result.generate(num))
        