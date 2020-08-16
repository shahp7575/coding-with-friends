"""
Implemented Kadane's algorithm!

Runtime: 92 ms
Memory: 14.8 MB
"""

from typing import List

class Solution:

    """
    Problem Statement:
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.

    Input: [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    """
    
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])

        return max(nums)

if __name__ == "__main__":

    result = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(result.maxSubArray(nums))