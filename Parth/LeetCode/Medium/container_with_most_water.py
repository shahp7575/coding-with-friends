"""
Runtime: 180 ms (faster than 14.8%)
Memory: 16.3 MB (Less than 81.52%)
"""

from typing import List

class Solution:
    
    """
    Problem # 11:
    Given n non-negative integers a1, a2, ..., an , 
    where each represents a point at coordinate (i, ai). 
    n vertical lines are drawn such that the two endpoints of the line i is at 
    (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, 
    such that the container contains the most water.
    """

    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height) - 1
        water = 0

        while i < j:

            water = max(water, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return water
        

if __name__ == "__main__":

    result = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(result.maxArea(height))