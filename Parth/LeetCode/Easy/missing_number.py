"""
Runtime: 140 ms
Memory: 15.1 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
    
    Input: [3,0,1]
    Ouptut: 2

    Note:
    Your algorithm should run in linear runtime complexity. 
    Could you implement it using only constant extra space complexity?
    """

    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)
            
if __name__ == "__main__":

    result = Solution()
    nums = [0,1,3]
    print(result.missingNumber(nums))